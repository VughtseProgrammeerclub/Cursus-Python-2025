import sys, pygame
pygame.init()

size = width, height = 800, 600
speed = [4, 4]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

logo = pygame.image.load("dvdlogo0.png")
logorect = logo.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    logorect = logorect.move(speed)
    if logorect.left < 0 or logorect.right > width:
        speed[0] = -speed[0]
    if logorect.top < 0 or logorect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(logo, logorect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

