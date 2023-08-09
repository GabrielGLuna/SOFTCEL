from flask import Blueprint, render_template
from models.celulares import Celular

celulares_views = Blueprint('celulares',__name__)

@celulares_views.route("/celulares/")
def celulares():
    cels = Celular.get_all()
    return render_template('/celulares/celulares.html', cels=cels)