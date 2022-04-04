import pygame, pymunk


def add_obj(space: pymunk.Space, x: int, y: int):
    obj = pymunk.Body(10, 50, body_type=pymunk.Body.DYNAMIC)
    obj.position = (x, y)
    obj_shape = pymunk.Circle(obj, 50)
    obj_shape.elasticity = 1

    space.add(obj, obj_shape)
    return obj_shape


# better alternative to a rectangle box using poly is segment
def create_floor(space: pymunk.Space, window: pygame.display, mouse_pos: tuple):
    # TOFIX
    floor_obj = pymunk.Body(10, 10, body_type=pymunk.Body.STATIC)
    width = window.get_width()
    height = window.get_height()

    mY = mouse_pos[1]
    floor_shape = pymunk.Poly(
        floor_obj, vertices=[(0, mY), (width, mY), (0, height), (width, height)]
    )
    floor_shape.elasticity = 0.7
    space.add(floor_obj, floor_shape)

    return floor_shape


def create_segment(body: pymunk.Body, p1: tuple, p2: tuple):
    pass
