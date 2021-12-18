from wtforms.fields.choices import SelectField, SelectMultipleField
from wtforms.widgets.core import CheckboxInput
from my_app import *
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, widgets, DateField, TextAreaField, TimeField, validators
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo, DataRequired, ValidationError, Optional


class CreationForm(FlaskForm):
    name = StringField("Name of your event", validators=[validators.Length(min=3, max=25), validators.DataRequired()])
    date = DateField("Date of your event", format='%d/%m/%Y', validators=[validators.DataRequired()])
    begin_hour = TimeField("Depart time of the event",  format='%H:%M', validators=[validators.DataRequired()])
    end_hour = TimeField("End time of the event", format='%H:%M', validators=[validators.DataRequired()])
    description = TextAreaField('Description (optional) :', validators=[Optional()])
    color = StringField("Choose your color", validators=[validators.DataRequired()])
    submit = SubmitField('Add Event')

hours = ['Default', '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00','20:00', '21:00', '22:00', '23:00']
colors = [('default', 'Default'), ('red', 'Red'), ('white', 'White'), ('green', 'Green'), ('blue', 'Blue'), ('purple', 'Purple')]

class editEventForm( FlaskForm ):
     title = StringField('Title:')
     description = StringField('description:')
     start_hour =  SelectField('Start hour:', choices=hours)
     end_hour =  SelectField('End hour:', choices=hours)
     color = SelectField('Color:', choices=colors)
     submit  = SubmitField('Submit')

# fonctions de validation des différents champs
def validate_firstname(self, Firstname):
    excluded_chars = " *?!'^+%&/()=}][{$#1234567890"
    for char in self.Firstname.data:
        if char in excluded_chars:
            raise ValidationError(
                f"Character {char} is not allowed in firstname.")

def validate_surname(self,Surname):
    excluded_chars = " *?!'^+%&/()=}][{$#1234567890"
    for char in self.Surname.data:
        if char in excluded_chars:
            raise ValidationError(
                f"Character {char} is not allowed in surname.")

def validate_password(self,Password):
    excluded_chars = " *?!'^+%&/()=}][{$#"
    for char in self.Password.data:
        if char in excluded_chars:
            raise ValidationError(
                f"Character {char} is not allowed in password.")

def validate_email(self,Mail):
    excluded_chars = " *?!'^+%&/()=}][{$#"
    for char in self.Mail.data:
        if char in excluded_chars:
            raise ValidationError(
                f"Character {char} is not allowed in email.")
    content = self.Mail.data.split("@")
    if len(content) != 2:
        raise ValidationError("Mail error : could not find 2 distinct parts. Are you sure you used '@' as a separator ?")
    content_0=content[1].split(".")
    if len(content_0) != 2:
        raise ValidationError("Mail error : could not find 2 distinct parts. Are you sure you used '.' as a separator ?")

# mise en page des checkbox
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

# formulaire de connexion avec l'adresse mail
class LoginForm( FlaskForm ):
    mail = StringField('eID:', validators=[InputRequired(), Length(min=3, max=20)])
    password = PasswordField(label=('Mot de passe:  '), validators=[InputRequired(), Length(min=5,max=20)])
    submit   = SubmitField('Connexion')



# formulaire de création de compte
class RegistrationForm( FlaskForm ):
    Firstname    = StringField('Prénom:', validators=[InputRequired(), Length(min=2, max=20), validate_firstname])
    Surname = StringField('Nom:', validators=[InputRequired(), Length(min=2, max=20), validate_surname])
    Mail = StringField('eID:', validators=[InputRequired(), Length(min=5, max=50), validate_email])
    Formation= SelectField('Formation:', choices= ['Science informatique','Science économiques'])
    Year = MultiCheckboxField('Année(s):', choices= ['Bac 1', 'Bac 2', 'Bac 3'])


    Password = PasswordField(label=('Mot de passe:'), validators=[InputRequired(), Length(min=5, max=20), validate_password])
    Confirm_password = PasswordField(label=('Confirmer le mot de passe:'), validators=[InputRequired(), EqualTo('Password', message='Both password fields must be equal!')])
    submit  = SubmitField('Valider')
