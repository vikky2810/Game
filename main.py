import pygame

pygame.init()

# Game Loop for contineous display..
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen = pygame.display.set_mode((400,400))

pygame.quit()
        