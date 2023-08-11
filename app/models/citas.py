from .db import get_connection

mydb = get_connection()
class Cita:
    def __init__(self,email_cliente, dispositivo, fecha, id=None):
        self.email_cliente = email_cliente
        self.dispositivo = dispositivo
        self.fecha = fecha
        self.id = id

    def save(self):
        # Create a New Object in DB
        if self.id is None:
            with mydb.cursor() as cursor:
               
                sql = "INSERT INTO citas(email_cliente, dispositivo, fecha) VALUES(%s, %s, %s)"
                val = (self.email_cliente, self.dispositivo, self.fecha)
                cursor.execute(sql, val)
                mydb.commit()
                self.id = cursor.lastrowid
                return self.id
        else:
            with mydb.cursor() as cursor:
                sql = 'UPDATE citas SET email_cliente = %s, dispositivo = %s, fecha = %s'
                sql += 'WHERE idcita = %s'
                val = (self.email_cliente, self.dispositivo, self.fecha, self.id)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id
       