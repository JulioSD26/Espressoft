from mysql.connector import connect,Error


def get_credenciales_local():
    with open("Credenciales_bd.txt", "r") as archivo:
        contador = 0
        dict_local = {}
        for linea in archivo:
            linea = linea.rstrip()

            if linea == "LOCAL":
                contador = 1
                continue
            if contador >= 1 and contador < 5:
                linea = linea.split(":")
                dict_local[linea[0]] = linea[1]
                contador += 1
        return dict_local

def get_credenciales_nube():
    with open("Credenciales_bd.txt", "r") as archivo:
        contador = 0
        dict_nube = {}
        for linea in archivo:
            linea = linea.rstrip()
            if linea == "NUBE":
                contador = 1
                continue
            if contador >= 1 and contador < 5:
                linea = linea.rstrip()
                linea = linea.split(":")
                dict_nube[linea[0]] = linea[1]
                contador += 1
        return dict_nube
    
def crear_conexion_local():
    try:
        credenciales = get_credenciales_local()
        conn = connect(host=credenciales['host'],
                       user=credenciales['username'],
                       password=credenciales['password'],
                       database=credenciales['database'],
                       port=3306)
        
        return conn
    
    except Error as err:
        print("Algo salio mal: {}".format(err))


def crear_conexion_nube():
    try:
        credenciales = get_credenciales_nube()
        conn = connect(host=credenciales['host'],
                       user=credenciales['username'],
                       password=credenciales['password'],
                       database=credenciales['database'],
                       port=3306)
        
        return conn
    
    except Error as err:
        print("Algo salio mal: {}".format(err))



    
          

             
              


