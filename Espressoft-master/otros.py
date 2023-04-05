import time
from datetime import datetime, timedelta

"""
En este modulo van a ver funciones de ayuda que no encajan en alguno de los otros modulos, pero que les sirven.
"""

def formatear_hora_a_formato_12_horas(hora_formato_24_horas):
        """
        Formatea una hora del tipo 11:10:00 (como estan en la base de datos) a una del tipo 11:10 AM, asi 
        como una del tipo 15:28:00 a una del tipo 03:28 PM.
        """
        # primero se pasa a tipo str, porque de la base de datos se obtiene como un objeto del tipo datetime
        hora_str = str(hora_formato_24_horas)
        # ahora se convierte a una estructura de tiempo con la funcion strptime() y el formato hora, minutos y segundos para que pueda ser usada
        # por la funcion strftime()
        hora_tipo_estructura_de_tiempo = time.strptime(hora_str, "%H:%M:%S")
        # finalmente se formatea con %I -> hora con formato de 12 horas, %M -> minutos y %p -> AM o PM
        hora_formateada = time.strftime("%I:%M %p", hora_tipo_estructura_de_tiempo)
        return hora_formateada


def formatear_dia_a_formato_dia_mes_anio(dia: datetime) -> str:
    """
    Formatea un dia al formato dia/mes/anio
    """
    return datetime.strftime(dia, "%d/%m/%Y")


def obtener_hora_siguiente(hora: str) -> str:
      """
      Dada una hora de tipo string, regresa su siguiente hora en formato %I:%M %p de tipo string.
      """
      siguiente_hora = (datetime.strptime(hora, "%I:%M %p") + timedelta(hours=1)).strftime("%I:%M %p")
      return siguiente_hora



def obtener_hora_restados_sus_minutos(hora_formato_12_horas: str) -> str:
    """
    Recibe como parametro una hora con formato de 12 horas y de tipo string, regresa esa
    hora pero con sus minutos restados.
    Por ejemplo si se recibe las 03:36 PM, se regresa las 03:00 PM.
    """
    # la hora en formato string se transforma y formatea a objeto tipo datetime
    hora_objeto_datetime = datetime.strptime(hora_formato_12_horas, "%I:%M %p")
    # se obtienen los minutos de esa hora
    minutos = hora_objeto_datetime.minute
    # a esa hora se le quitan los minutos que tenga,
    # de modo que si la hora es 03:26 PM, entonces se le quiten esos 26 minutos para obtener las 03:00 PM
    hora_minutos_restados = (hora_objeto_datetime - timedelta(minutes=minutos))
    # se formatea la hora obtenida
    hora_minutos_restados_formateada = hora_minutos_restados.strftime("%I:%M %p")
    return hora_minutos_restados_formateada


def crear_intervalo_de_horas(hora) -> str:
    """
    Crea el intervalo de horas de una hora dada.
    Ejemplo:
    Si se recibe la hora 03:26 PM, se regresa el siguiente string -> 03:00 PM - 04:00 PM.
    Si se recibe la hora 11:10 AM, se regresa el siguiente string -> 11:00 AM - 12:00 PM.
    """
    # ambos limites del intervalo son formateados para que se vean como 03:00 PM y 04:00 PM, porque si no se les agrega una fecha al principio que no se requiere y no es correcta
    hora_minutos_restados_formateada = obtener_hora_restados_sus_minutos(hora)
    # se obtiene a la siguiente hora del intervalo (que en el ejemplo anterior seria las 4:00 PM), sumandole una hora a la hora con los minutos ya restados
    siguiente_hora_formateada = obtener_hora_siguiente(hora_minutos_restados_formateada)
    # se regresa como 03:00 PM - 04:00 PM
    return f"{hora_minutos_restados_formateada} - {siguiente_hora_formateada}"



def ordenar_lista_horas(lista_horas):
    """
    Dada una lista de horas que tienen el formato de 12 horas, regresa una lista nueva con las horas ordenadas.
    """
    # gracias stackoverflow
    # https://stackoverflow.com/a/40187578
    formato = '%I:%M %p'
    # primero se transforman las horas a objetos datetime
    lista_horas_estructura_de_tiempo = [time.strptime(t, formato) for t in lista_horas]
    # luego se ordena esa lista con objetos datetime y se formatean
    lista_horas_ordenada = [time.strftime(formato, h) for h in sorted(lista_horas_estructura_de_tiempo)]
    return lista_horas_ordenada



def llenar_horas_vacias_intervalos_de_horas(lista_horas: list) -> list:
    """
    Dada una lista de horas, donde a estas horas ya se les restaron sus minutos, llena esta lista con aquellas horas que no se encuentren entre la primera hora
    y la ultima hora, de modo que regresa una lista ordenada con todas las horas desde la hora inicial hasta la final.
    Por ejemplo si la lista_horas recibida es = ['11:00 AM', '03:00 PM', '05:00 PM', '06:00 PM', '08:00 PM'],
    entonces la lista que se regresa es = ['11:00 AM', '12:00 PM', '01:00 PM', '02:00 PM', '03:00 PM', '04:00 PM', '05:00 PM', '06:00 PM', '07:00 PM', '08:00 PM']
    """
    # primero se quitan aquellas horas que esten repetidas
    lista_horas_sin_repetidos = list(set(lista_horas))
    # se ordena esa lista de horas
    lista_horas_ordenada = ordenar_lista_horas(lista_horas_sin_repetidos)
    # se crea una copia de esa lista para no mutar a la original y evitar problemas abajo cuando se insertan las horas faltantes
    copia_lista_horas_ordenada = lista_horas_ordenada.copy()
    # se inicializa este contador que va a ir contando cuantas horas se han agregado a copia_lista_horas_ordenada
    j = 0
    # se cicla hasta la penultima hora (len(lista_horas_ordenada) - 1), por que para la ultima hora no se necesita checar si tiene una siguiente, porque la ultima es la hora limite o final
    # como ejemplo se va a tomar esta lista ['11:00 AM', '03:00 PM', '05:00 PM', '06:00 PM', '08:00 PM']
    for i in range(0, len(lista_horas_ordenada) - 1):
        # hora_actual pasa a ser '11:00 AM' para la primera iteracion
        hora_actual = lista_horas_ordenada[i]
        # hora_siguiente pasa a ser '03:00 PM' para la primera iteracion
        hora_siguiente = lista_horas_ordenada[i + 1]
        # mientras la hora siguiente a la hora actual ('12:00 PM', para la primera iteracion) no sea igual a la hora siguiente en la lista de horas ordenada ('03:00 PM')
        while obtener_hora_siguiente(hora_actual) != hora_siguiente:
            # hora_actual pasa a ser '12:00 PM' para la primera iteracion del for y el while
            hora_actual = obtener_hora_siguiente(hora_actual)
            # a la copia se le inserta esa hora en la posicion 1 para la primera iteracion del for y el while, de modo
            # que copia_lista_horas_ordenada ahora es = ['11:00 AM', '12:00 PM', '03:00 PM', '05:00 PM', '06:00 PM', '08:00 PM']
            copia_lista_horas_ordenada.insert(j + 1, hora_actual)
            # se aumenta j, para que los siguientes valores que se vayan a insertar sean despues de las horas previamente insertadas
            j += 1
            # esto se repite hasta que obtener_hora_siguiente(hora_actual) == hora_siguiente,
            # de modo que se van agregando todas las horas que hay entre hora_actual y hora_siguiente
        # cuando obtener_hora_siguiente(hora_actual) == hora_siguiente, se sale del while
        # en este ejemplo, la primera vez que se saldria del while seria cuando:
        # obtener_hora_siguiente('02:00 PM') -> '03:00 PM' == hora_siguiente -> '03:00 PM'
        # cuando esto pasa j se incrementa, indicando que ya se llego a hora_siguiente y que la posicion a insertar va a ser despues de ese valor
        j += 1
    return copia_lista_horas_ordenada