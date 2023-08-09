from .db import get_connection

mydb = get_connection()
class Usuario:
    def __init__(self, id_rol, nombre, correo, password , id=None):
        self.nombre = nombre
        self.correo = correo
        self.password = password
        self.id_rol = id_rol
        self.id = id

    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM usuarios WHERE id = { id }"
            cursor.execute(sql)
            usuario = cursor.fetchone()
            if usuario:
               usuario = Usuario(nombre=usuario["nombre"],
                                 correo=usuario["correo"],
                                 password=usuario["password"],
                                 id_rol=usuario["id_rol"],
                                 id=usuario["id"])
            return usuario
        