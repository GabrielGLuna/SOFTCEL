from flask import Blueprint, render_template, redirect, url_for, abort
reparaciones_views = Blueprint('reparaciones',__name__)

from models.citas import Cita

from forms.citas_form import CreateCita
from models.cliente import Cliente
from models.reparacion import Reparacion
from models.usuarios import Usuario

@reparaciones_views.route("/Reparacion")
def reparacion():
    reps = Reparacion.get_all()
    return render_template('reparaciones/reparacion.html', reps=reps)

@reparaciones_views.route("/reparaciones/citas/", methods = ('GET','POST'))
def citas():
    form = CreateCita()
    if form.validate_on_submit():
      email_cliente = form.email_cliente.data
      dispositivo = form.dispositivo.data
      fecha = form.fecha.data
      cita = Cita(email_cliente=email_cliente, dispositivo=dispositivo, fecha=fecha)
      cita.save()
      return redirect(url_for('reparaciones.citas'))
    return render_template('reparaciones/citas.html', form=form)
