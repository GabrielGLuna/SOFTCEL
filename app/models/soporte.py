from .db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash
mydb = get_connection()

class Soporte:

    def __init__(self, email_sop, tel_sop, queja_sop, id=None) :
          self.email_sop = email_sop
          self.tel_sop = tel_sop
          self.queja_sop = queja_sop
          self.id= id

    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT email_sop, tel_sop, queja_sop FROM celulares WHERE id_sop = { id }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            soporte = Soporte(result["email_sop"], result["tel_sop"], result["queja_sop"], id)
            return soporte
        
    def save(self):
        # Create a New Object in DB
        if self.id is None:
            with mydb.cursor() as cursor:
               
                sql = "INSERT INTO soporte(email_sop, tel_sop, queja_sop) VALUES(%s, %s, %s,)"
                val = (self.email_sop, self.tel_sop, self.queja_sop)
                cursor.execute(sql, val)
                mydb.commit()
                self.id = cursor.lastrowid
                return self.id
        else:
            with mydb.cursor() as cursor:
                sql = 'UPDATE soporte SET email_sop = %s, tel_sop = %s, queja_sop = %s'
                sql += 'WHERE id_sop = %s'
                val = (self.email_sop, self.tel_sop, self.queja_sop, self.id)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id
            