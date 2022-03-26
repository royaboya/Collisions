import pygame

pygame.init()
pygame.display.set_caption('Collision Testing')
window = pygame.display.set_mode((900,900), 0, 32)
clock = pygame.time.Clock()

while True:
    window.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    clock.tick(60)
