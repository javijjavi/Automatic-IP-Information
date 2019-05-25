# Clase en la cual buscaremos las IP no encontradas en la BD en la web utilizando la herramienta selenium.
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
class seleniumDATA:
    
    def __init__(self, ip, ASN, ISP, organizacion, pais, estado, ciudad):
        self.ip = ip
        self.ASN = ASN
        self.ISP = ISP
        self.organizacion = organizacion
        self.pais = pais
        self.estado = estado
        self.ciudad = ciudad
        
    def buscar_datos_IP(self):
        options = Options()
        options.headless = True
        brower = webdriver.Firefox(options=options, executable_path=r"C:\PROYECTOS\WebDriver\Firefox\geckodriver.exe")
        website_URL ="https://db-ip.com/"
        brower.get(website_URL)
        elem = brower.find_element_by_id("search_input").send_keys(self.ip)
        hacer_click = brower.find_element_by_css_selector("button.btn.btn-outline-secondary").click()        
        web = brower.current_url
        sacar_datos_IP(web, brower)
        return web

    def sacar_datos_IP(self, web, brower):
        brower.get(web)
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

        posicion = 0
        for titulo in titulos:
            if titulo == "ASN":
                self.ASN = datos[posicion]
                posicion = posicion + 1
            elif titulo == "ISP":
                self.ISP = datos[posicion]
                posicion = posicion + 1

            elif titulo == "Organization":
                self.organizacion = datos[posicion]
                posicion = posicion + 1

            elif titulo == "Country":
                self.pais = datos[posicion]
                posicion = posicion + 1

            elif titulo == "State / Region":
                self.estado = datos[posicion]
                posicion = posicion + 1

            elif titulo == "City":
                self.ciudad = datos[posicion]
                posicion = posicion + 1
            else:
                posicion = posicion + 1
                continue

        if 'organizacion' in locals():
            self.organizacion = self.organizacion
        else:
            self.organizacion = "N/A"

        brower.close()    
    introducir_datos_BD()

    def introducir_datos_BD(self):
        try:
            import pymongo
            from pymongo import MongoClient
        except:
            print("Falta libreria mongodb.")

        myclient = MongoClient("mongodb://192.168.10.170:55059")
        mydb = myclient["DB_IPS"]
        mycol = mydb["ips"]   
        mydates = {
            "IP": self.ip,
            "ASN": self.ASN,
            "ISP": self.ISP,
            "Organización": self.organizacion,
            "Pais": self.pais,
            "Estado": self.estado,
            "Ciudad": self.ciudad  
        }
        insertar = mycol.insert_one(mydates)

