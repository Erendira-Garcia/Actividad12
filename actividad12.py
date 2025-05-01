import serial # pip install pyserial
import time
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image # pip install pillow
from threading import Thread

# COM5 o el numero correspondiente, se generan al conectar con el dispositivo
# Configura el puerto Bluetooth
bluetooth_serial = serial.Serial('COM5', baudrate= 115200, timeout = 1)
time.sleep(2) # Esperar la conexion

# Cargar imagen y convertir a np
image_path = 'astronauta.png'
IMG_WIDTH = 50
original_image = Image.open(image_path).convert('RGBA')
resized_image = original_image.resize((IMG_WIDTH, IMG_WIDTH))
np_image = np.array(resized_image)

# Crear la gráfica
WIDTH = 800
HEIGHT = 600
fig, ax = plt.subplots()
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_aspect('equal')

# Grafica la imagen en una posicion inicial (0, 0)
image_plot = ax.imshow(np_image, extent = (0, IMG_WIDTH, 0, IMG_WIDTH))

# Funcion para mover la imagen a una posicion (x, y)
def mover_avatar(x,y):
    image_plot.set_extent(extent=(
        x, x + IMG_WIDTH,
        y, y + IMG_WIDTH))
    fig.canvas.draw_idle()
	
# Funcion para mover la grafica a una posicion (x, y) aleatoria cada segundo
def actualizar_grafica_bt():
    prev_x = 0
    prev_y = 0
    while True:
        try:
            if bluetooth_serial.in_waiting:
                message = bluetooth_serial.readline().decode('utf-8').strip()

                valores = message.split(",")
                x_porc = float(valores[0])
                y_porc = float(valores[1])
                print (f"x_porc =  {x_porc * 100} %,  y_porc = {y_porc * 100} %")
        
                x = x_porc * (WIDTH - IMG_WIDTH)
                y = y_porc * (HEIGHT - IMG_WIDTH)
                if x != prev_x or y != prev_y:
                    mover_avatar(x,y)
                    prev_x = x
                    prev_y = y
        except:
            print("Algo salio mal :( ")
			
# Demonio para actualizar la gráfica
Thread(target = actualizar_grafica_bt, daemon = True).start()

# Muestra la grafica
plt.show()