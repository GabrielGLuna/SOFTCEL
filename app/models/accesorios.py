from .db import get_connection

mydb = get_connection()

class Accesorio:

    def __init__(self, categoria, color,
                 tipo, stock=1 ,especificacionExtra="", precio=0.0,image="",id=None):
        self.categoria = categoria
        self.color = color
        self.tipo = tipo
        self.stock = stock
        self.especificacionExtra = especificacionExtra
        self.precio = precio
        self.image = image
        self.id = id


    def save(self):
        # Create a New Object in DB
        if self.id is None:
            with mydb.cursor() as cursor:
               
                sql = "INSERT INTO accesorios(categoria, color, tipo, stock, especificacionExtra, precio, image) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                val = (self.categoria, self.color, self.tipo, self.stock, self.especificacionExtra, self.precio, self.image, self.id)
                cursor.execute(sql, val)
                mydb.commit()
                self.id = cursor.lastrowid
                return self.id
        else:
            with mydb.cursor() as cursor:
                sql = 'UPDATE accesorios SET categoria = %s, color = %s, tipo =%s, stock = %s, especificacionExtra = %s, precio = %s, image = %s'
                sql += 'WHERE idAcc = %s'
                val = (self.categoria, self.color, self.tipo, self.stock, self.especificacionExtra, self.precio, self.image, self.id)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id
            
    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM accesorios WHERE idAcc = { id }"
            cursor.execute(sql)
            acc = cursor.fetchone()
            if acc:
               acc = Accesorio(categoria=acc["categoria"],
                                  color=acc["color"],
                                  tipo=acc["tipo"],
                                  stock=acc["stock"],
                                  especificacionExtra=acc["especificacionExtra"],
                                  precio=acc["precio"],
                                  image=acc["image"],
                                  id=acc["idAcc"])
            return acc 
        

    @staticmethod
    def get_all_art(limit=4, page=1):
        offset = limit * page - limit
        accesorios = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT *  FROM accesorios LIMIT { limit } OFFSET { offset }"
            cursor.execute(sql)
            result = cursor.fetchall()
            for accesorio in result:
                accesorios.append(Accesorio(categoria=accesorio["categoria"],
                                  color=accesorio["color"],
                                  tipo=accesorio["tipo"],
                                  stock=accesorio["stock"],
                                  especificacionExtra=accesorio["especificacionExtra"],
                                  precio=accesorio["precio"],
                                  image=accesorio["image"],
                                  id=accesorio["idAcc"]))
            return accesorios
        
    @staticmethod
    def get_all(limit=10, page=1):
        offset = limit * page - limit
        accesorios = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT *  FROM accesorios LIMIT { limit } OFFSET { offset }"
            cursor.execute(sql)
            result = cursor.fetchall()
            for accesorio in result:
                accesorios.append(Accesorio(categoria=accesorio["categoria"],
                                  color=accesorio["color"],
                                  tipo=accesorio["tipo"],
                                  stock=accesorio["stock"],
                                  especificacionExtra=accesorio["especificacionExtra"],
                                  precio=accesorio["precio"],
                                  image=accesorio["image"],
                                  id=accesorio["idAcc"]))
            return accesorios
        
           
    @staticmethod
    def get_by_any(precio):
        accesorios = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT *FROM accesorios WHERE precio LIKE { precio }"
            cursor.execute(sql)
            result = cursor.fetchall()
            for accesorio in result:
                accesorios.append(Accesorio(categoria=accesorio["categoria"],
                                  color=accesorio["color"],
                                  tipo=accesorio["tipo"],
                                  stock=accesorio["stock"],
                                  especificacionExtra=accesorio["especificacionExtra"],
                                  precio=accesorio["precio"],
                                  image=accesorio["image"],
                                  id=accesorio["idAcc"]))
            return accesorios
        
    
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM accesorios WHERE idAcc = { self.id }"
            cursor.execute(sql)
            mydb.commit()
            return self.id
        

    

        