import pymongo


try:
    myclient = pymongo.MongoClient("mongodb://192.168.10.170:55059")
    #mongodb://usuario:password@host:puerto/nombre_db
    print("VA GUAY")
except:
    print("No se ha podido conectar con la base de datos, revisa MongoDB shell.")