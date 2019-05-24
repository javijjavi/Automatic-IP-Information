# Clase en la cual buscaremos si la IP solcitada por el usuario se encuentra en la BD o no.

class buscarBD():
    # Observamos si tenemos instalado la libreria de mongodb.
    try:
        import pymongo
        from pymongo import MongoClient
    except:
        print("Falta libreria mongodb.")
   
    ip = "193.30.35.74"
    # Conectamos con la maquina mongodb en nuestro servidor docker.
    myclient = MongoClient("mongodb://192.168.10.170:55059")
    # Solicitamos la base de datos que queremos.
    mydb = myclient["db_ip"]
    # Solicitamos la columna donde se encuentra la informacion.
    mycol = mydb["ip"]
    # Lanzamos un contador el cual nos cuenta relaciones que encontramos en nuestra base de datos.
    contador_DATA = mycol.count_documents({"IP": ip })
    # Comprobamos los resultados dandole una variable de True y False, para el despues procesamiento.
    if contador_DATA == 1:
        se_han_encontrado_datos = True
    if contador_DATA == 0:
        se_han_encontrado_datos = False
    # Si la variable fue True esta será introducida en un Json y lanzada de nuevo al cliente.
    if se_han_encontrado_datos == True:
        myquery = { "IP": ip }
        mydoc = mycol.find(myquery)
        for dato in mydoc:
            print(dato)
    # Si la variable fue False el programa enviara la IP a la clase selenium para su procesamiento y sacada de información.
    else:
        print("selenium")