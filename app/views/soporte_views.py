from flask import Blueprint, render_template, redirect, url_for, abort
soporte_views = Blueprint('soporte',__name__)

from models.soporte import Soporte, mydb

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

@soporte_views.route("/liistsoporte/")
def soporte_list():
  quejas = []  
  with mydb.cursor(dictionary=True) as cursor:
        sql = f"SELECT * FROM soporte "
        cursor.execute(sql)
        result = cursor.fetchall()

        for queja in result:
            queja_obj=Soporte(email_sop=queja["email_sop"],
                    tel_sop=queja["tel_sop"],
                    queja_sop=queja["queja_sop"],
                    id=queja["id_sop"]
            )
            quejas.append(queja_obj)
  return render_template('soporte/soporte_list.html', quejas=quejas)

@soporte_views.route('/soporte/admin/eliminar/<int:id>')
def eliminar_queja(id):
    Soporte.eliminar_queja(id)
    return redirect(url_for('soporte.soporte_list'))