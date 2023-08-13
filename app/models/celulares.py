from .db import get_connection

mydb = get_connection()

class Celular:

    def __init__(self, marca, modelo, color, stock, almacenamiento,condicion, idProveedor,precio,image, id=None ):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.stock = stock
        self.almacenamiento = almacenamiento
        self.condicion = condicion
        self.idProveedor = idProveedor
        self.precio = precio
        self.image = image
        self.id = id

    def save(self):
        # Create a New Object in DB
        if self.id is None:
            with mydb.cursor() as cursor:
               
                sql = "INSERT INTO celulares(marca, modelo, color, stock, almacenamiento, condicion,idProveedor,precio, image) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (self.marca, self.modelo, self.color, self.stock, self.almacenamiento, self.condicion, self.idProveedor,self.precio ,self.image)
                cursor.execute(sql, val)
                mydb.commit()
                self.id = cursor.lastrowid
                return self.id
        else:
            with mydb.cursor() as cursor:
                sql = 'UPDATE celulares SET marca = %s, modelo = %s, color =%s, stock = %s, almacenamiento = %s, condicion = %s, idProveedor= %s, precio=%s, image=%s'
                sql += 'WHERE idCel = %s'
                val = (self.marca, self.modelo, self.color, self.stock, self.almacenamiento, self.condicion, self.idProveedor,self.precio ,self.image )
                cursor.execute(sql, val)
                mydb.commit()
                return self.id
            
    
    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM celulares WHERE idCel = { id }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            celular = Celular(result["marca"], result["modelo"], result["color"],result["stock"],result["almacenamiento"], result["condicion"],  result["idProveedor"],result["precio"],result["image"], id)
            return celular
        
    @staticmethod
    def get_all(limit=8, page=1):
        offset = limit * page - limit
        celulares = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM celulares LIMIT { limit } OFFSET { offset }"
            cursor.execute(sql)
            result = cursor.fetchall()
            for celular in result:
                celulares.append(Celular( marca=celular["marca"],
                                  modelo=celular["modelo"],
                                  color=celular["color"],
                                  stock=celular["stock"],
                                  almacenamiento=celular["almacenamiento"],
                                  condicion=celular["condicion"],
                                  idProveedor=celular["idProveedor"],
                                  precio=celular["precio"],
                                  image=celular["image"],
                                  id=celular["idCel"]))
            return celulares

    @staticmethod
    def count():
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT count(idCel) as total FROM celulares"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['total']
