# Clase jugador con los siguients atributos: posX,posY y color
import pygame

from ObjecteEscenari import ObjecteEscenari
from constants import Juego, Colors, Jugadores


class Jugador(ObjecteEscenari):
    # Constructor
    def __init__(self, name):

        # Definimos los atributos de la clase comunes (Todos tendrán los mismos)
        self.name = name
        self.midaX = Jugadores.MIDAX_JUGADOR
        self.midaY = Jugadores.MIDAY_JUGADOR
        self.velocitat = Jugadores.VELOCIDAD
        self.punts = 0

        # Dependiendo del nombre del jugador, se le asignará una posición y un color diferente

        if self.name == "Jugador 1":
            self.posX = Jugadores.COSTAT_JUGADOR
            self.posY = Juego.ALCADA_FINESTRA // 2 - Jugadores.COSTAT_JUGADOR // 2
            self.color = Colors.BLANC
        elif self.name == "Jugador 2":
            self.posX = Juego.AMPLA_FINESTRA - (Jugadores.COSTAT_JUGADOR + Jugadores.MIDAX_JUGADOR)
            self.posY = Juego.ALCADA_FINESTRA // 2 - Jugadores.COSTAT_JUGADOR // 2
            self.color = Colors.GROC
        else:
            # Si el nombre del jugador no es válido, se mostrará un mensaje de error y se cerrará el programa
            print("Error: Nombre de jugador no válido")
            exit()

        super().__init__(self.posX, self.posY, self.color)

    def MoureMunt(self):
       self.posY = max(self.posY - self.velocitat, Juego.MARGES_ESCENARI[1]) # Ponemos los márgenes para que no se salga de la pantalla

    def MoureBaix(self):
        self.posY = min(self.posY + self.velocitat, Juego.ALCADA_FINESTRA - self.midaY - Juego.MARGES_ESCENARI[
            1])  # Ponemos los márgenes para que no se salga de la pantalla

