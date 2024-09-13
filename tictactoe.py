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
                dibujar_x(fila,col)
            elif tablero[fila][col] == 'O':
                dibujar_o(fila,col)

def dibujar_x(fila,col):
    """
    Funcion que le pasamos las filas y columnas y grafica la X
    """
    screen.blit(equis, coor[fila][col])

def dibujar_o(fila,col):
    """
    Funcion que le pasamos las filas y columnas y grafica la O
    """
    screen.blit(circulo, coor[fila][col])

def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != '': #verificar horizontalmente
            return True 
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != '': #verificacion vertical
            return True 
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '': 
        return True 
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '': 
       return True 
    return False
    
while not game_over: #Graficar las acciones del juego
    clock.tick(30)#FPS

    for event in pygame.event.get():#Captura todos los eventos que se hayan registrado durante la iteracion anterior
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN: #Evento de click de boton
            mouseX, mouseY = event.pos
            if (mouseX >= 40 and mouseX < 415) and (mouseY >= 50 and mouseY < 425): #Logica para marcalar los limites de la tablero
                fila = (mouseY - 50) // 125
                col = (mouseX - 40) // 125
                if tablero[fila][col] == '': #Logica para verificar si posicion esta vacia
                    tablero[fila][col] = turno
                    fin_juego = verificar_ganador()
                    print(fin_juego)
                    if fin_juego:
                        print(f"El jugador {turno} a ganado!!")
                        game_over = True
                    turno = 'O' if turno == 'X' else 'X'#Cambio de turno
    
    graficar_boar()
    pygame.display.update()#Actualizar nuestro display


pygame.quit()#Salir de juego