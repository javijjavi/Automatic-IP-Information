# Recivimos un Json con una o varias IPS
import buscarDB
try:
    import json
except:
    print("No se encontro la libreria Json.")

class procesamientoIPS:
    def procesarIP(self):
        ip = "192.168.50.32"
        parse_ip = json.loads(jsonIP)
        ip = (parse_ip["ip"])
        buscarDB(ip)

    def procesarIPS(self):
        parse_IPS = jsonIPS
        ips_array = json.loads(parse_IPS)
        for ip in ips_array:
            global ip
            buscarDB(ip)