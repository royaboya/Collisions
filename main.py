import pygame, sys, pymunk
from helper import add_obj, draw_obj



class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Collision Testing")

        self.window = pygame.display.set_mode((900, 900), 0, 32)
        self.space = pymunk.Space()
        self.space.gravity = (0, 300)
        self.objects = []
        self.running = True
        self.clock = pygame.time.Clock()

    def main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    self.objects.append(add_obj(self.space, x, y))
            pygame.display.update()
            # self.window.fill(255,255,255)
            self.window.fill("white")
            draw_obj(self.objects, self.window)
            self.space.step(1/60)
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

# def main():
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 x = pygame.mouse.get_pos()[0]
#                 y = pygame.mouse.get_pos()[1]
#                 objects.append(add_obj(space, x, y))

#         pygame.display.update()
#         window.fill((255, 255, 255))
#         draw_obj(objects, window)
#         space.step(1/60)
#         clock.tick(60)


if __name__ == "__main__":
    App().main()
