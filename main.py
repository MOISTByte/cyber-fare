# imports
import pygame
from pygame import locals
# initialise screen
pygame.init()
screen = pygame.display.set_mode((150, 50))
pygame.display.set_caption("Hi")
# add background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 250))
# text
font = pygame.font.Font(None, 36)
text = font.render("Hello, World!", 1, (10,10, 10))
text_position = text.get_rect()
text_position.centerx = background.get_rect().centerx
background.blit(text, text_position)
# loop + render + fps limit
clock = pygame.time.Clock()
while True:
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()

        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(60)
