from .db import get_connection

mydb = get_connection()

class Rep:

    def __init__(self, nombre,caracteristicas, costo, fecha_entrada,fecha_entrega, cliente, folio, estatus,comentarios, repimage= "", id_reparacion = None): 
        self.nombre= nombre
        self.id_reparacion= id_reparacion
        self.caracteristicas= caracteristicas 
        self.costo= costo 
        self.fecha_entrada=fecha_entrada
        self.fecha_entrega=fecha_entrega
        self.cliente= cliente
        self.folio=folio
        self.estatus=estatus
        self.comentarios= comentarios
        self.repimage=repimage

    @staticmethod
    def get_all ():
        
        reparaciones = []
        with mydb.cursor(dictionary=True) as cursor: 
            sql = f"select * from reparacion"
            cursor.execute(sql)
            result = cursor.fetchall()
            for reparacion in result:
                reparacion_obj = Rep(
                    nombre=reparacion["nombre"],
                    caracteristicas=reparacion["daño"],
                    costo=reparacion["costo"],
                    fecha_entrada=reparacion["fecha_entrada"],
                    fecha_entrega=reparacion["fecha_entrega"],
                    cliente=reparacion["cliente"],
                    folio=reparacion["folio"],
                    estatus=reparacion["estatus"],
                    comentarios=reparacion["comentarios"],
                    repimage=reparacion["repimage"],
                    id_reparacion=reparacion["id_reparacion"]
                )
                reparaciones.append(reparacion_obj)
                                    
        return reparaciones
        return None
    
    @staticmethod
    def add_reparacion(nombre, caracteristicas, costo,fecha_entrada, fecha_entrega, cliente, folio, estatus, comentarios, repimage):
        with mydb.cursor() as cursor:
            sql = "INSERT INTO reparacion (nombre, caracteristicas, costo,fecha_entrada, fecha_entrega, cliente, folio, estatus, comentarios, repimage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (nombre, caracteristicas, costo, fecha_entrada.strftime('%Y-%m-%d'), fecha_entrega.strftime('%Y-%m-%d'), cliente, folio, estatus, comentarios, repimage))
            mydb.commit()

    @staticmethod
    def obtener_reparacion_por_id(id_reparacion):
            with mydb.cursor(dictionary=True) as cursor:
                sql = "SELECT * FROM reparacion WHERE id_reparacion = %s"
                cursor.execute(sql, (id_reparacion,))
                reparacion = cursor.fetchone()
                if reparacion:
                    return Rep(
                        nombre=reparacion["nombre"],
                        caracteristicas=reparacion["caracteristicas"],
                        costo=reparacion["costo"],
                        fecha_entrada=reparacion["fecha_entrada"],
                        fecha_entrega=reparacion["fecha_entrega"],
                        cliente=reparacion["cliente"],
                        folio=reparacion["folio"],
                        estatus=reparacion["estatus"],
                        comentarios=reparacion["comentarios"],
                        repimage=reparacion["repimage"],
                        id_reparacion=reparacion["id_reparacion"]
                    )
                return None

    @staticmethod
    def actualizar_reparacion(id_reparacion,nombre, caracteristicas, costo,fecha_entrada, fecha_entrega, cliente, folio, estatus, comentarios, repimage):
        with mydb.cursor() as cursor:
            sql = "UPDATE reparacion SET nombre=%s, caracteristicas=%s, costo=%s,fecha_entrada=%s, fecha_entrega=%s, cliente=%s, folio=%s, estatus=%s, comentarios=%s, repimage=%s WHERE id_reparacion=%s"
            cursor.execute(sql, (nombre, caracteristicas, costo,fecha_entrada, fecha_entrega, cliente, folio, estatus, comentarios, repimage, id_reparacion))
            mydb.commit()


    @staticmethod
    def eliminar_reparacion(id_reparacion):
        with mydb.cursor() as cursor:
            sql = "DELETE FROM reparacion WHERE id_reparacion = %s"
            cursor.execute(sql, (id_reparacion,))
            mydb.commit()



    