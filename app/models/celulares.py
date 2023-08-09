from .db import get_connection

mydb = get_connection()

class Celular:

    def __init__(self, marca, modelo, color, stock, almacenamiento,condicion, idProveedor,precio, idCel=None ):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.stock = stock
        self.almacenamiento = almacenamiento
        self.condicion = condicion
        self.idProveedor = idProveedor
        self.precio = precio
        self.idCel = id

    
    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT marca, modelo, color, stock, almacenamiento,condicion, idProveedor, precio FROM celulares WHERE idCel = { id }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            celular = Celular(result["marca"], result["modelo"], result["color"],result["stock"],result["almacenamiento"], result["condicion"],  result["idProveedor"],result["precio"], id)
            return celular
        
    @staticmethod
    def get_all():
        celulares = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM celulares"
            cursor.execute(sql)
            result = cursor.fetchall()
            for cel in result:
                celulares.append(Celular(cel["marca"], cel["modelo"], cel["color"], cel["stock"],cel["almacenamiento"], cel["condicion"], cel["idProveedor"], cel["precio"]))
            return celulares
  