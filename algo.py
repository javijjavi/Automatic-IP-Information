try:
    myclient = pymongo.MongoClient("mongodb://foouser:foopwd@10.0.75.2:27017/")
    #mongodb://usuario:password@host:puerto/nombre_db
    mydb = myclient["db_ip"]
    mycol = mydb["ip"]
    mycol.drop()
except:
    print("No se ha podido conectar con la base de datos, revisa MongoDB shell.")