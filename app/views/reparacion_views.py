import os
from flask import Blueprint, render_template, url_for, redirect, request, current_app
from models.reparacion import Rep, mydb
from werkzeug.utils import secure_filename
from forms.add_reparacion import AddReparacionForm
from forms.citas_form import CreateCita
from models.citas import Cita


reparacion_view= Blueprint ('Reparacion', __name__)

@reparacion_view.route('/reparaciones/')
@reparacion_view.route('/reparaciones/<int:page>')
def reparacion(page=1):
    limit = 8
    offset = limit * page - limit  

    reparaciones = []  

    with mydb.cursor(dictionary=True) as cursor:
        sql = f"select * from reparacion LIMIT {limit} OFFSET {offset}"
        cursor.execute(sql)
        result = cursor.fetchall()

        for reparacion in result:
            reparacion_obj = Rep(
                    nombre=reparacion["nombre"],
                    caracteristicas=reparacion["caracteristicas"],
                    costo=reparacion["costo"],
                    fecha_entrada=reparacion["fecha_entrada"],
                    fecha_entrega=reparacion["fecha_entrega"],
                    cliente=reparacion["cliente"],
                    folio=reparacion["folio"],
                    estatus=reparacion["estatus"],
                    comentarios=reparacion["comentarios"],
                    repimage=reparacion["repimage"],
                    id_reparacion=reparacion["id_reparacion"]
            )
            reparaciones.append(reparacion_obj)

    total_cels = len(reparaciones)
    pages = total_cels // (total_cels//3)  
    return render_template('reparacion/reparaciones.html', reparaciones=reparaciones, pages=pages)

@reparacion_view.route('/admin/listareparaciones/')
def reparacion_list():
  

    reparaciones = []  

    with mydb.cursor(dictionary=True) as cursor:
        sql = f"select * from reparacion "
        cursor.execute(sql)
        result = cursor.fetchall()

        for reparacion in result:
            reparacion_obj = Rep(
                    nombre=reparacion["nombre"],
                    caracteristicas=reparacion["caracteristicas"],
                    costo=reparacion["costo"],
                    fecha_entrada=reparacion["fecha_entrada"],
                    fecha_entrega=reparacion["fecha_entrega"],
                    cliente=reparacion["cliente"],
                    folio=reparacion["folio"],
                    estatus=reparacion["estatus"],
                    comentarios=reparacion["comentarios"],
                    repimage=reparacion["repimage"],
                    id_reparacion=reparacion["id_reparacion"]
            )
            reparaciones.append(reparacion_obj)

   
    return render_template('reparacion/reparaciones_list.html', reparaciones=reparaciones)

@reparacion_view.route('/admin/agregar_reparacion/', methods=['GET', 'POST'])
def agregar_reparacion():
    form = AddReparacionForm()

    if form.validate_on_submit():
        repimage_file = request.files['repimage']
        if repimage_file:
            filename = secure_filename(repimage_file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            repimage_file.save(filepath)
        else:
            filename = None

        Rep.add_reparacion(
            nombre=form.nombre.data,
            caracteristicas=form.caracteristicas.data,
            costo=form.costo.data,
            fecha_entrada=form.fecha_entrada.data,  
            fecha_entrega=form.fecha_entrega.data,
            cliente=form.cliente.data,
            folio=form.folio.data,
            estatus=form.estatus.data,
            comentarios=form.comentarios.data,
            repimage=filename
        )
        return redirect(url_for('Reparacion.reparacion_list'))

    return render_template('reparacion/add_reparacion.html', form=form)

@reparacion_view.route('/detalle_reparacion/<int:id_reparacion>', methods=['GET', 'POST'])
def detalle_reparacion(id_reparacion):
    reparacion = Rep.obtener_reparacion_por_id(id_reparacion)
    if not reparacion:
        return render_template('error.html', error_message="Reparación no encontrada")
    return render_template('reparacion/detalle_reparacion.html', reparacion=reparacion)

@reparacion_view.route('/reparacion/admin/editar/<int:id>', methods=['GET', 'POST'])
def editar_reparacion(id):
    reparacion = Rep.obtener_reparacion_por_id(id)
    form = AddReparacionForm(obj=reparacion)

    if form.validate_on_submit():
        repimage_file = form.repimage.data
        if repimage_file:
            filename = secure_filename(repimage_file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            repimage_file.save(filepath)
        else:
            filename = reparacion.repimage  

        Rep.actualizar_reparacion(
            id_reparacion=id,
            nombre=form.nombre.data,
            caracteristicas=form.caracteristicas.data,
            costo=form.costo.data,
            fecha_entrada=form.fecha_entrada.data,  
            fecha_entrega=form.fecha_entrega.data,
            cliente=form.cliente.data,
            folio=form.folio.data,
            estatus=form.estatus.data,
            comentarios=form.comentarios.data,
            repimage=filename
        )

        return redirect(url_for('Reparacion.reparacion_list', id_reparacion=id))

    return render_template('reparacion/editar_reparacion.html', form=form, id=id)


@reparacion_view.route('/reparacion/admin/eliminar/<int:id>')
def eliminar_reparacion(id):
    Rep.eliminar_reparacion(id)
    return redirect(url_for('Reparacion.reparacion_list'))


@reparacion_view.route("/reparaciones/crearcitas/", methods = ('GET','POST'))
def citas():
    form = CreateCita()
    if form.validate_on_submit():
      email_cliente = form.email_cliente.data
      dispositivo = form.dispositivo.data
      fecha = form.fecha.data
      cita = Cita(email_cliente=email_cliente, dispositivo=dispositivo, fecha=fecha)
      cita.save()
      return redirect(url_for('reparaciones.citas'))
    return render_template('reparacion/citas.html', form=form)

@reparacion_view.route('/admin/listacitas/')
def citas_list():
  citas = []  
  with mydb.cursor(dictionary=True) as cursor:
        sql = f"select * from citas "
        cursor.execute(sql)
        result = cursor.fetchall()

        for cita in result:
            cita_obj=Cita(email_cliente=cita["email_cliente"],
                    dispositivo=cita["dispositivo"],
                    fecha=cita["fecha"],
                    id=cita["idcita"]
            )
            citas.append(cita_obj)
  return render_template('reparacion/citas_list.html', citas=citas)

@reparacion_view.route('/cita/admin/eliminar/<int:id>')
def eliminar_cita(id):
    Cita.eliminar_reparacion(id)
    return redirect(url_for('Reparacion.citas_list'))

@reparacion_view.route('/cita/admin/editar/<int:id>', methods=['GET', 'POST'])
def editar_cita(id):
    cita = Cita.get(id)
    form = CreateCita(obj=cita)

    if form.validate_on_submit():
      
        Rep.actualizar_reparacion(
            id_cita=id,
            email_cliente=form.email_cliente.data,
            dispositivo=form.dispositivo.data,
            fecha=form.fecha.data
           
        )

        return redirect(url_for('Reparacion.citas_list', id_cita=id))

    return render_template('reparacion/citas.html', form=form, id=id)
    


                        


 