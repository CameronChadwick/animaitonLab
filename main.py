import math
import pygame

# color constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (0, 94, 255)
GREY = (50, 54, 61)
ORANGE = (255, 106, 0)
LIGHT_GREY = (107, 107, 107)

# math constants
PI = math.pi

# game constants
SIZE = (800, 800)
FPS = 60

##########################################################################
cloud_x = 625
cloud_x2 = 325
cloudx_velo = 3.5
cloudy_velo = 0.5
cloud_y = 100


pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pygame Picture")

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        # check for user input
        if event.type == pygame.QUIT:
            running = False

    # game logic
    if cloud_x - 30 > 800:
        cloud_x = -100

    if cloud_x2 - 30 > 800:
            cloud_x2 = -100

    if cloud_y > 125:
        cloudy_velo *= -1

    if cloud_y < 75:
        cloudy_velo *= -1

    screen.fill(SKY_BLUE)

    # drawings

    # cloud function
    def cloud(cloud_x, cloud_y):
        pygame.draw.ellipse(screen, WHITE, [cloud_x, cloud_y, 60, 50])
        pygame.draw.ellipse(screen, WHITE, [cloud_x + 20, cloud_y - 15, 60, 50])
        pygame.draw.ellipse(screen, WHITE, [cloud_x - 20, cloud_y + 15, 60, 50])
        pygame.draw.ellipse(screen, WHITE, [cloud_x + 15, cloud_y + 15, 60, 50])
        pygame.draw.ellipse(screen, WHITE, [cloud_x - 25, cloud_y + 20, 60, 50])

    # ground and volcano
    pygame.draw.rect(screen, [18, 117, 18], [0, 650, 800, 150])
    pygame.draw.rect(screen, GREY, [350, 200, 100, 450])
    pygame.draw.polygon(screen, GREY, [(125, 650), (350, 200), (350, 650)])
    pygame.draw.polygon(screen, GREY, [(350, 650), (450, 200), (675, 650)])

    # lava flows and pools
    pygame.draw.line(screen, ORANGE, [440, 200], [615, 650], width=10)
    pygame.draw.line(screen, ORANGE, [350, 200], [125, 650], width=10)
    pygame.draw.line(screen, ORANGE, [440, 200], [400, 650], width=10)
    pygame.draw.line(screen, ORANGE, [410, 200], [200, 650], width=10)
    pygame.draw.circle(screen, ORANGE, [200, 700], 60)
    pygame.draw.circle(screen, ORANGE, [125, 700], 60)
    pygame.draw.circle(screen, ORANGE, [160, 700], 60)
    pygame.draw.circle(screen, ORANGE, [615, 700], 60)
    pygame.draw.circle(screen, ORANGE, [400, 700], 60)
    pygame.draw.circle(screen, ORANGE, [410, 700], 60)
    pygame.draw.circle(screen, ORANGE, [410, 710], 60)
    pygame.draw.circle(screen, ORANGE, [605, 710], 60)
    pygame.draw.circle(screen, ORANGE, [595, 700], 60)
    pygame.draw.ellipse(screen, ORANGE, [350, 170, 100, 65])
    pygame.draw.rect(screen, SKY_BLUE, [350, 150, 100, 50])

    # clouds
    cloud(cloud_x, cloud_y)
    cloud(cloud_x2, cloud_y - 50)
    cloud_x += cloudx_velo
    cloud_x2 += cloudx_velo - 1
    cloud_y += cloudy_velo

    # lava smoke
    pygame.draw.circle(screen, LIGHT_GREY, [400, 175], 40)
    pygame.draw.circle(screen, LIGHT_GREY, [375, 175], 40)
    pygame.draw.circle(screen, LIGHT_GREY, [340, 135], 40)
    pygame.draw.circle(screen, LIGHT_GREY, [315, 100], 40)
    pygame.draw.circle(screen, LIGHT_GREY, [275, 75], 40)
    pygame.draw.circle(screen, LIGHT_GREY, [240, 40], 40)
    pygame.draw.circle(screen, LIGHT_GREY, [190, 10], 40)

    pygame.display.flip()

    clock.tick(FPS)

# quit
pygame.quit()
