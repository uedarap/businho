import time
import os # aqui se necesita el os para que permita interactuar con el sistema operativo (aqui para limpiar la pantalla mientras los buses avanzan)
from random import randint # aqui el randiant genera numeros aleatorios, que se usa para determinar cual bus avanza 
import pygame
from pygame import mixer # mixer para el uso del audio

# aqui se iniciliza el audio 
mixer.init()

# Funcion para reproducir el audio al inicio
def play_audio():
    mixer.music.load(os.path.join(os.path.dirname(__file__), 'businho.mp3')) #aqui cargamos el audio de forma dinamica
    mixer.music.play(-1) # con esto reproduce el audio indefinidamente con el -1, por lo que la musica continuara hasta que sea detenida manualmente


# Funcion para detener el audio al finalizar la carrera
def stop_audio():
    mixer.music.stop()

# Funcion para dibujar los buses
def buses(n1, n2):
    print(115 * "-") # el print(115 * "-") se encarga de imprimir 115 guiones, esta linea se usa para separar los 2 buses
    print((n1 * " ") + "________________" + ((100 - n1) * " ") + "|")
    print((n1 * " ") + "|__|__|__|__|__|__" + ((97 - n1) * " ") + "|")
    print((n1 * " ") + "|       UE        |" + ((96 - n1) * " ") + "|")
    print((n1 * " ") + "|----@--------@---|" + ((96 - n1) * " ") + "|")
    print(115 * "-")
    print((n2 * " ") + "________________" + ((100 - n2) * " ") + "|")
    print((n2 * " ") + "|__|__|__|__|__|__" + ((97 - n2) * " ") + "|")
    print((n2 * " ") + "|       LO        |" + ((96 - n2) * " ") + "|")
    print((n2 * " ") + "|----@--------@---|" + ((96 - n2) * " ") + "|")
    print(115 * "-")

# aqui Funcion para limpiar la pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Variables iniciales
a = 0
b = 0

clear_screen()
print("💵💵💵🤑💰  FAÇAM SUAS APOSTAS 💰🤑💵💵💵")
print("  UE ❌ LO  ")
print("🏁🏁🏁 Pressione Enter para corrida 🏁🏁🏁")
input()

# aqui inicia el audio cuando comienza la carrera
play_audio()

# Carrera de buses
while a < 97 and b < 97:
    c = randint(1, 2)
    if c == 1:
        a += 1
    else:
        b += 1

    clear_screen()
    buses(a, b)
    time.sleep(0.05)

# aqui detiene el audio al finalizar la carrera
stop_audio()

# con esto se Verifica quien gano
if a == 97:
    gano = "UE"
elif b == 97:
    gano = "LO"

print(f"🎉🥇 {gano} 🥇🎉")
