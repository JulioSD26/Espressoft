from PyQt5.QtWidgets import QFileDialog, QMessageBox
from pathlib import Path  


class ControladorVentanaImportarDatos():
    """
    Este controlador se va a encargar de darle funcionalidad a la ventana de importar datos.
    """
    
    def __init__(self, ventana_principal):

        # Botones para la funcionalidad de importar datos desde Excel

        ventana_principal.boton_seleccionar_archivo_ventas.clicked.connect(lambda: self.seleccionar_archivo(ventana_principal))

        ventana_principal.boton_subir_archivos.clicked.connect(lambda: self.subir_archivos(ventana_principal))

        ventana_principal.boton_ayuda_archivo_ventas.clicked.connect(lambda: self.mostrar_ayuda(ventana_principal))


    def seleccionar_archivo(self, ventana_principal):
        """
        Evento para el boton de seleccion de archivo de ventas en importar datos, al presionarlos abre una ventana donde pueden seleccionar los archivos de tipo Excel.
        """
        
        nombre_ventana_seleccion_archivo = "Seleccionar archivo de ventas"
        # se instancia un objeto QFileDialog con un metodo estatico de abrir un archivo, 
        # como parametros se le dan el widget padre que en este caso seria MainWindow, luego el nombre que aparece
        # en la ventana de seleccion de archivo, luego la ruta en la que se empieza por defecto (en este caso esta vacia)
        # para que la tome automaticamente, por que si se le pone C:// por ejemplo, podria ser que la aplicacion se use
        # en otro sistema operativo a windows o en algun disco duro que se llame diferente, ...
        ## el tercer parametro es el filtro de los archivos que se pueden seleccionar, en este caso solo los que sean de tipo excel .xlsx
        archivo_seleccionado = QFileDialog.getOpenFileName(ventana_principal, nombre_ventana_seleccion_archivo, "", "Archivos Excel (*.xlsx)")
        # al aceptar o darle en cancelar en la ventana de seleccion de archivo, se obtiene una tupla, si se le dio aceptar con un archivo,
        # se obtiene la ruta absoluta del archivo como primer elemento de la tupla y como segundo elemento se obtiene la extension del archivo, 
        # en este caso "Archivos Excel (*.xlsx)".
        # Si se le dio cancelar y no se se selecciono un archivo, se obtiene una tupla vacia
        print(archivo_seleccionado)
        # se usa la libreria de pathlib y su modulo Path para encargarse de obtener solo el nombre del archivo, para que se muestre como texto
        # en los botones de seleccion de archivo, se usa esta, porque parece que es la que es mas confiable en el sentido, 
        # de que es multiplataforma y sirve para distintos sistemas operativos, por lo que se supone que no habria problema
        # si el sistema corriera en Linux o Windows, donde sus rutas varian mucho como el uso de "//".
        # la libreria os parece que esta mas centrada a Windows y con Linux hay problemas en esta parte.
        # De la tupla, se obtiene el primer elemento que es su ruta absoluta y con Path se obtiene solo el nombre del archivo
        print(Path(archivo_seleccionado[0]).name)
        # se le pone como texto el nombre del archivo al boton de seleccion de archivo de ventas
        ventana_principal.boton_seleccionar_archivo_ventas.setText(Path(archivo_seleccionado[0]).name)
        # tambien se le pone un tooltip para que al poner el mouse sobre el boton como un hover, se vea la ruta absoluta en un pequenio recuadro, por si no llega a caber
        # esto tambien tiene el proposito de tener guardada tambien la ruta absoluta, para luego usarla en subir_archivos()
        ventana_principal.boton_seleccionar_archivo_ventas.setToolTip(archivo_seleccionado[0])


    def subir_archivos(self, ventana_principal):
        """
        Sube el archivo seleccionado de ventas, importando los datos del Excel a la base de datos.
        """

        """
        Esto es un borrador para ver como funcionaban los messagebox, tendria que ser cambiado para conectar la 
        logica de excel_a_bd.py a este controlador
        """

        # del tooltip del boton de seleccion de archivo de ventas se obtiene la rutas absoluta del archivo seleccionado
        ruta_absoluta_archivo_ventas = ventana_principal.boton_seleccionar_archivo_ventas.toolTip()

        # esta variable va a a contener el texto que se muestre en el mensaje
        texto_dialogo = ""
        # se checa si no se selecciono ningun archivo, viendo si la ruta absoluta del tooltip del boton de seleccion de archivo de ventas esta vacio
        if ruta_absoluta_archivo_ventas == "":
            texto_dialogo = "Selecciona un archivo, por favor"
        else:
            texto_dialogo += f"Subiste el archivo: {ruta_absoluta_archivo_ventas} \n"

        # guia en https://www.pythonguis.com/tutorials/pyqt6-dialogs/
        mensaje = QMessageBox(ventana_principal)
        mensaje.setWindowTitle("Archivo subido")
        mensaje.setText(texto_dialogo)
        boton_ok = mensaje.exec()
        # cuando se presiona el boton Ok en el mensaje
        #if boton_ok == QMessageBox.StandardButton.Ok:
        #    print("OK!")

        # esto es para que se "resetee" el valor del archivo seleccionado en el boton
        # de modo que su texto que contiene el nombre del archivo y su tooltip que contiene la ruta absoluta,
        # se cambien a vacios
        ventana_principal.boton_seleccionar_archivo_ventas.setText("")
        ventana_principal.boton_seleccionar_archivo_ventas.setToolTip("")


    def mostrar_ayuda(self, ventana_principal):
        """
        Muestra un mensaje de ayuda cuando el boton de ayuda de la ventana de importar datos es presionado.
        Muestra el formato que debe seguir el Excel de ventas para ser importado.
        """
        
        titulo_mensaje = "Formato del archivo de ventas"
        # esta identacion de texto_mensaje es necesaria, por que si no, los "tabs" que aqui se le pongan para identar, 
        # en el mensaje que se muestre se van a aplicar, lo que hace que se vieran raros
        texto_mensaje = """
Para que el archivo de ventas se importe correctamente es necesario que cumpla con las siguientes características: \n
- La hoja en que se encuentra la información debe de llamarse "Hoja1" \n
- En el primer renglón se debe de indicar los nombres de las columnas   "total", "fecha", "hora", "empleado_id" sin espacios y en minusculas \n
- Debe cuidar que los datos de cada renglón cumplan con lo siguiente: \n
* "total" -> Solo puede tener datos que sean números \n
* "fecha" -> Debe de tener formato de fecha dado por excel o bien puede estar escrito de la siguiente manera "año-mes-dia". Por ejemplo: "2015-01-29" \n
* "hora" -> Debe de tener formato de hora dado por excel o bien puede estar escrito de la siguiente manera "hora:minutos" en formato de 24 horas. Por ejemplo: "16:40" \n
* "empleado_id" -> Su longitud debe de ser de 50 carácteres o menor \n
Si algún renglón no cuenta con este formato, se le notificará el número de renglón y el archivo no se importará.
        """
        # se crea el mensaje y se le pase como padre a la ventana principal para que se le aplique focus y se centre en la ventana principal
        mensaje = QMessageBox(ventana_principal)
        mensaje.setWindowTitle(titulo_mensaje)
        mensaje.setText(texto_mensaje)
        # esto es necesario para que el mensaje aparezca, con esto tambien se puede hacer algo despues de que el boton de "Ok" se presione
        # pero como aqui no es necesario, no se realiza eso
        boton_ok = mensaje.exec()