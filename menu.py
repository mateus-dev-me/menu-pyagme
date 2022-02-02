
import pygame


class Menu:
    def __init__(self, local):
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(local)

        self.sprite.rect = self.sprite.image.get_rect()


