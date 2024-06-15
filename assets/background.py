import pygame

from assets.common import sprite_sheet


class Background:
    def __init__(self):
        original_w: int = 2400
        original_h: int = 25
        aspect_ratio: float = original_w / original_h

        self.h: int = 25
        self.w: int = int(self.h * aspect_ratio)
        self.scroll = 0
        self.scroll_speed = 10
        self.tiles = 2

        img = sprite_sheet.subsurface(2, 104, original_w, original_h)
        img = pygame.transform.scale(img, (self.w, self.h))

        self.img = img


bg = Background()
