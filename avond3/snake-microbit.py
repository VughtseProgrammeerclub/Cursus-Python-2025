import pygame, random, sys
from pygame.locals import *
from kaspersmicrobit import KaspersMicrobit
from kaspersmicrobit.services.accelerometer import AccelerometerData
from kaspersmicrobit.services.buttons import ButtonState

# Functie om te bepalen of een rechthoekig object met afmeting w1, h1 op
# locatie x1, y1 een object met afmeting w2, h2 op locatie x2, y2 raakt 
def collide(x1, x2, y1, y2, w1, w2, h1, h2):
    return x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2

# Game Over functie die de eindscore laat zien en na 2 seconden het spel afsluit
def game_over(screen, score):
    font = pygame.font.SysFont('Arial', 30);
    text = font.render(f'Your score was: {score}', True, (0, 0, 0))
    screen.blit(text, (10, 270))
    pygame.display.update()
    pygame.time.wait(2000)
    sys.exit(0)

ACCEL_EVENT: int = pygame.event.custom_type()

def post_accelerometer_event(data:AccelerometerData):
    event_dict: dict = {"x": data.x / 1000, "y": data.y / 1000}
    pygame.event.post(pygame.event.Event(ACCEL_EVENT, event_dict))

pygame.init()
snake_segments_x = [290, 290, 290, 290, 290]
snake_segments_y = [290, 270, 250, 230, 210]
direction = 0
score = 0
applepos = (random.randint(0, 590), random.randint(0, 590))
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

appleimage = pygame.Surface((10, 10))
appleimage.fill((0, 255, 0))

snakeimage = pygame.Surface((20, 20))
snakeimage.fill((255, 0, 0))

font = pygame.font.SysFont('Arial', 20)
clock = pygame.time.Clock()

with KaspersMicrobit.find_one_microbit() as microbit:
    microbit.accelerometer.notify(post_accelerometer_event)
    
    while True:
        clock.tick(10)
        
        # Controleer events, zoals welke knoppen ingedrukt zijn
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)
            elif e.type == KEYDOWN:
                if e.key == K_UP and direction != 0:
                    direction = 2
                elif e.key == K_DOWN and direction != 2:
                    direction = 0
                elif e.key == K_LEFT and direction != 1:
                    direction = 3
                elif e.key == K_RIGHT and direction != 3:
                    direction = 1
            elif e.type == ACCEL_EVENT:
                if e.__dict__["x"] < -.75:
                    direction = 3
                elif e.__dict__["x"] > .75:
                    direction = 1
                elif e.__dict__["y"] < -.75:
                    direction = 2
                elif e.__dict__["y"] > .75:
                    direction = 0
        
        # Kijk of het hoofd van de slang de slang zelf raakt
        i = len(snake_segments_x) - 1
        while i >= 2:
            if collide(snake_segments_x[0], snake_segments_x[i], snake_segments_y[0], snake_segments_y[i], 20, 20, 20, 20):
                game_over(screen, score)
            i -= 1
        
        # Kijk of het hoofd van de slang de appel raakt
        if collide(snake_segments_x[0], applepos[0], snake_segments_y[0], applepos[1], 20, 10, 20, 10):
            score += 1
            snake_segments_x.append(700)
            snake_segments_y.append(700)
            applepos = (random.randint(0,590),random.randint(0,590))
            
        # Kijk of het hoofd van de slang de rand raakt 
        if snake_segments_x[0] < 0 or snake_segments_x[0] > 580 or snake_segments_y[0] < 0 or snake_segments_y[0] > 580:
            game_over(screen, score)
        
        # Verplaats de slang
        i = len(snake_segments_x) - 1
        while i >= 1:
            snake_segments_x[i] = snake_segments_x[i-1]
            snake_segments_y[i] = snake_segments_y[i-1]
            i -= 1
        
        if direction == 0:
            snake_segments_y[0] += 20
        elif direction == 1:
            snake_segments_x[0] += 20
        elif direction == 2:
            snake_segments_y[0] -= 20
        elif direction == 3:
            snake_segments_x[0] -= 20
        
        # Scherm leeg maken en alles tekenen
        screen.fill((255, 255, 255))    
        for i in range(0, len(snake_segments_x)):
            screen.blit(snakeimage, (snake_segments_x[i], snake_segments_y[i]))
        
        screen.blit(appleimage, applepos)
        
        text = font.render(str(score), True, (0, 0, 0))
        screen.blit(text, (10, 10))
        
        pygame.display.update()

