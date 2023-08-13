from .db import get_connection

mydb = get_connection()

class Audio :
    
    def __init__(self, marca, modelo, conexion,tipo,stock, precio,image, id=None):
        self.marca = marca
        self.modelo = modelo
        self.conexion = conexion
        self.tipo = tipo
        self.stock = stock
        self.precio = precio
        self.image = image
        self.id = id



    def save(self):
        # Create a New Object in DB
        if self.id is None:
            with mydb.cursor() as cursor:
               
                sql = "INSERT INTO audio(marca, modelo, conexion, tipo, stock, precio, image) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                val = (self.marca, self.modelo, self.conexion, self.tipo, self.stock, self.precio, self.image)
                cursor.execute(sql, val)
                mydb.commit()
                self.id = cursor.lastrowid
                return self.id
        else:
            with mydb.cursor() as cursor:
                sql = 'UPDATE audio SET marca = %s, modelo = %s, conexion =%s, tipo = %s, stock = %s, precio = %s, image = %s'
                sql += 'WHERE idAudio = %s'
                val = (self.marca, self.modelo, self.conexion, self.tipo, self.stock, self.precio, self.image, self.id)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id
            
    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM audio WHERE idAudio = { id }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            audio = Audio(result["marca"], result["modelo"], result["conexion"],result["tipo"],result["stock"],  result["precio"], result["image"], id)
            return audio

    @staticmethod
    def get_all(limit=4, page=1):
        offset = limit * page - limit
        audios = []

        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM audio LIMIT {limit} OFFSET {offset}"
            cursor.execute(sql)
            result = cursor.fetchall()
            for aud in result:
                audios.append(Audio(aud["marca"], aud["modelo"], aud["conexion"], aud["tipo"], aud["stock"],aud["precio"], aud["image"], aud["idAudio"]))
            return audios
        
    
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM audio WHERE idAudio = { self.id }"
            cursor.execute(sql)
            mydb.commit()
            return self.id
        
    @staticmethod
    def count():
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT count(idAudio) as total FROM audio"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['total']
        
      
        
