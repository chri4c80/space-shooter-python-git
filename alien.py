import pygame as pg
class Alien:
    
    def __init__(self, x, y, vel=2, hitpoints=1):
        self.x = x
        self.y = y
        self.vel = vel
        self.hp = hitpoints
        self.images = []
        self.draw_tick = 0

        for i in range(2):
            img = pg.image.load(f"images/alien_{i}.png")
            self.images.append(img)
        self.w = self.images[0].get_rect().size[0]
        self.h = self.images[0].get_rect().size[1]

    def move(self):
        self.x += 0 
        self.y += 0 

    def draw(self, screen):
        r = int((self.draw_tick/8) % 2 )
        screen.blit(self.images[r], (self.x, self.y))
        self.draw_tick += 1