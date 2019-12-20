import pygame
import sys

pygame.init()



class Snake:

    
    snake_head = [200, 100]#Cabeza de la serpiente
    snake_body = [[200, 100], [180, 100], [160, 100]]


    def __init__(self):
        self.direction = "LEFT"#Dirección en la cual va la serpiente
        self.change = self.direction#Se utiliza para cambiar la dirección de la serpiente


    def draw(self, screen):
        """
        Recorre cada rectangulo en el cuerpo de la serpiente y lo dibuja en pantalla
        """
        #Recorre cada parte(p) del cuerpo
        for p in self.snake_body:
            pygame.draw.rect(screen, (131, 0, 0), [p[0], p[1], 20, 20])

    
    def capKeys(self, event):
        """
        Captura las teclas pulsadas
        """
        #Si una tecla fue presionada
        if event.type == pygame.KEYDOWN:

            #Si la tecla pulsada es la tecla izquierda(flecha) del teclado cambiar
            # dirección a la izquierda 
            if event.key == pygame.K_LEFT:
                self.change = "LEFT"
            
            #Si la tecla pulsada es la tecla abajo(flecha) del teclado cambiar
            # dirección a la abajo
            if event.key == pygame.K_DOWN:
                self.change = "DOWN"

            #Si la tecla pulsada es la tecla derecha(flecha) del teclado cambiar
            # dirección a la derecha
            if event.key == pygame.K_RIGHT:
                self.change = "RIGHT"

            #Si la tecla pulsada es la tecla arriba(flecha) del teclado cambiar
            # dirección a la arriba
            if event.key == pygame.K_UP:
                self.change = "UP"

    def move(self):
        """
        Mueve la serpiente hacia la dirección especificada
        """
        #*******************************Cambiar de dirección**************************

        # Si se quiere cambiar de dirección hacia la izquierda solo permitirlo si la
        # dirección actual no es la derecha
        if self.change == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"

        # Si se quiere cambiar de dirección hacia abajo solo permitirlo si la
        # dirección actual no es la arriba
        if self.change == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"

        # Si se quiere cambiar de dirección hacia la derecha solo permitirlo si la
        # dirección actual no es la izquierda
        if self.change == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

        # Si se quiere cambiar de dirección hacia la arriba solo permitirlo si la
        # dirección actual no es la abajo
        if self.change == "UP" and self.direction != "DOWN":
            self.direction = "UP"


        #*****************************Mover****************************************
        #Le resta 20 pixeles al eje x de la cabeza
        if self.direction == "LEFT":
            self.snake_head[0] -= 20

        #Le resta 20 pixeles al eje y de la cabeza
        if self.direction == "DOWN":
            self.snake_head[1] += 20

        #Le resta 20 pixeles al eje x de la cabeza
        if self.direction == "RIGHT":
            self.snake_head[0] += 20

        #Le resta 20 pixeles al eje y de la cabeza
        if self.direction == "UP":
            self.snake_head[1] -= 20

        
    def update(self):

        """
        Actualiza las posiciones del cuerpo 
        [tail]{body}(head) -> 
        [tail delete]{body is last part or coordinate(x, y)}(head is a new part or coordinate(x, y))
        """
        #agrega una nueva coordenada a al principio del cuerpo, esta es la cabeza
        self.snake_body.insert(0, list(self.snake_head))
        #Elimina la última coordenada del cuerpo, esto mantiene un equilibrio ya que por cada
        # coordenada(x, y) agregadas se elimina la de atras creando así una cadena de partes
        # en constante movimiento 
        self.snake_body.pop()

    def lost(self):
        """
        Si la cabeza de la serpiente colisiona con su cuerpo o con alguno de los bordes
        de la ventana esta muere y por ende se termina el juego
        """

        #Si colisiona con uno de los bordes izquierdo-derecho
        if self.snake_head[0] < 0 or self.snake_head[0] > 490:
            sys.exit()

        #si colisiona con uno de los bordes arriba-abajo
        if self.snake_head[1] < 0 or self.snake_head[1] > 490:
            sys.exit()


        #*********************Comprueba si la serpiente colisionó con su cuerpo*********

        #Si ya la serpiente está lo suficientemente grande para que pueda colisionar con su cuerpo
        if len(self.snake_body) > 6:
            for p in self.snake_body[3:]:
                #Si colisiona con alguna parte de su cuerpo cerrar la ventana
                if pygame.Rect(self.snake_head[0], self.snake_head[1], 20, 20).collidepoint(p[0], p[1]):
                    sys.exit()

    def addTail(self):
        """
        Se usa siempre que la serpiente coma y agrega una nueva cola([x,y]) con el valor de la cola([x,y]) anterior
        """
        x = self.snake_body[len(self.snake_body) - 1][0]#Posición en x de la cola de la serpiente(último rect)
        y = self.snake_body[len(self.snake_body) - 1][1]#Posición en y de la cola de la serpiente(último rect)
        self.snake_body.append([x, y])#Agregamos una nueva lista al cuerpo

            

