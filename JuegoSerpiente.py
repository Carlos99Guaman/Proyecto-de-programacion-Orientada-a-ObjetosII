import pygame
import random
import time


class Cuerpo:#1
    def __init__(self, window):
        self.x = 0
        self.y = 0
        self.window = window
        self.dir = 0 
#2
    def draw(self):
        pygame.draw.rect(self.window, (255, 255, 255), (self.x, self.y, 10, 10))
#3
    def movement(self):
        if self.dir == 0:
            self.x += 10
        elif self.dir == 1:
            self.x -= 10
        elif self.dir == 2:
            self.y += 10
        elif self.dir == 3:
            self.y -= 10


class comida:#4
    def __init__(self, window):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10
        self.window = window

    def draw(self):
        pygame.draw.rect(self.window, (255, 0,0), (self.x, self.y, 10, 10))

    def relocate(self):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10

#5
def redraw(window):
    window.fill((0, 0, 0))
    comida.draw()
    for i in range(len(Spt)):
        Spt[i].draw()

#6
def snake_ubicacion():
    if(len(Spt)) > 1:
        for i in range(len(Spt)-1):
            Spt[len(Spt)-i-1].x = Spt[len(Spt)-i-2].x
            Spt[len(Spt) - i - 1].y = Spt[len(Spt) - i - 2].y

#7
def Colision():
    hit = False
    if (len(Spt)) > 1:
        
        for i in range(len(Spt) - 1):
            if Spt[0].x == Spt[i + 1].x and Spt[0].y == Spt[i + 1].y:
                
                hit = True
                
    return hit

#8
def main():
    global comida, Spt
    window = pygame.display.set_mode((400, 400))
    window.fill((0, 0, 0))
    pygame.display.set_caption("Juego de la Serpiente")
    Spt = [Cuerpo(window)]
    Spt[0].draw()
    comida = comida(window)
    redraw(window)
    run = True
    velocidad = 150
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    Spt[0].dir = 2
                if event.key == pygame.K_LEFT:
                    Spt[0].dir = 1
                if event.key == pygame.K_RIGHT:
                    Spt[0].dir = 0
                if event.key == pygame.K_UP:
                    Spt[0].dir = 3
        snake_ubicacion()
        Spt[0].movement()
        redraw(window)
        pygame.display.update()
        pygame.time.delay(velocidad)

        if Spt[0].x >= 400:
            Spt[0].x = 0
        elif Spt[0].x < 0:
            Spt[0].x = 390

        if Spt[0].y >= 400:
            Spt[0].y = 0
        elif Spt[0].y < 0:
            Spt[0].y = 390

        if Colision():
            
            Spt = [Cuerpo(window)]
            comida.relocate()
            velocidad = 100

        if Spt[0].x == comida.x and Spt[0].y == comida.y:
            if velocidad > 35:
                velocidad -= 5
            comida.relocate()
            Spt.append(Cuerpo(window))
            snake_ubicacion()


main()
pygame.quit()