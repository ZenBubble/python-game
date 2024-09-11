import pygame

pygame.init

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PLR_WIDTH = 50
PLR_HEIGHT = 50
MISL_SIZE = 10
MISL_SPEED = 2

missles = []

running = True

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLR_HEIGHT, PLR_WIDTH))

def handleMovement():
    ## basic movement x and y
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-1,0)
    if key[pygame.K_d]:
        player.move_ip(1,0)
    if key[pygame.K_w]:
        player.move_ip(0,-1)
    if key[pygame.K_s]:
        player.move_ip(0,1)
    ## handles going out of bound
    if player.x < 0:
        player.x = 0
    if player.y < 0:
        player.y = 0
    if player.x > SCREEN_WIDTH - PLR_WIDTH:
        player.x = SCREEN_WIDTH - PLR_WIDTH
    if player.y > SCREEN_HEIGHT - PLR_HEIGHT:
        player.y = SCREEN_HEIGHT - PLR_HEIGHT

def shootMissle():
    ## sets the velocity of the bullet to MISL_SPEED in the direction of mouse button
    targ = pygame.mouse.get_pos()
    dx = targ[0] - player.x
    dy = targ[1] - player.y
    speed = (dx**2 + dy**2)**(1/2)
    ideal = speed / MISL_SPEED
    dx = dx/ideal
    dy = dy/ideal
    ## adds missle to list
    missles.append([player.x, player.y, dx, dy])

def updateMissles():
    ## goes throguh each missle in list and draws them and updates their position for next iteration
    for pos in missles:
        if (pos[0] > SCREEN_WIDTH or pos[0] < 0 or pos[1] < 0 or pos[1] > SCREEN_HEIGHT):
            missles.remove(pos)
        else:
            pygame.draw.circle(screen, (255,0,0), (pos[0],pos[1]), MISL_SIZE)
            pos[0] += pos[2]
            pos[1] += pos[3]
            

while running:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), player)
    handleMovement()
    updateMissles()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            shootMissle()
    pygame.display.update()

pygame.quit()
