from my_app import *
from flask import redirect, render_template, url_for, request
from flask import flash, jsonify
from flask_login import login_required, login_user, logout_user, current_user
from my_app.forms import *
from my_app.models import *

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/get_lessons', methods=['GET'])
def get_lessons():
    if request.method == 'GET':
        lessons = Lessons.query
        return jsonify(list(map(lambda x: x.to_dict(), lessons)))


@app.route('/get_user', methods=['GET'])
def get_user():
    if request.method == 'GET':
        return jsonify(id=current_user.id,
                       studies=current_user.studies)


@app.route("/", methods=['POST','GET'])
@login_required
def homepage():
        return render_template("home.html")

@app.route('/get_event', methods=['GET'])
def get_event():
    if request.method == 'GET':
        event = event.query
        return jsonify(list(map(lambda x: x.to_dict(), event)))

# Fonction de connexion
@app.route("/")
@app.route('/loginForm', methods=['GET', 'POST'])
def login():

    # Si l'utilisateur est connecté, il accède à la page d'accueil
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))

    # Récupérer les infos entrées dans le formulaire
    form = LoginForm()
    if form.validate_on_submit():
      # On cherche l'adresse mail de l'utilisateur dans la base de données
        user = User.query.filter_by(eid=form.mail.data).first()
        # Pour le connecter, il faut que l'utilisateur existe dans la base de données, que le mot de passe entré soit identique à celui présent dans la base de données, et qu'il ne soit pas bloqué
        if user is None:
            flash('You are not registered yet', 'info')
            return redirect(url_for('login'))
        elif not user.check_password(form.password.data):
            flash('Invalid email or password', 'info')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('homepage'))


    else:
        return render_template('loginForm.html', form = form)


# Fonction de création de compte
@app.route('/createAccount', methods=['GET', 'POST'])
def register():

    form = LoginForm()
    regform = RegistrationForm(request.form)

    if request.method=='POST' and regform.validate_on_submit():
        # Création de l'objet User avec les données entrées dans le formulaire
        user = User(eid=regform.Mail.data,fstname=regform.Firstname.data,name=regform.Surname.data, studies=regform.Formation.data)
        # Récupération du mot de passe pour le hasher et le stocker dans la base de données user
        user.set_password(regform.Password.data)
        db.session.add(user)
        db.session.commit()
        li = regform.Year.data
        year=""
        for i in li :
            year=i
            years = Years(name=year,user=user)
            db.session.add(years)
            db.session.commit()
        flash('Thanks for registering')
        # Arrivée sur la page de login
        return render_template('loginForm.html', form = form)
    else:
        return render_template('createAccount.html', form = regform)


# @login_manager.user_loader
# def load_user(userid):
#     return User.query.get(int(userid))

# Déconnexion de l'utilisateur
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


########### CREATION EVENTS #####################
@app.route('/creation', methods=['GET', 'POST'])
@login_required
def event_creation():
    form = CreationForm()
    if form.validate_on_submit():
        new_event = event(title=form.name.data, description=form.description.data, start_hour=str(form.begin_hour.data), end_hour=str(form.end_hour.data), user_id=current_user.id, color=form.color.data)
        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for('homepage'))

    return render_template("creation.html", form=form)


@app.route('/modEvent/<int:id>', methods=['POST', 'GET'])
@login_required
def modEvent(id):
    form = editEventForm()
    if form.validate_on_submit():
        Event = event.query.filter_by(author = current_user, id=id).first()
        if form.title.data:
            Event.title = form.title.data
        if form.description.data:
            Event.description = form.description.data

        if form.start_hour.data and form.end_hour.data and form.start_hour.data != 'Default' and form.end_hour.data != 'Default':
            if int(form.start_hour.data[0:2]) <= int(form.end_hour.data[0:2]):
                Event.start_hour = form.start_hour.data
                Event.end_hour = form.end_hour.data
            else:
                flash('Start hour must be before end hour!', 'info')
                return render_template("modEvent.html", form = form)
        if form.start_hour.data and form.end_hour.data and form.start_hour.data != 'Default' and form.end_hour.data == 'Default':
            flash('End hour missing!', 'info')
            return render_template("modEvent.html", form = form)
        if form.start_hour.data and form.end_hour.data and form.start_hour.data == 'Default' and form.end_hour.data != 'Default':
            flash('Start hour missing!', 'info')
            return render_template("modEvent.html", form = form)

        if form.color.data and form.color.data != 'default':
            Event.color = form.color.data
        db.session.commit()
        return redirect('/')
    return render_template("modEvent.html", form = form)


@app.route('/delete/<int:id>')
@login_required
def delete(id):
    print(event.query.filter_by(author = current_user, id=id).first())
    Event = event.query.filter_by(author = current_user, id=id).first()
    db.session.delete(Event)
    db.session.commit()
    return redirect('/')
