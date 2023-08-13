from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SubmitField, FileField, DateField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename

class AddReparacionForm(FlaskForm):
    nombre = StringField('nombre', validators=[DataRequired()])
    caracteristicas = StringField('caracteristicas', validators=[DataRequired()])
    costo = FloatField('Costo', validators=[DataRequired()])
    fecha_entrada = DateField('fecha_entrada', validators=[DataRequired()])
    fecha_entrega = DateField('fecha_entrega', validators=[DataRequired()])
    cliente = StringField('Cliente', validators=[DataRequired()])
    folio = StringField('Folio', validators=[DataRequired()])
    estatus = StringField('Estatus', validators=[DataRequired()])
    comentarios = TextAreaField('Comentarios', validators=[DataRequired()])
    repimage = FileField('Imagen')
    idReparacion = StringField('ID de Reparación')
    submit = SubmitField('Agregar')