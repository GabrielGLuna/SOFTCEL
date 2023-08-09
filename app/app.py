from flask import Flask

from views.home_views import home_views
from views.articulos_views import articulos_views
from views.celulares_views import celulares_views
from views.soporte_views import soporte_views
from views.reparaciones_views import reparaciones_views
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'

app.register_blueprint(home_views)
app.register_blueprint(articulos_views)
app.register_blueprint(celulares_views)
app.register_blueprint(soporte_views)
app.register_blueprint(reparaciones_views)

if __name__ == '__main__':
    app.run(debug=True)