import pygame
from random import choice

pygame.init()



class Food:


    def __init__(self):
        """
        Crea dos posiciones iniciales
        """
        #Guarda todas las posiciones divisibles por 20(w,h de los cuadrados) para que
        # cuando se elija uno random la comida quede centrada en un cuadro
        self.posXY = [x for x in range(0, 490) if x % 20 == 0]#Numeros divisibles por 20
        self.x = choice(self.posXY)#Posición en x
        self.y = choice(self.posXY)#Posición en y
        

    def draw(self, screen):
        """
        Dibuja la comida en la pantalla
        """
        pygame.draw.rect(screen, (0, 170, 1), [self.x, self.y, 20, 20])

    def snakeAte(self, snake_head):
        """
        Determina si la serpiente comió la comida
        (snake_head) = [x, y]
        también es usada para hacer crecer a la serpiente
        :return: bool
        """

        #Si la serpiente comió la comida
        if pygame.Rect(self.x, self.y, 20, 20).collidepoint(snake_head[0], snake_head[1]):
            #Actualizar la posición de la comida
            self.x = choice(self.posXY)
            self.y = choice(self.posXY)
            return True