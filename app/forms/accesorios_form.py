from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField,TextAreaField, SelectField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.file import FileField, FileAllowed

from models.accesorios import Accesorio
class CreateAccesorioForm(FlaskForm):

    accs=[]
    
    categoria = StringField('categoria', validators=[DataRequired()])
    tipo = StringField('tipo', validators=[DataRequired()])
    stock = IntegerField('stock', validators=[DataRequired(), NumberRange(min=0, max=None)])
    color = StringField('color', validators=[DataRequired()])
    especificacionExtra = TextAreaField('especificacionExtra', validators=[DataRequired()])
    precio = FloatField('precio', validators=[DataRequired(), NumberRange(min=0.0, max=None)])
  
    image = FileField('Imagen de Producto', 
                      validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo imagenes!')])
    submit = SubmitField('Guardar')

class FiltroBusqueda(FlaskForm):
     precio = FloatField('precio', validators=[DataRequired(), NumberRange(min=0.0, max=None)])
     submit = SubmitField('Filtrar')

class UpdateAccesorioForm(FlaskForm):


    categoria = StringField('categoria', validators=[DataRequired()])
    tipo = TextAreaField('tipo', validators=[DataRequired()])
    color = StringField('color', validators=[DataRequired()])
    stock = IntegerField('stock', validators=[DataRequired(), NumberRange(min=0, max=None)])
    especificacionExtra = TextAreaField('especificacionExtra', validators=[DataRequired()])
    precio = FloatField('precio', validators=[DataRequired(), NumberRange(min=0.0, max=None)])
   
    image = FileField('Imagen de Producto', 
                      validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo imagenes!')])
    submit = SubmitField('Actualizar')