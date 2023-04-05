"""
Controlador que podria reutilizarse para las tablas de todas las ventanas de ventas
"""
from PyQt5 import QtGui
from PyQt5.QtWidgets import QTableWidgetItem


def llenar_datos_tabla(tabla, diccionario_datos: dict):
    """
    LLena una tabla dada, con unos datos dados (diccionario_datos)
    """
    # antes de llenarla, se vacia por si tenia filas de una generacion de datos anterior
    limpiar_tabla(tabla)
    # se recorren las llaves del diccionario de datos, que serian los periodos de tiempo, 
    # por ejemplo,
    # pueden ser los intervalos de horas para las ventas diarias (03:00 PM - 04:00 PM, ...)
    # aunque tambien pueden ser los meses de las ventas mensuales o los anios de las ventas anuales
    for periodo_de_tiempo in diccionario_datos.keys():
        # se obtiene el valor del diccionario con esa llave, que seria el total asignado a cada periodo de tiempo
        # por ejemplo si se usara para la ventana de ventas diarias:
        # llave/periodo_de_tiempo = '03:00 PM - 04:00 PM'
        # valor/total_correspondiente = 3560.98
        total_correspondiente = diccionario_datos[periodo_de_tiempo]
        # se va insertando cada fila con esos 2 datos en la tabla
        insertar_fila_en_tabla(tabla, periodo_de_tiempo, total_correspondiente)


def insertar_fila_en_tabla(tabla, periodo_de_tiempo, total_correspondiente):
    """
    Recibe como argumentos una tabla a la que se le va a insertar la fila,
    un periodo de tiempo que podria ser por ejemplo '03:00 PM - 04:00 PM', 'Enero' o '2021', entre otros,
    tambien recibe el total correspondiente a ese periodo de tiempo
    """
    # se obtiene la cantidad de filas de la tabla, que si ya fue limpiada, deberia de ser 0
    cantidad_filas = tabla.rowCount()
    # se suma 1 a la cantidad de filas, por que se va a insertar una
    tabla.setRowCount(cantidad_filas + 1)
    # el periodo de tiempo se transforma a un QTableWidgetItem para poder ser agregado como celda a la tabla
    item_periodo_tiempo = QTableWidgetItem(periodo_de_tiempo)
    # lo mismo para el total, solo que este se transforma a str, porque si no, la tabla no lo muestra, porque parece
    # que solo muestra datos de tipo string, lo raro es que no muestra error
    # tambien se le agrega un $
    item_total = QTableWidgetItem(f"${str(total_correspondiente)}")
    # se crea una fuente para el item/celda
    font = QtGui.QFont()
    font.setFamily("Montserrat")
    font.setBold(True)
    font.setWeight(75)
    # se le asigna esa fuente a ambos items.
    # esto se tiene que hacer para cada item, porque no se puede usar css, ni tampoco se mantiene ese estilo para
    # todos los items
    item_periodo_tiempo.setFont(font)
    item_total.setFont(font)
    # a la tabla se le agregan esas 2 celdas
    # .setItem(fila, columna, item)
    # la primera columna (0) es el periodo de tiempo, mientras que la segunda (1) es su total correspondiente
    tabla.setItem(cantidad_filas, 0, item_periodo_tiempo)
    tabla.setItem(cantidad_filas, 1, item_total)
    

def limpiar_tabla(tabla):
    """
    Vacia la tabla de todas sus filas.
    """
    # simplemente se le asigna a la tabla un contador de filas de 0,
    # pyqt internamente elimina todas las filas si es que la tabla tenia
    tabla.setRowCount(0)


def imprimir_filas_tabla(tabla):
    """
    Imprime los datos de todas las filas de la tabla.
    Solo esta para checar que la tabla se haya llenado bien.
    """
    contador_filas = tabla.rowCount()
    for fila in range(0, contador_filas):
        print((tabla.item(fila, 1)).text())
