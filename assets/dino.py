import pygame

from assets.common import sprite_sheet
from config import settings


class Dino:
    def __init__(self):
        self.h: int = 94
        self.w: int = 88

        self.idle_with_ground_img = sprite_sheet.subsurface(76, 2, self.w, self.h)
        self.idle_img = sprite_sheet.subsurface(1678, 2, self.w, self.h)
        self.step_up_img = sprite_sheet.subsurface(1854, 2, self.w, self.h)
        self.step_down_img = sprite_sheet.subsurface(1942, 2, self.w, self.h)

        self.current_step = "up"
        self.step_fps_count = 0
        self.steps_per_second = 4

    def get_step_img(self):
        if self.step_fps_count < settings.fps / self.steps_per_second:
            self.step_fps_count += 1

            if self.current_step == "up":
                return self.step_up_img

            elif self.current_step == "down":
                return self.step_down_img
        else:
            self.step_fps_count = 0

            if self.current_step == "up":
                self.current_step = "down"
                return self.step_down_img

            elif self.current_step == "down":
                self.current_step = "up"
                return self.step_up_img


dino = Dino()
