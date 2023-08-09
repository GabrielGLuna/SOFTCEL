from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, EmailField, 
                     SubmitField, ValidationError, TextAreaField,DateField)
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

from models.cliente import Cliente
class CreateCita(FlaskForm):
    dispositivo = StringField('dispositivo', validators=[DataRequired()])
    fecha = DateField('fecha', validators=[DataRequired()])
    submit = SubmitField('Guardar')

