import pygame

pygame.init()#inicializar el motor

screen = pygame.display.set_mode((450, 450)) #creacion de ventana
pygame.display.set_caption("Tic Tac Toe") #Titulo de la ventana/ juego

fondo = pygame.image.load("static/tictactoe_background.png") #Fondo el juego
circulo = pygame.image.load("static/circle.png")
equis = pygame.image.load('static/x.png')

fondo = pygame.transform.scale(fondo, (450, 450)) #Sobre escribir varible para ajustar la escala
circulo = pygame.transform.scale(circulo, (125, 125))
equis = pygame.transform.scale(equis, (125, 125))   


coor = [[(40,50),(165,50),(290,50)], #Cordenas X,Y 
        [(40,175),(165,175),(290,175)],
        [(40,300),(165,300),(290,300)]]

tablero = [['','',''], #Tablero
         ['','',''],
         ['','','']]

turno = 'X' #Primer turno
game_over = False #Estado del juego
clock = pygame.time.Clock()#Estableser los fps del juego

def graficar_boar():
    """
    Grafica el fondo y verifica si la matrix tiene una X o O.
    """
    screen.blit(fondo, (0,0))#Graficar el fondo primero es IMPORTANTE
    for fila in range(3):#Iterar sobre la matrix
        for col in range(3):
            if tablero[fila][col] == 'X':
                pass
            elif tablero[fila][col] == 'O':
                pass

def dibujar_x(fila,col):
    pass

while not game_over: #Graficar las acciones del juego
    clock.tick(30)#FPS

    for event in pygame.event.get():#Captura todos los eventos que se hayan registrado durante la iteracion anterior
        if event.type == pygame.QUIT:
            game_over = True

    
    screen.blit(circulo, (40,50))
    screen.blit(equis, (160,165))
    pygame.display.update()#Actualizar nuestro display

pygame.quit()#Salir de juego