import pygame
import random

from ObjecteEscenari import ObjecteEscenari
from constants import Juego, Colors, Jugadores, Pilotas

class Pilota(ObjecteEscenari):
    def __init__(self, color):
        self.midaX = Pilotas.MIDAX_PILOTA
        self.midaY = Pilotas.MIDAY_PILOTA
        self.color = color
        self.velocitat_inicial = Pilotas.VELOCITAT
        self.reinicia()
        super().__init__(self.posX, self.posY, color)


    def reinicia(self):
        self.posX = Juego.AMPLA_FINESTRA // 2
        self.posY = Juego.ALCADA_FINESTRA // 2
        self.velocitat = self.velocitat_inicial
        # Se elige una dirección aleatoria entre las diagonales
        self.direccio = random.choice([[-1, -1], [-1, 1], [1, -1], [1, 1]])

    def augmenta_velocitat(self):
        self.velocitat = self.velocitat * 1.1


    def MovimentPilota(self, jugador1, jugador2):
        self.posX += self.velocitat * self.direccio[0]
        self.posY += self.velocitat * self.direccio[1]

        # Rebote en la parte superior o inferior de la pantalla
        if self.posY <= Juego.MARGES_ESCENARI[1] or self.posY >= (
                Juego.ALCADA_FINESTRA - Juego.MARGES_ESCENARI[1]) - self.midaY:
            self.direccio[1] = -self.direccio[1]

        # Crear los coliders para la pelota y los jugadores
        rect_pilota = pygame.Rect(self.posX, self.posY, self.midaX, self.midaY)
        rect_jugador1 = pygame.Rect(jugador1.posX, jugador1.posY, jugador1.midaX, jugador1.midaY)
        rect_jugador2 = pygame.Rect(jugador2.posX, jugador2.posY, jugador2.midaX, jugador2.midaY)

        # Rebote en los lados izquierdo o derecho de la pantalla
        if self.posX <= 0:
            if rect_pilota.colliderect(rect_jugador1):
                self.direccio[0] = -self.direccio[0]
                self.augmenta_velocitat()
            else:
                jugador2.punts += 1
                self.reinicia()
        elif self.posX >= (Juego.AMPLA_FINESTRA) - self.midaX:
            if rect_pilota.colliderect(rect_jugador2):
                self.direccio[0] = -self.direccio[0]
                self.augmenta_velocitat()
            else:
                jugador1.punts += 1
                self.reinicia()

        # Comprobar colisiones con los jugadores
        if rect_pilota.colliderect(rect_jugador1) or rect_pilota.colliderect(rect_jugador2):
            self.direccio[0] = -self.direccio[0]
            self.augmenta_velocitat()