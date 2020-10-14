import pygame
import os
from Player import Player
from Enemyclass import Enemy


SCR_WIDTH = 1600
SCR_HEIGHT = 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ALPHA = (255, 0, 0)
fps = 30
animation = 9
world = pygame.display.set_mode([SCR_WIDTH, SCR_HEIGHT])


class Walls(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        self.image_walls = pygame.image.load(os.path.join("images", "walls.png"))
        self.image_walls.convert_alpha()
        self.image_walls.set_colorkey(ALPHA)
        self.image = self.image_walls
        self.rect = self.image.get_rect()
        self.rect_x = x
        self.rect_y = y
        self.mask = pygame.mask.from_surface(self.image)  # experiment


def main():
    pygame.init()
    background = pygame.image.load(os.path.join("images", "background.jpg"))
    background = pygame.transform.scale(background, (SCR_WIDTH, SCR_HEIGHT))
    clock = pygame.time.Clock()
    bgbox = world.get_rect()
    player = Player()
    enemy = Enemy(512, 300)
    walls = Walls(0, 0)
    player.rect.x = 1400
    player.rect.y = 180
    enemy.rect.x = 512
    enemy.rect.y = 300
    walls.rect.x = 0
    walls.rect.y = 0
    player_list = pygame.sprite.Group(player)
    player_list.add(player)
    enemy_list = pygame.sprite.Group(enemy)
    enemy_list.add(enemy)
    walls_list = pygame.sprite.Group(walls)
    walls_list.add(walls)
    steps_x = 2
    steps_y = 2
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        button_pressed = pygame.key.get_pressed()  # ändra till keyup och keydown?
        if button_pressed[pygame.K_UP]:
            player.rect.y -= 1
            player.control(0, steps_y)
            if pygame.sprite.groupcollide(player_list, walls_list, False, False, pygame.sprite.collide_mask):
                player.rect.y += 5
        if button_pressed[pygame.K_DOWN]:
            player.rect.y += 1
            player.control(0, -steps_y)
            if pygame.sprite.spritecollideany(player, walls_list, pygame.sprite.collide_mask):
                player.rect.y -= 5
        if button_pressed[pygame.K_RIGHT]:
            player.rect.x += 1
            player.control(-steps_x, 0)
            if pygame.sprite.spritecollideany(player, walls_list, pygame.sprite.collide_mask):
                player.rect.x -= 5
        if button_pressed[pygame.K_LEFT]:
            player.rect.x -= 1
            player.control(steps_x, 0)
            if pygame.sprite.spritecollideany(player, walls_list, pygame.sprite.collide_mask):
                player.rect.x += 5
        #if pygame.sprite.spritecollide(sprite=player, dokill=True, group=enemy_list):
            #print("Collide")
        if button_pressed[pygame.K_SPACE]:
            player.attack_left = True
            player.control(player.rect.x, player.rect.y)

        walls_list.update()
        walls_list.draw(world)

        world.blit(background, bgbox)

        player_list.update()
        player_list.draw(world)

        enemy_list.update()
        enemy_list.draw(world)

        pygame.display.update()
        clock.tick(fps)

if __name__ == "__main__":
    main()
