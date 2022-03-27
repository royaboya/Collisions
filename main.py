import pygame, sys, pymunk
import constants
from helper import *


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Collision Testing")
        self.running = True
        self.window = pygame.display.set_mode((900, 900), 0, 32)

        self.space = pymunk.Space()
        self.space.gravity = (0, 300)
        self.objects = []
        self.floors = []  # 1 for now, maybe change to multiple lines

        self.clock = pygame.time.Clock()
        self.floor_position = (0, 0)  # find better solution to first click default

    def main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        self.objects.append(add_obj(self.space, x, y))
                    elif event.button == 3:
                        if len(self.floors) == 0:
                            self.floor_position = pygame.mouse.get_pos()
                            self.floors.append(
                                create_floor(
                                    self.space, self.window, self.floor_position
                                )
                            )

            pygame.display.update()
            self.window.fill("white")
            draw_obj(self.objects, self.window, constants.BLACK)  # draw pymunk objects
            draw_floor(self.floors, self.window, constants.RED, self.floor_position)
            self.space.step(1 / 60)
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    App().main()
