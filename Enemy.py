import pygame
import os

ALPHA = (255, 0, 0)


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        self.image_monster = pygame.image.load(os.path.join("images", "monster.png"))
        self.image_monster.convert_alpha()
        self.image_monster.set_colorkey(ALPHA)
        self.image = self.image_monster
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #self.move_x
        #self.move_y


def main():
    pass


if __name__ == "__main__":
    main()
