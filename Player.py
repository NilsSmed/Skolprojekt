import pygame
import os


ALPHA = (255, 0, 0)
animation = 3
animation_attack = 1


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images_fwd = []
        self.images_rvs = []
        self.images_right = []
        self.images_left = []
        self.images_left_attack = []
        self.move_up = 0
        self.move_down = 0
        self.move_right = 0
        self.move_left = 0
        self.attack_left = 0
        self.frame = 0

        for i in range(1, 5):
            img = pygame.image.load(os.path.join("images", "Hero_fwd" + str(i) + ".gif"))
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images_fwd.append(img)
            self.image = self.images_fwd[0]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)  # experiment

        for i in range(1, 5):
            img = pygame.image.load(os.path.join("images", "Hero_rvs" + str(i) + ".gif"))
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images_rvs.append(img)
            self.image = self.images_rvs[0]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)  # experiment

        for i in range(1, 5):
            img = pygame.image.load(os.path.join("images", "Hero_right" + str(i) + ".gif"))
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images_right.append(img)
            self.image = self.images_right[0]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)  # experiment

        for i in range(1, 5):
            img = pygame.image.load(os.path.join("images", "Hero_left" + str(i) + ".gif"))
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images_left.append(img)
            self.image = self.images_left[0]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)  # experiment

        for i in range(1, 3):
            img = pygame.image.load(os.path.join("images", "Hero_left_attack" + str(i) + ".gif"))
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images_left_attack.append(img)
            self.image = self.images_left_attack[0]
            self.rect = self.image.get_rect()

    def control(self, x, y):
        self.move_up += y
        self.rect.y -= self.move_up
        self.move_down -= y
        self.rect.y += self.move_down
        self.move_right -= x
        self.rect.x += self.move_right
        self.move_left += x
        self.rect.x -= self.move_left
        self.attack_left = self.images_left_attack

        if self.attack_left is True:
            self.frame += 1
            if self.frame > 3*animation_attack:
                self.frame = 0
            self.image = self.images_left_attack[self.frame//animation]

        if self.move_up > 0:
            self.frame += 1
            if self.frame > 3*animation:
                self.frame = 0
            self.image = self.images_fwd[self.frame//animation]
        self.move_up -= y  # använder denna två gånger? samma sak med move_down.
        self.rect.y -= self.move_up

        if self.move_down > 0:
            self.frame += 1
            if self.frame > 3*animation:
                self.frame = 0
            self.image = self.images_rvs[self.frame//animation]
        self.move_down += y
        self.rect.y += self.move_down

        if self.move_right > 0:
            self.frame += 1
            if self.frame > 3*animation:
                self.frame = 0
            self.image = self.images_right[self.frame//animation]
        self.move_right += x
        self.rect.x += self.move_right

        if self.move_left > 0:
            self.frame += 1
            if self.frame > 3*animation:
                self.frame = 0
            self.image = self.images_left[self.frame//animation]
        self.move_left -= x
        self.rect.x -= self.move_left


def main():
    pass


if __name__ == "__main__":
    main()
