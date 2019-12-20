# Snake with squares

El juego de snake con un background con cuadros los cuales son de Width=20 y Height=20


# ¡¿Como funciona?!

# Funciona de la siguiente manera:

- Los cuadrados fueron hechos de la siguiente forma:
 
*Dividí 500(W, H) de la ventana entre la longitud de los cuadrados que es igual a 20(W, H) esto es igual a 25(rows, columns) luego para formar los rectangulos use una técnica que vi hace un tiempo en internet para formar un board.

*Los rectangulos tienen un width central de 1 pixel esto para que solo se le vean los bordes.

- Posición de la comida:

*En este caso almacené en una lista todos los numeros divisibles por 20 que estén en el rango de (0, 490) para que se centre en un cuadrado del board en la coordenada x e y.

*La comida debe tener una longitud igual al cuerpo de la serpiente para que pueda centrarse en los cuadrados y para que se vea más elegante cuando la serpiente coma.

- Movimiento de la serpiente:

*Change y direction, change es usada para cuando se vaya a comprobar si la serpiente va en la dirección opuesta a la que se quiere girar y directión para guiar a la serpiente en esa dirección.

*Se utilizan las 4 letras de flechas del teclado para mover la serpiente.

*La posición de la serpiente se actualiza siempre que avanza, de modo que, se va agregando una nueva posición al comencienzo de la lista que contiene el cuerpo de la serpiente, y removiendo su último elemento así la serpiente pasaría de posición en posición con estas 2 funcionalidades.
