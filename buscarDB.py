# Clase en la cual buscaremos si la IP solcitada por el usuario se encuentra en la BD o no.
import seleniumDATA
import procesamintoIPS

try:
    import pymongo
    from pymongo import MongoClient
except:
    print("Falta libreria mongodb.")

class buscarBD():
    def sacar_DB(self):
        myclient = MongoClient("mongodb://192.168.10.170:55059")         # Conectamos con la maquina mongodb en nuestro servidor docker.                           
        mydb = myclient["db_ip"]        # Solicitamos la base de datos que queremos.
        mycol = mydb["ip"]      # Solicitamos la columna donde se encuentra la informacion.
        contador_DATA = mycol.count_documents({"IP": ip })      # Lanzamos un contador el cual nos cuenta relaciones que encontramos en nuestra base de datos.
        # Comprobamos los resultados dandole una variable de True y False, para el despues procesamiento.
        if contador_DATA == 1:
            se_han_encontrado_datos = True
        if contador_DATA == 0:
            se_han_encontrado_datos = False
        return se_han_encontrado_datos
        sacar_DB()
        if se_han_encontrado_datos == True:
            myquery = { "IP": ip }
            mydoc = mycol.find(myquery)
            for dato in mydoc:
                print(dato)
        # Si la variable fue False el programa enviara la IP a la clase selenium para su procesamiento y sacada de información.
        else:
            seleniumDATA