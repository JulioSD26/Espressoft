"""
Controlador que podria reutilizarse para las graficas de todas las ventanas de ventas
"""

import random
import pyqtgraph as pg
from PyQt5 import QtGui, QtWidgets

# esta funcion deberia ser eliminada cuando ya no se requiera probar con ella, en la segunda iteracion
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

    # agrega un label en el eje y
    grafica.getAxis("left").setLabel(text="Total ($)")

    # con esto se puede cambiar la fuente del titulo de la grafica
    grafica.getPlotItem().titleLabel.item.setFont(font)

    # con esto se puede mostrar/ocultar las lineas que son paralelas a cada uno de los ejes.
    # en este caso solo se muestran las del eje y, para que se parezca al disenio
    #desactiva movimientos del mouse.
    #grafica.setMouseEnabled(x=True, y=True)
    #grafica.getPlotItem().getViewBox().setMouseMode(grafica.getPlotItem().getViewBox().RectMode)
    grafica.setMenuEnabled(False)
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


def dibujar_grafica(grafica, diccionario_datos: dict):
    """
    Recibe un diccionario, donde sus llaves son los valores del eje x, que pueden ser
    intervalos de horas como 03:00 PM - 04:00 PM, meses como Enero o anios como el 2022,
    sus valores correspodientes son los valores del eje y, los cuales son sus correspondientes totales.
    Dibuja una grafica con estos datos
    """
    # cada que se va  a dibujar la grafica se borra la anterior, para que no aparezca junto a la nueva
    limpiar_grafica(grafica)
    
    
    pen = pg.mkPen({'color': "#8cb2e2", 'width': 3})
    # valores_eje_x son los labels de tipo texto que se van a poner en el eje x
    # en este caso las llaves del diccionario de datos
    valores_eje_x = list(diccionario_datos.keys())
    valores_eje_x_tipo_str = []
    # todos los valores del eje x se pasan a str, por si eran numericos
    for valor in valores_eje_x:
        valores_eje_x_tipo_str.append(str(valor))
    # los valores del eje y son los valores del diccionario de datos
    valores_eje_y = list(diccionario_datos.values())

    # esto es para checar si solo se esta tratando de graficar un punto, en una situacion muy rara
    # en la que al obtener los datos de ventas, se haya obtenido solo 1 elemento, 
    # por ejemplo en ventas individuales diarias si se da al boton generar con los datos:
    # fecha = "2022-12-31" 
    # empleado_id = "11"
    # de la base de datos solo se obtiene un registro
    # y cuando se trata de graficar un solo punto, el programa lo grafica pero truena, porque espera
    # graficar una linea que por lo menos tenga 2 puntos.
    # para este punto ya esta validado que si no se obtuvo un registro de la base de datos, 
    # no se genere la grafica ni se actualicen los datos de la ventana, mostrandole un mensaje al usuario,
    # sin embargo queda este caso donde solo se obtiene un registro
    if len(valores_eje_x_tipo_str) == 1:
        # la mejor forma de momento para que el programa no truene y no se vea tan feo, es agregar otro punto
        # despues, con una etiqueta de No conocido y con el mismo valor en y que ese punto
        valores_eje_x_tipo_str.append("No conocido")
        # por correspondencia las listas de valores_eje_x_tipo_str y valores_eje_y tienen que tener la misma longitud,
        # por lo que si solo hay un elemento, entonces valores_eje_y[0] es el total de ese elemento
        valores_eje_y.append(valores_eje_y[0])

    asignar_valores_de_tipo_string_eje_x(grafica, valores_eje_x_tipo_str)
    # estos van a ser los valores en el eje x, pero los labels de arriba (valores_eje_x_tipo_str) los van a representar
    # esto es asi porque no se puede poner un valor en uno de los ejes que no sea numerico
    valores_x_numericos = [i for i in range(1, len(valores_eje_x_tipo_str) + 1)]

    # esto es para poner los limites de la grafica
    # xMin = 0 es para que no se muestren los valores de x negativos, el eje x solo puede tener valores numericos (aunque luego sean reemplazados por labels, siguen siendo representados por numeros)
    # yMin = -1 es para que no se muestren los valores de y negativos, de modo que no permite verlos ya que ninguna venta podria tener valores negativos
    # xMax = len(valores_eje_x_tipo_str) + 1 es para que el limite en el eje x sea de la cantidad de valores en el eje x + 1, es mas 1 para que no se meustre recortado el ultimo elemento, de modo que si hay 5 valores en el eje x (en el eje y correspondientemente deben haber 5 tambien), el limite ser hasta el elemento 6
    # yMax = max(valores_eje_y) + (sum(valores_eje_y) / len(valores_eje_y) es para poner el limite maximo en el eje y,
    # para esto se obtiene el maximo entre los valores del eje y (totales) y para que no se muestre recortado el ultimo elemento,
    # se le suma el promedio de los valores en el eje y, porque estos valores pueden variar mucho
    grafica.getPlotItem().vb.setLimits(xMin = 0, yMin= -1, xMax = len(valores_eje_x) + 1, yMax = max(valores_eje_y) + (sum(valores_eje_y) / len(valores_eje_y)))
    # symbol representa un simbolo que se puede poner en cada punto x, y, en este caso se le pone uno con forma de 'o', tamanio = 10, de color blanco y cubiero por el color '#658fc2' 
    #grafica.plot(valores_x_numericos, valores_eje_y, pen = pen, symbolBrush = 'white', symbolPen ='#658fc2', symbol ='o', symbolSize = 10)     
    
    grafica.plot(valores_x_numericos, valores_eje_y, pen = pen, symbolBrush = 'white', symbolPen ='#658fc2', symbol ='o', symbolSize = 10)

def limpiar_grafica(grafica):
    """
    Limpia una grafica dada de sus elementos.
    """
    grafica.getPlotItem().clear()
    