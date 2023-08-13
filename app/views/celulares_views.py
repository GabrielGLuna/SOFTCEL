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
    pages = total_cels // limit
    return render_template('/celulares/celulares.html', pages=pages, cels=cels)

@celulares_views.route("/celulares_cli/")
def celulares_cli():
    cels = Celular.get_all()
    return render_template('/celulares/celulares_cli.html', cels=cels)

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
    celulares = Celular.get_all()
    cels = [(-1, '')]
    for celular in celulares:
        cels.append((celular.id, celular.marca))
    form.idCel.choices = cels

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
                            image=image
                            
                            )
        celular.save()
        return redirect(url_for('home.home'))

    return render_template('celulares/insertar_cel.html', form=form)