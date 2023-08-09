from .db import get_connection

mydb = get_connection()
class Cita:
    def __init__(self, idCliente, dispositivo, fecha, id=None):
        self.dispositivo = dispositivo
        self.fecha = fecha
        self.idCliente = idCliente
        self.id = id

    def save(self):
        # Create a New Object in DB
        if self.id is None:
            with mydb.cursor() as cursor:
               
                sql = "INSERT INTO citas(idCliente, dispositivo, fecha) VALUES(%s, %s, %s)"
                val = (self.idCliente, self.dispositivo, self.fecha)
                cursor.execute(sql, val)
                mydb.commit()
                self.id = cursor.lastrowid
                return self.id
        else:
            with mydb.cursor() as cursor:
                sql = 'UPDATE citas SET idCliente = %s, dispositivo = %s, fecha = %s'
                sql += 'WHERE idcita = %s'
                val = (self.idCliente, self.dispositivo, self.fecha, self.id)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id
       