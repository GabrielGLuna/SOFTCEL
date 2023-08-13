from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField,TextAreaField, SelectField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.file import FileField, FileAllowed


from models.celulares import Celular

class CreateCelularForm(FlaskForm):
   
    cels=[]
    
    marca = StringField('marca', validators=[DataRequired()])
    modelo = StringField('modelo', validators=[DataRequired()])
    color = StringField('color', validators=[DataRequired()])
    stock = IntegerField('stock', validators=[DataRequired(), NumberRange(min=0, max=None)])
    almacenamiento = StringField('almacenamiento', validators=[DataRequired()])
    condicion = StringField('condicion', validators=[DataRequired()])
    idProveedor = StringField('idProveedor', validators=[DataRequired()])
    precio = FloatField('precio', validators=[DataRequired(), NumberRange(min=0.0, max=None)])
    image = FileField('Imagen de Producto', 
    validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo imagenes!')])
    submit = SubmitField('Guardar')

class UpdateCelularForm(FlaskForm):
    marca = StringField('marca', validators=[DataRequired()])
    modelo = StringField('modelo', validators=[DataRequired()])
    color = StringField('color', validators=[DataRequired()])
    stock = IntegerField('stock', validators=[DataRequired(), NumberRange(min=0, max=None)])
    almacenamiento = StringField('almacenamiento', validators=[DataRequired()])
    condicion = StringField('condicion', validators=[DataRequired()])
    idProveedor = StringField('idProveedor', validators=[DataRequired()])
    precio = FloatField('precio', validators=[DataRequired(), NumberRange(min=0.0, max=None)])
  
    image = FileField('Imagen de Producto', 
                      validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo imagenes!')])
    submit = SubmitField('Guardar')