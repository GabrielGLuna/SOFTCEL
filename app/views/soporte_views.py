from flask import Blueprint, render_template, redirect, url_for, abort
soporte_views = Blueprint('soporte',__name__)

from models.soporte import Soporte

from forms.soporte_form import CreateQuejaForm


@soporte_views.route("/soporte/", methods = ('GET','POST'))
def soporte():
    form = CreateQuejaForm()

    if form.validate_on_submit():
      email = form.email.data
      telefono = form.telefono.data
      queja = form.queja.data
      sop = Soporte(email, telefono, queja)
      sop.save()
      return redirect(url_for('soporte.soporte'))
    return render_template('soporte/soporte.html', form=form)
