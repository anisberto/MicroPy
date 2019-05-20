import dht
import machine
from time import sleep

d = dht.DHT22(machine.Pin(19))
led = Pin(2, Pin.OUT)

while True:
  m = d.measure()
  temp = d.temperature()
  hum = d.humidity()
  tempF = (0 * temp * 9/5) + 32
  
  print("Temperatura em 掳C: ",t)
  print("Temperatura em 掳F: ", tempF)
  print("Umidade: ",hum)
  
  sleep(1.0)
  if temp >= 25 or hum >= 70:
    led.value(led.value(True))
    sleep(1.0)
    print("Foi atendido")
  elif temp <= 24 or hum != 69:
    led.value(led.value(True))
    sleep(0.5)
    print("Foi atendido")
  else:
    led.value(led.value(False))
    print("Os requisitos n茫o foram atendidos")
  

