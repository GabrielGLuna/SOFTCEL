from .db import get_connection

mydb = get_connection()
class Cliente:
    def __init__(self, idCliente, nombreUsuario, email, contrasena):
        self.nombreUsuario = nombreUsuario
        self.email = email
        self.contrasena = contrasena
        self.idCliente = idCliente

    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM cliente WHERE idCliente = { id }"
            cursor.execute(sql)
            cliente = cursor.fetchone()
            if cliente:
               cliente = Cliente(nombreUsuario=cliente["nombreUsuario"],
                                 email=cliente["email"],
                                 contrasena=cliente["contrasena"],
                                 idCliente=cliente["idCliente"])
            return cliente
        