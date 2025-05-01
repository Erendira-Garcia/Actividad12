import serial # pip install pyserial
import time

# COM5 o el numero correspondiente, se generan al conectar con el dispositivo
bluetooth_serial = serial.Serial('COM5', baudrate= 115200, timeout = 1)
time.sleep(2) # Esperar la conexion

try:
    while True:
        # Recibe mensaje por BT
        if bluetooth_serial.in_waiting:
            message = bluetooth_serial.readline().decode('utf-8').strip()

            valores = message.split(",")
            x_porc = float(valores[0])
            y_porc = float(valores[1])
            print (f"x_porc =  {x_porc * 100} %,  y_porc = {y_porc * 100} %")
except Exception as e:
        print(f"Ocurrio un error: {e}")