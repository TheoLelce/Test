from flask_login import UserMixin
from my_app import *
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    eid = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(80), unique=False, nullable=False)
    fstname = db.Column(db.String(80), unique=False, nullable=False)
    studies = db.Column(db.String(80), unique=False, nullable=False)
    year = db.relationship('Years', backref='user', lazy=True)

    def getPseudo(self):
        return self.username
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def isAdmin(self):
        return self.admin
    def __repr__(self):
        return "<User id: %d, eid: %s, name: %s, first name: %s>" % (self.id, self.eid, self.name, self.fstname)


class event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(80), nullable=True)
    start_hour = db.Column(db.String(80), nullable=False)
    end_hour = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    color = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return "<Event id: %d, title: %s, description: %s, start_hour: %s, end_hour: %s, color: %s>" % (self.id, self.title, self.description, self.start_hour.strftime('%Y-%m-%d %H:%m'), self.end_hour.strftime('%Y-%m-%d %H:%m'), self.color)

class Lessons(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    studies= db.Column(db.String(80), unique=False, nullable=False)
    years= db.Column(db.String(80), unique=False, nullable=False)
    title= db.Column(db.String(80), unique=False, nullable=False)
    location = db.Column(db.String(80), unique=False, nullable=False)
    jour = db.Column(db.String(80), unique=False, nullable=False)
    start_hour = db.Column(db.String(80), nullable=True)
    end_hour = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return "<Lessons id: %d,studies: %s,years: %s, title: %s, location: %s, start_hour: %s, end_hour: %s>" % (self.id, self.studies, self.years, self.title, self.location, self.start_hour, self.end_hour)

class Years(db.Model, SerializerMixin):
    tablename = 'years'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
db.drop_all()
db.create_all()

objects = [
Lessons(studies='Science informatique' , years='Bac 1', title='Fait et d??cisions ??conomique', location='Vauban', jour='Lundi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science informatique' , years='Bac 1', title='Fait et d??cisions ??conomique', location='Vauban', jour='Mercredi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science informatique' , years='Bac 1', title='TP-Eco-INFO A', location='E25', jour='Mardi', start_hour='8:30', end_hour='10:30' ),
Lessons(studies='Science informatique' , years='Bac 1', title='Programmation2', location='E01', jour='Vendredi',start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science informatique' , years='Bac 1', title='Fondement math(EX)- Groupe C', location='I01', jour='Lundi',start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science informatique' , years='Bac 1', title='Program(Ex)-Groupe A', location='I02', jour='Mardi', start_hour='10:40', end_hour='11:40'),
Lessons(studies='Science informatique' , years='Bac 1', title='N??erlandais 1', location='I32', jour='Mardi', start_hour='13:00', end_hour='14:00'),
Lessons(studies='Science informatique' , years='Bac 1', title='Program(EX)Pool-Groupe B', location='I21', jour='Mardi', start_hour='16:00', end_hour='18:00'),
Lessons(studies='Science informatique' , years='Bac 1', title='Analyse math??matique Ex-Groupe A', location='I30', jour='Jeudi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science informatique' , years='Bac 1', title='Analyse math??matique', location='I03', jour='Jeudi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science informatique' , years='Bac 1', title="Fondement math??matique pour l'info 1", location='M02', jour='Vendredi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science informatique' , years='Bac 1', title='N??erlandais 2', location='I30', jour='Vendredi', start_hour='13:00', end_hour='14:00'),
Lessons(studies='Science informatique' , years='Bac 1', title='Anglais 1-Groupe A', location='BUMP03', jour='Vendredi', start_hour='14:00', end_hour='16:00'),


#Bac2
Lessons(studies='Science informatique' , years='Bac 2', title='OS EX', location='I21', jour='Lundi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science informatique' , years='Bac 2', title='technique de programation', location='I32', jour='Lundi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science informatique' , years='Bac 2', title='OS', location='I03', jour='Lundi', start_hour='14:00', end_hour='16:00' ),
Lessons(studies='Science informatique' , years='Bac 2', title='Proba', location='I20', jour='Mardi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science informatique' , years='Bac 2', title='Technique de programmation(Ex)', location='I32', jour='Mardi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science informatique' , years='Bac 2', title="Fondements math??matique pour l'informatique 2 (Ex)", location='I01', jour='Mardi',start_hour='16:00', end_hour='18:00'),
Lessons(studies='Science informatique' , years='Bac 2', title='Proba', location='I20', jour='Mercredi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science informatique' , years='Bac 2', title='Anglais', location='130', jour='Mercredi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science informatique' , years='Bac 2', title='N??erlandais 1', location='I32', jour='Mardi', start_hour='13:00', end_hour='14:00'),
Lessons(studies='Science informatique' , years='Bac 2', title='Bases de donn??es 2', location='I20', jour='Mercredi', start_hour='16:00', end_hour='18:00'),
Lessons(studies='Science informatique' , years='Bac 2', title='Proba (EX)', location='I22', jour='Jeudi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science informatique' , years='Bac 2', title='Alg??bre 2', location='I02', jour='Jeudi',start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science informatique' , years='Bac 2', title='Mooc', location='I22', jour='Jeudi', start_hour='16:00', end_hour='18:00'),
Lessons(studies='Science informatique' , years='Bac 2', title='Alg??bre 2 (Ex)', location='I33', jour='Vendredi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science informatique' , years='Bac 2', title='N??erlandais 2', location='I30', jour='Vendredi', start_hour='13:00', end_hour='14:00'),
#Bac3
Lessons(studies='Science informatique' , years='Bac 3', title='Amsi(Ex)', location='I20', jour='Lundi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science informatique' , years='Bac 3', title='Techno Web', location='I21', jour='Lundi', start_hour='10:40', end_hour = '12:40'),
Lessons(studies='Science informatique' , years='Bac 3', title='Techno Web Ex', location='I21', jour='Lundi', start_hour='14:00', end_hour='16:00' ),
Lessons(studies='Science informatique' , years='Bac 3', title='R??seaux', location='I30', jour='Mardi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science informatique' , years='Bac 3', title='Anglais', location='I32', jour='Mardi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science informatique' , years='Bac 3', title="R??sseaux", location='I03', jour='Mardi',start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science informatique' , years='Bac 3', title='AMSI', location='I20', jour='Mercredi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science informatique' , years='Bac 3', title='IHM', location='132', jour='Mercredi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science informatique' , years='Bac 3', title='Programmation Fonctionnelle et logique', location='I20', jour='Jeudi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science informatique' , years='Bac 3', title='IHM (Ex)', location='I32', jour='Jeudi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science informatique' , years='Bac 3', title='Projet(TP)', location='I30', jour='Vendredi',start_hour='9:30', end_hour='11:30'),
Lessons(studies='Science informatique' , years='Bac 3', title='Projet(TP)', location='I30', jour='Vendredi',start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science informatique' , years='Bac 3', title='Programmation fonctionnelle et Logique(EX)', location='I20', jour='Vendredi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science informatique' , years='Bac 3', title='N??erlandais 2', location='I30', jour='Vendredi', start_hour='13:00', end_hour='14:00'),
#Bac 1
Lessons(studies='Science ??conomiques' , years='Bac 1', title='Fait et d??cisions ??conomique', location='Vauban', jour='Lundi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='Mod??le de calcul et BD', location='E01', jour='Lundi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='TP-Droit ECGE5', location='E27', jour='Lundi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='TP-Droit ECGE3', location='E27', jour='Lundi', start_hour='16:00', end_hour='18:00'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='NL1', location='E31-   E21', jour='Lundi', start_hour='18:00', end_hour='20:00'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='Math??matique pour ??co et gestion 1', location='E01', jour='Mardi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='Fondements du Droit', location='E01', jour='Mardi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='TP-stat ECGE2', location='E11', jour='Mardi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='TP-Droit ECGE4', location='E33', jour='Mardi', start_hour='16:00', end_hour='18:00'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='Anglais1', location='Vauban', jour='Mardi', start_hour='18:00', end_hour='20:00'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='Fait et d??cisions ??conomique', location='Vauban', jour='Mercredi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='TP-Math EcoGes', location='E01', jour='Mercredi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='TP-Eco', location='E23', jour='Mercredi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='TP-Eco', location='E25', jour='Mercredi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='TP Mod & BD', location='E04-E03', jour='Mercredi', start_hour='16:00', end_hour='18:00'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='Travaux dirig??s Math EcoGes', location='E01', jour='Mercredi', start_hour='18:00', end_hour='20:00'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='TP-stat', location='E24', jour='Jeudi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='TP-Math EcoGes', location='E33', jour='Jeudi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='TP Mod & BD', location='E05', jour='Jeudi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='Remediation Math EcoGes', location='E12', jour='Jeudi', start_hour='16:00', end_hour='18:00'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='TP-Math EcoGes', location='Vauban', jour='Vendredi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='TP Mod & BD', location='Vauban', jour='Vendredi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science ??conomiques' , years='Bac 1', title='TP-Math EcoGes', location='Vauban', jour='Vendredi', start_hour='14:00', end_hour='16:00'),
#Bac 2
Lessons(studies='Science ??conomiques' , years='Bac 2', title='Compta Finaci??re et analytique', location='D02', jour='Lundi', start_hour='8:30', end_hour='12:40'),
Lessons(studies='Science ??conomiques' , years='Bac 2', title='Macroeconomie', location='E01', jour='Lundi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science ??conomiques' , years='Bac 2', title='TP - Micro', location='E12', jour='Mardi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science ??conomiques' , years='Bac 2', title='TP math3', location='E24', jour='Mardi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science ??conomiques' , years='Bac 2', title='Micro??conomie', location='E014', jour='Mercredi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science ??conomiques' , years='Bac 2', title='TP-Macro', location='E22', jour='Mercredi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science ??conomiques' , years='Bac 2', title='TP-Micro', location='E23', jour='Mercredi', start_hour='16:00', end_hour='18:00'),
Lessons(studies='Science ??conomiques' , years='Bac 2', title='TP-Math3', location='E31', jour='Jeudi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science ??conomiques' , years='Bac 2', title='Langues', location='E33', jour='Jeudi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science ??conomiques' , years='Bac 2', title='Micro??conomie', location='E01', jour='Vendredi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science ??conomiques' , years='Bac 2', title='Anglais', location='E34-E31', jour='Vendredi', start_hour='14:00', end_hour='16:00'),
#Bac3
Lessons(studies='Science ??conomiques' , years='Bac 3', title='Anglais', location='E34', jour='Lundi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science ??conomiques' , years='Bac 3', title='TP-Econom??trie', location='E05', jour='Lundi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science ??conomiques' , years='Bac 3', title='NL3', location='E31', jour='Lundi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science ??conomiques' , years='Bac 3', title='Projet: Strategie et d??cisisons ??co. Coaching', location='E33', jour='Mardi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science ??conomiques' , years='Bac 3', title='Econom??trie', location='PA11', jour='Mardi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science ??conomiques' , years='Bac 3', title='Langues ', location='E31-E32', jour='Mardi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science ??conomiques' , years='Bac 3', title='TP-Finances', location='E04', jour='Mercredi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science ??conomiques' , years='Bac 3', title='Science religieuses', location='D02', jour='Mercredi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science ??conomiques' , years='Bac 3', title='Projet: Strategie et d??cisisons ??co. (me)', location='E13', jour='Mercredi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science ??conomiques' , years='Bac 3', title='Projet: Strategie et d??cisisons ??co. Anglais', location='E31', jour='Mercredi', start_hour='16:00', end_hour='18:00'),
Lessons(studies='Science ??conomiques' , years='Bac 3', title='Langues', location='E24', jour='Jeudi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science ??conomiques' , years='Bac 3', title='Projet: Strategie et d??cisisons ??co. (Je-ve)', location='E13', jour='Jeudi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science ??conomiques' , years='Bac 3', title='Finance', location='E01', jour='Jeudi', start_hour='14:00', end_hour='16:00'),
Lessons(studies='Science ??conomiques' , years='Bac 3', title='Strat??gie et leadership', location='E11', jour='Jeudi', start_hour='16:00', end_hour='18:00'),
Lessons(studies='Science ??conomiques' , years='Bac 3', title='TP Econom??trie', location='E05', jour='Vendredi', start_hour='8:30', end_hour='10:30'),
Lessons(studies='Science ??conomiques' , years='Bac 3', title="Economie de l'environement", location='E32', jour='Vendredi', start_hour='10:40', end_hour='12:40'),
Lessons(studies='Science ??conomiques' , years='Bac 3', title='Finance', location='E01', jour='Vendredi', start_hour='14:00', end_hour='16:00')]

db.session.bulk_save_objects(objects)

# for testing purposes
user = User(eid='admin@gmail.com',fstname='Admin',name='admin', studies='Science informatique')
user.set_password('admin')
db.session.add(user)
db.session.commit()
li = ['Bac 2', 'Bac 3']
year=""
for i in li :
    year=i
    years = Years(name=year,user=user)
    db.session.add(years)
    db.session.commit()


db.session.commit()
# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))
