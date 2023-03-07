# al principio no hay empleado_loggeado
empleado_loggeado = None

class Empleado():

    # de momento solo interesan el id del empleado y el tipo de empleado, es posible que en el futuro se requieran mas datos del empleado
    def __init__(self, id_empleado, tipo_empleado):
        self.id_empleado = id_empleado
        self.tipo_empleado = tipo_empleado


def asignar_empleado_loggeado(datos_empleado_loggeado: tuple):
    """
    Crea una instancia de la clase Empleado y le asigna los datos que se hayan obtenido del empleado que se
    haya loggeado, se tiene una variable global empleado_loggeado que se utilizara para otros modulos como ventas.py,
    para poner el tipo de usuario en los labels correspondientes
    """
    global empleado_loggeado
    # como es una tupla, se acceden a sus elementos por indices
    empleado_loggeado = Empleado(datos_empleado_loggeado[0], datos_empleado_loggeado[1])


def obtener_usuario_loggeado():
    """
    Regresa al usuario que se encuentre loggeado.
    """
    return empleado_loggeado


