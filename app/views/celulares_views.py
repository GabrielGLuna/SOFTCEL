from flask import Blueprint, render_template, redirect, url_for, abort
from models.celulares import Celular
import traceback

from forms.celulares_form import CreateCelularForm, UpdateCelularForm

from utils.file_handler import save_image

celulares_views = Blueprint('celulares',__name__)

@celulares_views.route("/celulares/<int:page>")
def celulares(page=1):
    limit = 8

    cels = Celular.get_all(limit=limit, page=page)
    total_cels = Celular.count()
    pages = total_cels // (total_cels//3)
    return render_template('/celulares/celulares.html', pages=pages, cels=cels)

@celulares_views.route("/celulares_cli/<int:page>")
def celulares_cli(page=1):
    limit = 8

    cels = Celular.get_all(limit=limit, page=page)
    total_cels = Celular.count()
    pages = total_cels // (total_cels//3)  
    
    return render_template('/celulares/celulares_cli.html', cels=cels, pages=pages)

@celulares_views.route("/admin/celulares_list/")
def celulares_list(page=1):
    limit =8
    cels = Celular.get_all(limit=limit, page=page)
    total_cels = Celular.count()
    pages = total_cels // (total_cels//3)
    return render_template('/celulares/celulares_list.html', pages=pages, cels=cels)


@celulares_views.route('/celulares/<int:id>/celular/')
def celular(id):
    celular = Celular.get(id)
    if celular is None: abort(404)
    return render_template('celulares/celular.html', celular=celular)

@celulares_views.route('/celulares/<int:id>/celular_cli/')
def celular_cli(id):
    celular = Celular.get(id)
    if celular is None: abort(404)
    return render_template('celulares/celular_cli.html', celular=celular)



@celulares_views.route("/celulares/insertarcelular/", methods=['GET', 'POST'])
def insert_celular():
    form = CreateCelularForm()

    if form.validate_on_submit():
        marca = form.marca.data
        modelo = form.modelo.data
        color = form.color.data 
        stock = form.stock.data
        almacenamiento = form.almacenamiento.data
        condicion = form.condicion.data
        idProveedor = form.idProveedor.data
        precio = form.precio.data
        f = form.image.data
        image = ""
        if f:
            image = save_image(f, 'images/Celulares')
        celular = Celular(marca=marca,
                            modelo=modelo,
                            color=color,
                            stock=stock,
                            almacenamiento=almacenamiento,
                            condicion=condicion,
                            idProveedor=idProveedor,
                            precio=precio,
                            image=image)
        celular.save()
      

        return redirect(url_for('celulares.celulares_list'))

    return render_template('celulares/insertar_cel.html', form=form)

@celulares_views.route('/celulares/<int:id>/updatecel', methods=('GET', 'POST'))
def updatecel(id):
    form = UpdateCelularForm()
    cel = Celular.get(id)
    if cel is None:
        abort(404)
    if form.validate_on_submit():
        cel.modelo=form.marca.data
        cel.color=form.modelo.data
        cel.stock=form.stock.data
        cel.almacenamiento=form.almacenamiento.data
        cel.condicion=form.condicion.data
        cel.idProveedor=form.idProveedor.data
        cel.precio=form.precio.data
        f = form.image.data
        if f:
            image = save_image(f, 'images/Celulares')
            cel.image = image
        cel.save()
        return redirect(url_for('celulares.celulares_list'))
    form.marca.data = cel.marca
    form.modelo.data = cel.modelo
    form.color.data = cel.color
    form.stock.data = cel.stock
    form.almacenamiento.data = cel.almacenamiento
    form.condicion.data = cel.condicion
    form.idProveedor.data = cel.idProveedor
    form.precio.data = cel.precio
    image = cel.image
    return render_template('celulares/insertar_cel.html', form=form, image=image)

@celulares_views.route('/celulares/<int:id>/deletecel/', methods=['POST'])
def deletecel(id):
    Celular.delete_celular(id)

    return redirect(url_for('celulares.celulares_list'))