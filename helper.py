import pygame, pymunk

def add_obj(space: pymunk.Space, x: int, y: int):
    obj = pymunk.Body(10, 50, body_type=pymunk.Body.DYNAMIC)
    obj.position = (x, y)
    obj_shape = pymunk.Circle(obj, 50)
    
    space.add(obj, obj_shape)
    return obj_shape

def draw_obj(objects: list, window: pygame.display):
    for object in objects:
        x = int(object.body.position.x)
        y = int(object.body.position.y)
        pygame.draw.circle(window, (0,0,0), (x, y), 50)
        
