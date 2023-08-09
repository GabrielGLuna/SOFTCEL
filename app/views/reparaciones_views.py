from flask import Blueprint, render_template, redirect, url_for, abort
reparaciones_views = Blueprint('reparaciones',__name__)

from models.citas import Cita

from forms.citas_form import CreateCita
from models.cliente import Cliente
from models.reparacion import Reparacion
from models.usuarios import Usuario

@reparaciones_views.route("/<int:id>/Reparacion")
def reparacion(id):
    usuario = Usuario.get(id)
    if usuario is None: abort(404)
    rep = Reparacion.get(id)
    return render_template('reparaciones/reparacion.html', rep=rep)

@reparaciones_views.route("/reparaciones/<int:id>/citas/", methods = ('GET','POST'))
def citas(id):
    form = CreateCita()
    if form.validate_on_submit():
      cliente = Cliente.get(id)
      dispositivo = form.dispositivo.data
      fecha = form.fecha.data
      cita = Cita(idCliente=cliente.idCliente, dispositivo=dispositivo, fecha=fecha)
      cita.save()
      return redirect(url_for('reparaciones.citas', id=id))
    return render_template('reparaciones/citas.html', form=form)
