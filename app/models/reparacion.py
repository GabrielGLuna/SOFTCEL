from .db import get_connection

from werkzeug.security import generate_password_hash, check_password_hash
mydb = get_connection()
from models.usuarios import Usuario
class Reparacion:

    def __init__(self, nombre, caracteristicas, costo, fecha_entrada, fecha_entrega, idCliente, id ):
     self.nombre = nombre
     self.caracteristicas = caracteristicas
     self.costo = costo
     self.fecha_entrada = fecha_entrada
     self.fecha_entrega = fecha_entrega
     self.idCliente = idCliente
     self.id = id
 
    @staticmethod
    def get(id):
     with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM reparacion WHERE idCliente = { id }"
            cursor.execute(sql)
            reparacion = cursor.fetchone()
            if reparacion:
               reparacion = Reparacion(nombre=reparacion["nombre"],
                                       caracteristicas= reparacion["caracteristicas"],
                                       costo=reparacion["costo"],
                                       fecha_entrada=reparacion["fecha_entrada"],
                                       fecha_entrega=reparacion["fecha_entrega"],
                                       idCliente=reparacion["idCliente"],
                                       id=reparacion["id_reparacion"]
                                       )
            return reparacion
        
    @staticmethod
    def get_all(limit=10, page=1):
        offset = limit * page - limit
        reparaciones = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT *  FROM reparacion LIMIT { limit } OFFSET { offset }"
            cursor.execute(sql)
            result = cursor.fetchall()
            for reparacion in result:
               reparaciones.append(Reparacion(nombre=reparacion["nombre"],
                                       caracteristicas= reparacion["caracteristicas"],
                                       costo=reparacion["costo"],
                                       fecha_entrada=reparacion["fecha_entrada"],
                                       fecha_entrega=reparacion["fecha_entrega"],
                                       idCliente=reparacion["idCliente"],
                                       id=reparacion["id_reparacion"]
                                       ))
            return reparaciones
        