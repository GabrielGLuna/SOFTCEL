from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class CreateQuejaForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    telefono = StringField('telefono', validators=[DataRequired()])
    queja = TextAreaField('queja', validators=[DataRequired()])
    submit = SubmitField('Guardar')

