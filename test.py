#!/usr / bin / env python 

# Importamos las librerias de selenium si, hubiera algun fallo el programa nos mostrará el error y cerrará este.

try:
    from selenium import webdriver 
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import time 
    import selenium as se
    from selenium.webdriver.firefox.options import Options
except:
    print("Falta la libreria selenium en su python, pip install selenium")
    time.sleep(10)
    exit()

# Leemos el archivo ips.txt para sacar todas la IP disponibles. Si no se encuentra el archivo txt habria que crearlo.

try:
    with open('ips.txt', 'r') as dominio:
        dominios = dominio.readlines()
    with open('ips.txt', 'r') as dominio:
        dominios = [line.strip() for line in dominio]
except:
    print("No se ha encontrado el archivo dominios.txt, o se ha localizado algun fallo relacionado con el, porfavor revisalo.")

# Comprobamos librerias de mongodb

try:
    import pymongo
except:
    print("Falta la libreria de mongodb en su python, pip install pymongo")

# Conexion con la base de datos MongoDB, creacion de database y de column.

try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["db_ip"]
    mycol = mydb["ip"]
    mycol.drop()
except:
    print("No se ha podido conectar con la base de datos, revisa MongoDB shell.")

# Importamos psutil para saber cuanto consume nuestra aplicación

try:
    import psutil
except:
    print("No se ha encontrado la libreria psutil.")

_id = 0

# En la funcion "funcion_analizarURL" indicaremos al we de donde extraemos la información y enviamos las direntes ip.

def funcion_analizarURL(dominios, _id):
    for dominio in dominios:
        options = Options()
        options.headless = True
        brower = webdriver.Firefox(options=options, executable_path=r"C:\PROYECTOS\WebDriver\Firefox\geckodriver.exe")
        website_URL ="https://db-ip.com/"
        brower.get(website_URL)
        start = time.time()
        elem = brower.find_element_by_id("search_input").send_keys(dominio)
        hacer_click = brower.find_element_by_css_selector("button.btn.btn-outline-secondary").click()        
        web = brower.current_url
        _id = _id + 1
        funcion_sacarINF(_id, web, brower, dominio)
        end = time.time()
        tiempo_procesado = end - start
        print("El tiempo procesado para el proceso "+str(_id)+" es de "+str(tiempo_procesado)+" segundos.")
        del elem
        del web
    print("Memoria usada en MB: "+memory_usage_psutil())

# En la funcion "funcion_sacarINF" extraemos la informacion que queremos de las diferente IP analizadas.

def funcion_sacarINF(_id, web, brower, dominio):
    brower.get(web)
    time.sleep(5)
    tabla_datos = brower.find_elements_by_xpath("//table[@class='table table-norowsep']//td")
    tabla_titulos = brower.find_elements_by_xpath("//table[@class='table table-norowsep']//th")
    datos = []
    for dato in tabla_datos:
        text = dato.text
        datos.append(text)
    titulos = []
    for titulo in tabla_titulos:
        text = titulo.text
        titulos.append(text)
    dominio = dominio
    time.sleep(2)
    brower.close()
    posicion = 0
    for titulo in titulos:
        
        if titulo == "ASN":
            ASN = datos[posicion]
            posicion = posicion + 1
        elif titulo == "ISP":
            ISP = datos[posicion]
            posicion = posicion + 1

        elif titulo == "Organization":
            organizacion = datos[posicion]
            posicion = posicion + 1

        elif titulo == "Country":
            pais = datos[posicion]
            posicion = posicion + 1

        elif titulo == "State / Region":
            estado = datos[posicion]
            posicion = posicion + 1

        elif titulo == "City":
            ciudad = datos[posicion]
            posicion = posicion + 1
        else:
            posicion = posicion + 1
            continue

    funcion_introducirMongoDB(_id, ip, ASN, ISP, organizacion, pais, estado, ciudad)



    funcion_memoryMagnement(brower)

def funcion_introducirMongoDB(_id, ip, ASN, ISP, organizacion, pais, estado, ciudad):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["db_ip"]
    mycol = mydb["ip"]   
    mydates = {
    "_id": _id,
    "IP": ip,
    "ASN": ASN,
    "ISP": ISP,
    "Organización": organizacion,
    "Pais": pais,
    "Estado": estado,
    "Ciudad": ciudad  
    }
    insertar = mycol.insert_one(mydates)

    print(insertar)

def memory_usage_psutil():
    # return the memory usage in MB
    import os
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / (2 ** 20)
    return mem

def funcion_memoryMagnement(brower):
    memoria = psutil.virtual_memory()
    controlador = 100 * 1024 * 100
    if memoria.available <= controlador:
        brower.close
        exit()

funcion_analizarURL(dominios, _id)