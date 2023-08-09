from flask import Blueprint, render_template, redirect, url_for, abort

articulos_views = Blueprint('articulos',__name__)

from models.accesorios import Accesorio
from models.audio import Audio
from forms.accesorios_form import CreateAccesorioForm, FiltroBusqueda, UpdateAccesorioForm
from forms.audio_form import CreateAudioForm, UpdateAudioForm

from utils.file_handler import save_image
@articulos_views.route("/articulos")
def articulos():
    accs = Accesorio.get_all_art()
    
    auds = Audio.get_all()
    return render_template('articulos/articulos.html',accs=accs, auds = auds)

@articulos_views.route("/accesorios")
def accesorios():
    accs = Accesorio.get_all()
    
    return render_template('articulos/accesorios.html',accs=accs)

@articulos_views.route("/audios")
def audios():
    auds = Audio.get_all()
    
    return render_template('articulos/audios.html',auds=auds)

@articulos_views.route("/articulos/crear_accesorio")
def crear_accesorio():
    form = CreateAccesorioForm()
    accesorios = Accesorio.get_all()
    accs = [(-1, '')]
    for acc in accesorios:
        accs.append((acc.id))
    form.idAcc.choices = accs

    if form.validate_on_submit():
        categoria = form.categoria.data
        tipo = form.tipo.data
        stock = form.stock.data
        color = form.color.data
        especificacionExtra = form.especificacionExtra.data
        precio = form.precio.data
        f = form.image.data
        image = ""
        if f:
            image = save_image(f, 'images/Accesorios')
        accesorio = Accesorio(categoria=categoria, 
                          tipo=tipo,
                          stock=stock,
                          color=color,
                          especificacionExtra=especificacionExtra,
                          precio=precio,
                          image=image)
        accesorio.save()
        return redirect(url_for('home.home'))

    return render_template('articulos/insertar_acce.html', form=form)

@articulos_views.route('/articulos/<int:id>/accesorio/')
def accesorio(id):
    accesorio = Accesorio.get(id)
    if accesorio is None: abort(404)
    return render_template('articulos/accesorio.html', accesorio=accesorio)

@articulos_views.route('/articulos/<int:id>/audio/')
def audio(id):
    audio = Audio.get(id)
    if audio is None: abort(404)
    return render_template('articulos/audio.html', audio=audio)

@articulos_views.route('/product/<int:id>/delete_acc/', methods=['POST'])
def delete_acc(id):
    accesorio = Accesorio.get(id)
    if accesorio is None: abort(404)
    accesorio.delete()
    return redirect(url_for('articulos.articulos'))

@articulos_views.route('/product/<int:id>/delete_aud/', methods=['POST'])
def delete_aud(id):
    audio = Audio.get(id)
    if audio is None: abort(404)
    audio.delete()
    return redirect(url_for('articulos.articulos'))

@articulos_views.route('/products/<int:id>/update_acc/', methods=('GET', 'POST'))
def update_acc(id):
    form = UpdateAccesorioForm()
    accesorio = Accesorio.get(id)
    if accesorio is None:
        abort(404)
    if form.validate_on_submit():
        accesorio.categoria = form.categoria.data
        accesorio.tipo = form.tipo.data
        accesorio.stock = form.stock.data
        accesorio.color = form.color.data
        accesorio.precio = form.precio.data
        accesorio.especificacionExtra = form.especificacionExtra.data
        f = form.image.data
        if f:
            image = save_image(f, 'images/Accesorios')
            accesorio.image = image
        accesorio.save()
        return redirect(url_for('articulos.articulos'))
    form.categoria.data = accesorio.categoria
    form.tipo.data = accesorio.tipo
    form.stock.data = accesorio.stock
    form.color.data = accesorio.color
    form.precio.data = accesorio.precio
    form.especificacionExtra.data = accesorio.especificacionExtra
    image = accesorio.image
    return render_template('articulos/insertar_acc.html', form=form, image=image)

@articulos_views.route('/products/<int:id>/update_audio/', methods=('GET', 'POST'))
def update_audio(id):
    form = UpdateAudioForm()
    audio = Audio.get(id)
    if audio is None:
        abort(404)
    if form.validate_on_submit():
        audio.marca = form.marca.data
        audio.modelo = form.modelo.data
        audio.tipo = form.tipo.data
        audio.conexion = form.conexion.data
        audio.stock = form.stock.data
        audio.precio = form.precio.data
   
        f = form.image.data
        if f:
            image = save_image(f, 'images/Audio')
            audio.image = image
        audio.save()
        return redirect(url_for('articulos.articulos'))
    form.marca.data = audio.marca
    form.modelo.data= audio.modelo
    form.tipo.data = audio.tipo
    form.conexion.data = audio.conexion
    form.stock.data = audio.stock
    form.precio.data = audio.precio
    image = audio.image
   
    
    return render_template('articulos/insertar_audio.html', form=form, image=image)