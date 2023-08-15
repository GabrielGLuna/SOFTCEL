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
            
    @staticmethod
    def get_all(limit=8,  page=1):
        offset = limit * page - limit
        citas = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM citas LIMIT { limit } OFFSET { offset }"
            cursor.execute(sql)
            result = cursor.fetchall()
            for cita in result:
                citas.append(Cita( email_cliente=cita["marca"],
                                  dispositivo=cita["modelo"],
                                  fecha=cita["color"],
                                  id=cita["id_cita"],
                                  ))
            return citas
        
    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM citas WHERE idcita = { id }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            cita = Cita(result["email_cliente"], result["dispositivo"], result["fecha"],id)
            return cita
        
    @staticmethod
    def count():
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT count(idcita) as total FROM citas"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['total']
       
    @staticmethod
    def eliminar_cita(id):
        with mydb.cursor() as cursor:
            sql = "DELETE FROM citas WHERE idcita = %s"
            cursor.execute(sql, (id,))
            mydb.commit()



    