import pygame


class ObjecteEscenari:
    def __init__(self, posX, posY, color):
        self.posX = posX
        self.posY = posY
        self.color = color

    def Pinta(self, finestraJoc):
        pygame.draw.rect(finestraJoc, self.color, (self.posX, self.posY, self.midaX, self.midaY))