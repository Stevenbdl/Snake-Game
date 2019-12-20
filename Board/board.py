import pygame
import sys

pygame.init()

W, H = 500, 500



class Board:

    size = 20#Ancho(With, Heigh) de cada cuadro en la pantalla
    def __init__(self):
        self.board = []#Almacena una lista de 
        self.create()

    def draw(self, screen):
        for s in self.board:
            for square in s:
                pygame.draw.rect(screen, (255, 255, 255), square, 1)


    def create(self):
        """
        Crea el tablero
        width, height = 500, 500
        sizeSquare = 20
        500 / 20 = 25rows(filas) y 25colum(columnas)
        """
        for r in range(0, 25):
            row = []#fila para agregar elementos 
            for c in range(0, 25):
                row.append([self.size * c, self.size * r, self.size, self.size])

            self.board.append(row)#Agrega la nueva fila
            row = []#vacía la lista despúes de agregar 25 elementos 
