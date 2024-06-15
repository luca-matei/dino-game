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

        self.started = False
        self.current_step = "up"
        self.current_avatar = "idle_with_ground"
        self.step_fps_count = 0
        self.steps_per_second = 4

        self.y = settings.screen_h - self.h - settings.offset_bottom

        self.in_jump = False
        self.touched_top = False
        self.jump_height = 180

    def get_avatar(self):
        if not self.started:
            return self.idle_with_ground_img

        if self.in_jump:
            self.current_avatar = "idle"
            return self.idle_img

        elif self.started:
            self.current_avatar = "step"
            return self.get_step_img()

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

    def get_y(self):
        if self.in_jump:
            if not self.touched_top:
                self.y -= 10
                if self.y <= settings.screen_h - self.h - settings.offset_bottom - self.jump_height:
                    self.touched_top = True
            else:
                self.y += 10
                if self.y >= settings.screen_h - self.h - settings.offset_bottom:
                    self.in_jump = False
                    self.touched_top = False

        return self.y


dino = Dino()
