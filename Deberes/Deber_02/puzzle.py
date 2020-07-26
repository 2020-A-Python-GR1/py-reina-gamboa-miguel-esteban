import numpy as np
import pygame

IMAGE_FILE = "Bandera-Suiza.jpg" 
IMAGE_SIZE = (450, 450)
filas = 0
columnas = 0

def puzzle():
    global filas, columnas
    num = int(input('Dimension del puzzle: '))    
    COLUMNS = num
    ROWS = num    
    movimientos = 20
    FICHA_WIDTH = IMAGE_SIZE[0] / COLUMNS
    FICHA_HEIGHT = IMAGE_SIZE[1] / ROWS

    hor_border = pygame.Surface((int(FICHA_WIDTH), 2))
    ver_border = pygame.Surface((2, int(FICHA_HEIGHT)))

    imagen = pygame.image.load(IMAGE_FILE)
    fichas = {}
    for r in range(ROWS):
        for c in range(COLUMNS):
            pieza = imagen.subsurface(int(r*FICHA_HEIGHT), int(c*FICHA_WIDTH), int(FICHA_HEIGHT), int(FICHA_WIDTH))
            pieza.blit(hor_border, (0, 0))
            pieza.blit(ver_border, (0, 0))
            fichas[(r,c)] = pieza

    ficha_disponible = (np.random.randint(num),np.random.randint(num))
    fichas[ficha_disponible].fill((0,0,0))
    (filas, columnas) = ficha_disponible 

    posicion_inicial = {(row,col): (row,col) 
                      for row in range(ROWS) for col in range(COLUMNS)}
    posicion = {(row,col): (row,col) 
              for row in range(ROWS) for col in range(COLUMNS)}

    pygame.init()
    display = pygame.display.set_mode((IMAGE_SIZE))
    pygame.display.set_caption("Puzzle")
    display.blit (imagen, (0, 0))
    pygame.display.flip() 

    def mover_ficha(r,c):
         global columnas, filas
         display.blit(fichas[posicion[(r, c)]], (int(filas*FICHA_HEIGHT), int(columnas*FICHA_WIDTH))) 
         display.blit(fichas[ficha_disponible], (int(r*FICHA_HEIGHT), int(c*FICHA_WIDTH))) 
         posicion[(filas, columnas)] = posicion[(r, c)]
         posicion[(r, c)] = ficha_disponible
         (filas, columnas) = (r, c)
         pygame.display.flip() 
         
    def ordenar_ficha():
        for i in range(movimientos):
            mover_ficha(np.random.randint(num),np.random.randint(num))
            pygame.time.delay(150) 

    def mensaje():
        font = pygame.font.SysFont("arial",80)
        fuente = font.render("¡Ganador!",True, (0,0,0))
        texto = fuente.get_rect()
        texto.center = (int(IMAGE_SIZE[0]/2),int(IMAGE_SIZE[1]/2))
        display.blit(fuente, texto) 
        pygame.display.update()

    inicia = True
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if inicia:
                ordenar_ficha()
                inicia = False
            else:
                posicion_mouse = pygame.mouse.get_pos() 
                r = int(posicion_mouse[0] / FICHA_HEIGHT)
                c = int(posicion_mouse[1] / FICHA_WIDTH)        
                mover_ficha(r,c)
                if (posicion_inicial == posicion):                                
                    imagen = pygame.image.load(IMAGE_FILE)
                    pygame.init()
                    display = pygame.display.set_mode(IMAGE_SIZE)
                    pygame.display.set_caption("Puzzle")
                    display.blit (imagen, (0, 0))
                    pygame.display.flip()  
                    mensaje()

puzzle()
