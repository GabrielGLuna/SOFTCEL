from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField,TextAreaField, SelectField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.file import FileField, FileAllowed

from models.audio import Audio

class CreateAudioForm(FlaskForm):

    auds=[]
    
    marca = StringField('marca', validators=[DataRequired()])
    modelo = StringField('modelo', validators=[DataRequired()])
    conexion = StringField('conexion', validators=[DataRequired()])
    tipo = StringField('tipo', validators=[DataRequired()])
    stock = IntegerField('stock', validators=[DataRequired(), NumberRange(min=0, max=None)])
    precio = FloatField('precio', validators=[DataRequired(), NumberRange(min=0.0, max=None)])
  
    image = FileField('Imagen de Producto', 
                      validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo imagenes!')])
    submit = SubmitField('Guardar')

class UpdateAudioForm(FlaskForm):


    marca = StringField('marca', validators=[DataRequired()])
    modelo = StringField('modelo', validators=[DataRequired()])
    conexion = StringField('conexion', validators=[DataRequired()])
    tipo = StringField('tipo', validators=[DataRequired()])
    stock = IntegerField('stock', validators=[DataRequired(), NumberRange(min=0, max=None)])
    precio = FloatField('precio', validators=[DataRequired(), NumberRange(min=0.0, max=None)])
  
    image = FileField('Imagen de Producto', 
                      validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo imagenes!')])
    submit = SubmitField('Guardar')