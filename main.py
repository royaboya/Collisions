import pygame, sys, pymunk
from helper import add_obj, draw_obj

pygame.init()
pygame.display.set_caption("Collision Testing")
window = pygame.display.set_mode((900, 900), 0, 32)
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 120)
objects = []

objects.append(add_obj(space, 200, 100))


def main():
    while True:
        window.fill((255, 255, 255))
        draw_obj(objects, window)
        space.step(1/40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
