import pygame

from config import settings
from assets import bg, dino

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((settings.screen_w, settings.screen_h))
clock = pygame.time.Clock()
pygame.display.set_caption(settings.app_name)

start = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            start = True

    # Fill the screen with white color
    screen.fill("#ffffff")

    # Draw the background
    if start:
        for i in range(bg.tiles):
            screen.blit(bg.img, (i * bg.w + bg.scroll, settings.screen_h - bg.h - 100))

        bg.scroll -= bg.scroll_speed
        if bg.scroll <= -bg.w:
            bg.scroll = 0

        # Draw the dino
        screen.blit(dino.get_step_img(), (100, settings.screen_h - dino.h - 100))

    else:
        screen.blit(dino.idle_with_ground_img, (100, settings.screen_h - dino.h - 100))

    # Update the display
    pygame.display.flip()
    clock.tick(settings.fps)

# Quit the game
pygame.quit()
