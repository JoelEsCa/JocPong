import sys
import pygame

import constants
from constants import Juego, Colors, Juego
import Jugador

# Inicializamos pygame
pygame.init()

# Creamos la ventana del juego, el reloj y la variable que controla el fin del juego
finestraJoc = pygame.display.set_mode((Juego.AMPLA_FINESTRA, Juego.ALCADA_FINESTRA))
rellotge = pygame.time.Clock()
gameOver = False

# Creamos los dos jugadores
jugador1 = Jugador.Jugador("Jugador 1")
jugador2 = Jugador.Jugador("Jugador 2")


# Función que pinta los objetos en la pantalla
def PintaObjectes(jugador1, jugador2):
    # Pintamos el fondo
    finestraJoc.fill(Colors.VERD)
    pygame.draw.rect(finestraJoc, Colors.NEGRE, Juego.MARGES_ESCENARI)

    # Pinta los jugadores
    jugador1.pintar(finestraJoc)
    jugador2.pintar(finestraJoc)


# Función que detecta los eventos de teclado
def DetectaEvents(jugador1, jugador2):

    # Detectamos los eventos de teclado
    keys = pygame.key.get_pressed()

    # Movemos los jugadores
    if keys[pygame.K_w]:
        jugador1.moviment("arriba")
    if keys[pygame.K_s]:
        jugador1.moviment("abajo")
    if keys[pygame.K_UP]:
        jugador2.moviment("arriba")
    if keys[pygame.K_DOWN]:
        jugador2.moviment("abajo")

    # Detectamos si se ha cerrado la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


# Bucle principal del juego
while not gameOver:

    # Pintamos los objetos y detectamos los eventos
    PintaObjectes(jugador1, jugador2)
    DetectaEvents(jugador1, jugador2)

    # Añadimos la tasa de refresco y actualizamos la pantalla
    rellotge.tick(Juego.TASA_DE_REFRESCO)
    pygame.display.update()