import serial # pip install pyserial
import time

# COM5 o el numero correspondiente, se generan al conectar con el dispositivo
bluetooth_serial = serial.Serial('COM4', baudrate= 115200, timeout = 1)
time.sleep(2) # Esperar la conexion

try:
 while True:
 # Enviar mensaje BT
 message = input("Escribe un mensaje para enviar al ESP32: ")
 bluetooth_serial.write((message + '\n')).encode('utf-8')

 # Leer respuesta por BT
 # if bluetooth_serial.in_waiting: # Evita bloqueo de recepcion
 response = bluetooth_serial.readline().decode('utf-8').strip()
 print(f"ESP32 respondio: {response}")
except Exception as e:
 print(f"Ocurrio un error: {e}")