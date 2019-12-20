import pygame
import sys
from Board.board import Board
from Snake.snake import Snake
from Food.food import Food

pygame.init()

W, H = 500, 500#Dimensiones de la ventana

#Author@ Steven Beltrán De León

pygame.display.set_caption('Snake game')# 

def game():
    screen = pygame.display.set_mode((W, H))
    board = Board()#Tablero
    snake = Snake()#Serpiente
    food = Food()#Comida

    fps = pygame.time.Clock()#FPS

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit(); pygame.quit()

            snake.capKeys(event)
        
        snake.move()#Mueve la serpiente
        snake.update()# Actualiza su cuerpo
        snake.lost()# Si pierde termina el juego

        if food.snakeAte(snake.snake_head):#Si la serpiente se come a la comida posicionarla en otra posición
            snake.addTail()#Agrega una nueva cola

        screen.fill(0)#Background negro
        board.draw(screen)#Dibuja el tablero
        snake.draw(screen)#Dibuja la serpiente
        food.draw(screen)# Dibuja la serpiente
        pygame.display.update()
        fps.tick(10)#10 cuadros por segundo

if __name__ == "__main__":
    game()