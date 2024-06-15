import pygame

from config import settings
from assets.background import bg

screen_w = 1280
screen_h = 720

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()
pygame.display.set_caption(settings.app_name)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white color
    screen.fill("#ffffff")

    # Draw the background
    for i in range(bg.tiles):
        screen.blit(bg.img, (i * bg.w + bg.scroll, screen_h - bg.h - 100))

    bg.scroll -= bg.scroll_speed
    if bg.scroll <= -bg.w:
        bg.scroll = 0

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
