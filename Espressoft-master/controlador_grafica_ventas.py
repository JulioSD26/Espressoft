"""
Este archivo es un borrador de lo que podria ser un controlador para las graficas de ventas.
De momento esta solo para probar.
"""


import random
import pyqtgraph as pg
from PyQt5 import QtGui

def generar_datos_aleatorios_para_probar(valores_eje_x: list):
    y = []
    for i in range(0, len(valores_eje_x)):
        y.append(random.randint(7000, 25000))
    return y


def estilizar_grafica(grafica, titulo: str):
    """
    Estiliza a la grafica, cambiando su color de fondo, titulo, fuentes de letra, entre otras cosas.
    """
    grafica.setBackground('#FFFFFF')
    grafica.setTitle(titulo, color="#344055", size="10pt")
    # esto es para que se muestren de entrada 2 valores en el eje x, en este caso los primeros 2, 
    # sin embargo los demas valores se pueden visualizar al desplazarse por el grafico arrastrando con el mouse.
    # es una solucion temporal porque los labels del eje x, por ejemplo los intervalos de horas, se acoplaban,
    # de momento no se ha encontrado otra forma de separarlos
    grafica.setXRange(0, 2)
    
    font= QtGui.QFont('Montserrat', 20)

    # con este "lapiz" se decide como se va a dibujar la grafica, en este caso se le puede dar un color y un ancho
    lapiz_ejes = pg.mkPen({'color': "#BCC7D5", 'width': 2})
    # se obtiene al eje x y se le asigna esa fuente a los labels del eje x
    grafica.getAxis("bottom").tickFont = font
    # se obtiene al eje x y se le asigna como lapiz de dibujado el lapiz_ejes
    grafica.getAxis("bottom").setTextPen(lapiz_ejes)

    # lo mismo de arriba pero para el eje y
    grafica.getAxis("left").tickFont = font
    grafica.getAxis("left").setTextPen(lapiz_ejes)

    # con esto se puede cambiar la fuente del titulo de la grafica
    grafica.getPlotItem().titleLabel.item.setFont(font)

    # con esto se puede mostrar/ocultar las lineas que son paralelas a cada uno de los ejes.
    # en este caso solo se muestran las del eje y, para que se parezca al disenio
    grafica.showGrid(x=False, y=True)


def asignar_valores_de_tipo_string_eje_x(grafica, lista_valores_eje_x):
    """
    A los labels del eje x que solo pueden ser numericos, les asigna valores de tipo string como una tupla.
    """
    # con esto se genera una lista de tuplas de la forma [(0, "valor_eje_x_1"), (1, "valor_eje_x_2"), ...]
    # esto es asi porque no se pueden poner valores al eje x que no sean numericos en un principio, de esta manera
    # se puede hacer eso
    # fuente: https://stackoverflow.com/questions/31775468/show-string-values-on-x-axis-in-pyqtgraph
    
    ticks = [list(zip(range(1, len(lista_valores_eje_x) + 1), (lista_valores_eje_x)))]
    x_axis = grafica.getAxis('bottom')
    x_axis.setTicks(ticks)


def dibujar_grafica(grafica, valores_eje_x: list):
    # cada que se va  a dibujar la grafica se borra la anterior, para que no aparezca junto a la nueva
    grafica.getPlotItem().clear()
    pen = pg.mkPen({'color': "#8cb2e2", 'width': 3})
    # valores_eje_x son los labels de tipo texto que se van a poner en el eje x
    asignar_valores_de_tipo_string_eje_x(grafica, valores_eje_x)
    # estos van a ser los valores en el eje x, pero los labels de arriba los van a representar
    # esto es asi porque no se puede poner un valor en uno de los ejes que no sea numerico
    valores_x_numericos = [i for i in range(1, len(valores_eje_x) + 1)]
    valores_eje_y = generar_datos_aleatorios_para_probar(valores_eje_x)
    # symbol representa un simbolo que se puede poner en cada punto x, y, en este caso se le pone uno con forma de 'o', tamanio = 10, de color blanco y cubiero por el color '#658fc2' 
    grafica.plot(valores_x_numericos, valores_eje_y, pen = pen, symbolBrush = 'white', symbolPen ='#658fc2', symbol ='o', symbolSize = 10)

    

