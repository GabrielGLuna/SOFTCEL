from flask import Flask, render_template, session, request, url_for, redirect, flash

from flask_mysqldb import MySQL,MySQLdb
import pymysql
from models.usuarios import Usuario

from views.home_views import home_views
from views.articulos_views import articulos_views
from views.celulares_views import celulares_views
from views.soporte_views import soporte_views
from views.reparaciones_views import reparaciones_views
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'
app.secret_key = 'ismontana'  # Cambia esto por una clave secreta real
db = pymysql.connect(host='localhost', user='root', password='', db='softcell')

app.register_blueprint(home_views)
app.register_blueprint(articulos_views)
app.register_blueprint(celulares_views)
app.register_blueprint(soporte_views)
app.register_blueprint(reparaciones_views)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']  # Cambio aquí
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s AND password = %s", (correo, password))  # Cambio aquí
        user = cursor.fetchone()
        cursor.close()
        if user:
            session['id_rol'] = user[4]
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'id_rol' in session:
        id_rol = session['id_rol']
        if id_rol == 1:
            return render_template('admin.html')
        elif id_rol == 2:
            return render_template('cajero.html')
        elif id_rol == 3:
            return render_template('home/home_cliente.html')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('id_rol', None)
    return redirect(url_for('home.home_user'))

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        password = request.form['password'] 
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (nombre, correo, password, id_rol) VALUES (%s, %s, %s, %s)",
                           (nombre, correo, password, 3)) 
            db.commit()
            flash('Registrado correctamente!', 'success')
            return redirect(url_for('login'))
        except pymysql.IntegrityError:
            db.rollback()
            flash('El correo ya está registrado', 'error')
        cursor.close()
    return render_template('registro.html')


if __name__ == '__main__':
    app.run(debug=True)