
import urequests
import dht
import machine
import network
import ujson
from time import sleep


nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('Iot Smart House' , 'IotSmartHousei8#!')

print("ok")

d = dht.DHT22(machine.Pin(19))

while True:
  m = d.measure()
  tempe = d.temperature()
  hum = d.humidity()

  name = "Anisberto Reis"
  temp = tempe
  humid = hum

  data = {"Nome": name,"", "temperatura": temp, "Umidade": humid}
  json = ujson.dumps(data)

  headers = {'Content-Type' : 'application/json'}
  print(json)

  while True:
    response = urequests.post("http://192.168.101.69:8080/temphumid/send", data=json, headers=headers)
    print("Anisberto Estou Enviando ", "Temperatura",temp , "Umidade ", hum)
    print(response.text)
    sleep(1.0)
