import pygame, pymunk


def draw_obj(objects: list, window: pygame.display, color: tuple):
    for object in objects:
        x = int(object.body.position.x)
        y = int(object.body.position.y)
        pygame.draw.circle(window, color, (x, y), 50)


def draw_floor(floors: list, window: pygame.display, color: tuple, c_mouse_pos: tuple):
    for floor in floors:  # bad loop
        width = window.get_width()
        mouse_y = c_mouse_pos[1]
        box = pygame.Rect((0, mouse_y), (width, mouse_y))
        pygame.draw.rect(window, color, box)


def draw_segment():
    pass
