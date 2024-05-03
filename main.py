import sys
import pygame

import constants
from Pilota import Pilota
from constants import Juego, Colors, Juego
import Jugador

# Inicializamos pygame
pygame.init()
fontText = pygame.font.SysFont("monospace", 22)

# Creamos la ventana del juego, el reloj y la variable que controla el fin del juego
finestraJoc = pygame.display.set_mode((Juego.AMPLA_FINESTRA, Juego.ALCADA_FINESTRA))
rellotge = pygame.time.Clock()
gameOver = False

# Creamos los dos jugadores
jugador1 = Jugador.Jugador("Jugador 1")
jugador2 = Jugador.Jugador("Jugador 2")

# Creamos la pelota en el centro de la pantalla
pilota = Pilota(Colors.BLANC)

# Función que pinta los objetos en la pantalla
def PintaObjectes(jugador1, jugador2, pilota):
    # Pintamos el fondo
    finestraJoc.fill(Colors.VERD)
    pygame.draw.rect(finestraJoc, Colors.NEGRE, Juego.MARGES_ESCENARI)

    # Pinta els jugadors i la pilota
    jugador1.Pinta(finestraJoc)
    jugador2.Pinta(finestraJoc)
    pilota.Pinta(finestraJoc)

    textJugador1 = "Jugador 1: " + str(jugador1.punts)
    textJugador2 = "Jugador 2: " + str(jugador2.punts)

    etiquetaJugador1 = fontText.render(textJugador1, 1, Colors.BLANC)
    etiquetaJugador2 = fontText.render(textJugador2, 1, Colors.BLANC)

    finestraJoc.blit(etiquetaJugador1, (50, 50))
    finestraJoc.blit(etiquetaJugador2, (Juego.AMPLA_FINESTRA - 200, 50))

# Función que detecta los eventos de teclado
def DetectaEvents(jugador1, jugador2, pilota):

    # Detectamos los eventos de teclado
    keys = pygame.key.get_pressed()

    # Movemos los jugadores
    if keys[pygame.K_w]:
        jugador1.MoureMunt()
    if keys[pygame.K_s]:
        jugador1.MoureBaix()
    if keys[pygame.K_UP]:
        jugador2.MoureMunt()
    if keys[pygame.K_DOWN]:
        jugador2.MoureBaix()

    # Detectamos si se ha cerrado la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


# Bucle principal del juego
while not gameOver:
    PintaObjectes(jugador1, jugador2, pilota)
    DetectaEvents(jugador1, jugador2, pilota)

    pilota.MovimentPilota(jugador1, jugador2)

    rellotge.tick(Juego.TASA_DE_REFRESCO)
    pygame.display.update()