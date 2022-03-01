import pygame
import random
import csv
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

bg = pygame.image.load('bg.jpg')

global kills
kills = 0

global kills_lst
kills_lst = [0]

class Player(pygame.sprite.Sprite):
    right = True

    def __init__(self):
        super().__init__()

        elf = Elf()

        self.win_doing = False

        self.walking = False

        self.attack_doing = False

        self.death_doing = False

        self.enemy_life = False

        self.index_walking = 0

        self.index = 0

        self.index_death = 0

        self.secundes = 100

        self.cd = 0

        self.image = pygame.image.load('Skeleton_Warrior_Stay.png')

        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0

        self.at_k = pygame.Surface((42, 86))

        self.images_attack = []

        self.images_attack.append(pygame.image.load('images_attack_____right/1.png'))
        self.images_attack.append(pygame.image.load('images_attack_____right/2.png'))
        self.images_attack.append(pygame.image.load('images_attack_____right/3.png'))
        self.images_attack.append(pygame.image.load('images_attack_____right/4.png'))
        self.images_attack.append(pygame.image.load('images_attack_____right/5.png'))
        self.images_attack.append(pygame.image.load('images_attack_____right/6.png'))
        self.images_attack.append(pygame.image.load('images_attack_____right/7.png'))
        self.images_attack.append(pygame.image.load('images_attack_____right/8.png'))

        self.images_attack_left = []

        self.images_attack_left.append(pygame.image.load('images_attack_____left/1.png'))
        self.images_attack_left.append(pygame.image.load('images_attack_____left/2.png'))
        self.images_attack_left.append(pygame.image.load('images_attack_____left/3.png'))
        self.images_attack_left.append(pygame.image.load('images_attack_____left/4.png'))
        self.images_attack_left.append(pygame.image.load('images_attack_____left/5.png'))
        self.images_attack_left.append(pygame.image.load('images_attack_____left/6.png'))
        self.images_attack_left.append(pygame.image.load('images_attack_____left/7.png'))
        self.images_attack_left.append(pygame.image.load('images_attack_____left/8.png'))

        self.images_walk = []

        self.images_walk.append(pygame.image.load('images_walk/1.png'))
        self.images_walk.append(pygame.image.load('images_walk/2.png'))
        self.images_walk.append(pygame.image.load('images_walk/3.png'))
        self.images_walk.append(pygame.image.load('images_walk/4.png'))
        self.images_walk.append(pygame.image.load('images_walk/5.png'))
        self.images_walk.append(pygame.image.load('images_walk/6.png'))
        self.images_walk.append(pygame.image.load('images_walk/7.png'))
        self.images_walk.append(pygame.image.load('images_walk/8.png'))
        self.images_walk.append(pygame.image.load('images_walk/9.png'))
        self.images_walk.append(pygame.image.load('images_walk/10.png'))
        self.images_walk.append(pygame.image.load('images_walk/11.png'))
        self.images_walk.append(pygame.image.load('images_walk/12.png'))

        self.images_walk_left = []

        self.images_walk_left.append(pygame.image.load('images_walk_left/1.png'))
        self.images_walk_left.append(pygame.image.load('images_walk_left/2.png'))
        self.images_walk_left.append(pygame.image.load('images_walk_left/3.png'))
        self.images_walk_left.append(pygame.image.load('images_walk_left/4.png'))
        self.images_walk_left.append(pygame.image.load('images_walk_left/5.png'))
        self.images_walk_left.append(pygame.image.load('images_walk_left/6.png'))
        self.images_walk_left.append(pygame.image.load('images_walk_left/7.png'))
        self.images_walk_left.append(pygame.image.load('images_walk_left/8.png'))
        self.images_walk_left.append(pygame.image.load('images_walk_left/9.png'))
        self.images_walk_left.append(pygame.image.load('images_walk_left/10.png'))
        self.images_walk_left.append(pygame.image.load('images_walk_left/11.png'))
        self.images_walk_left.append(pygame.image.load('images_walk_left/12.png'))

        self.images_death = []

        self.images_death.append(pygame.image.load('images_death/1.png'))
        self.images_death.append(pygame.image.load('images_death/2.png'))
        self.images_death.append(pygame.image.load('images_death/3.png'))
        self.images_death.append(pygame.image.load('images_death/4.png'))
        self.images_death.append(pygame.image.load('images_death/5.png'))
        self.images_death.append(pygame.image.load('images_death/6.png'))

        self.images_death_left = []

        self.images_death_left.append(pygame.image.load('images_death_left/1.png'))
        self.images_death_left.append(pygame.image.load('images_death_left/2.png'))
        self.images_death_left.append(pygame.image.load('images_death_left/3.png'))
        self.images_death_left.append(pygame.image.load('images_death_left/4.png'))
        self.images_death_left.append(pygame.image.load('images_death_left/5.png'))
        self.images_death_left.append(pygame.image.load('images_death_left/6.png'))

        self.enemy_list = pygame.sprite.Sprite

        mob = Elf()
        self.enemy_list.add(mob)

    def update(self):
        global kills
        if self.secundes <= 0:
            end_screen()
        self.cd += 1
        self.gravity()
        self.secundes -= 1

        self.rect.x += self.change_x

        if not self.enemy_life:
            if kills <= kills_lst[-1]:
                self.enemy()

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            self.change_y = 0

        if self.attack_doing:
            elf = Elf()
            pl = Player()
            hit = pygame.sprite.collide_rect(elf, pl)
            if hit:
                kills += 0.125
                kills_lst.append(kills)
                self.secundes = 100
                self.enemy()
                self.enemy_life = False

            if self.right:
                self.image = self.images_attack[self.index]
                self.cd = 0
                self.index += 1
                if self.index >= len(self.images_attack):
                    self.index = 0
                    self.attack_doing = False
                    self.image = pygame.image.load('Skeleton_Warrior_Stay.png')
            else:
                self.image = self.images_attack_left[self.index]
                self.cd = 0
                self.index += 1
                if self.index >= len(self.images_attack):
                    self.index = 0
                    self.attack_doing = False
                    self.image = pygame.image.load('Skeleton_Warrior_Stay_left.png')

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
            if self.right:
                self.image = self.images_walk[self.index_walking]
                self.index_walking += 1
                if self.index_walking >= len(self.images_walk):
                    self.index_walking = 0
                    self.image = pygame.image.load('Skeleton_Warrior_Stay.png')
            else:
                self.image = self.images_walk_left[self.index_walking]
                self.index_walking += 1
                if self.index_walking >= len(self.images_walk_left):
                    self.index_walking = 0
                    self.walking = False
                    self.image = pygame.image.load('Skeleton_Warrior_Stay_left.png')

        if self.death_doing:
            if self.right:
                self.image = self.images_death[self.index_death]
                self.cd = 0
                self.index_death += 1
                if self.index_death >= len(self.images_death):
                    self.index_death = 0
                    self.death_doing = False
            else:
                self.image = self.images_death_left[self.index_death]
                self.cd = 0
                self.index_death += 1
                if self.index >= len(self.images_death_left):
                    self.index_death = 0
                    self.death_doing = False

    def gravity(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.95

        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        self.rect.y += 10
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 10

        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -16

    def go_left(self):
        self.walking = True
        self.change_x = -9
        if self.right:
            self.flip()
            self.right = False

    def go_right(self):
        self.walking = True
        self.change_x = 9
        if not self.right:
            self.flip()
            self.right = True

    def stop(self):
        self.change_x = 0

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def attack(self):
        if self.cd >= 20:
            self.attack_doing = True

    def death(self):
        if self.right:
            self.image = pygame.image.load(self.index_death)
        else:
            self.image = pygame.image.load(self.index_death)

    def enemy(self):
        elf = Elf()
        lst = [1, 2, 3, 4]
        nomer = random.choice(lst)
        if nomer == 1:
            elf.rect.x = 200
            elf.rect.y = 319
            self.enemy_life = True
        elif nomer == 2:
            elf.rect.x = 600
            elf.rect.y = 419
            self.enemy_life = True
        elif nomer == 3:
            elf.rect.x = 0
            elf.rect.y = 519
            self.enemy_life = True
        elif nomer == 4:
            elf.rect.x = 300
            elf.rect.y = 319
            self.enemy_life = True


def start_screen():
    screen_size = (800, 600)
    screen_st = pygame.display.set_mode(screen_size)
    fon = pygame.image.load('fon.png')
    screen_st.blit(fon, (0, 0))
    pygame.display.update()

    button = pygame.Rect(350, 250, 100, 100)
    img = pygame.image.load('start.png')

    bt_rect = (350, 250, 100, 100)
    screen_st.blit(img, bt_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                    return


def end_screen():
    screen_size = (800, 600)
    screen_st = pygame.display.set_mode(screen_size)
    fon = pygame.image.load('fon.png')
    screen_st.blit(fon, (0, 0))
    stroka = 'Вам удалось уничтожить: ' + str(int(round(kills))) + ' ненавистных эльфов!'
    pygame.display.set_caption(stroka)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()


def terminate():
    pygame.quit()
    sys.exit()


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.image.load('platform.png')

        self.rect = self.image.get_rect()


class Elf(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Wood_Elf_Stay.png').convert()

        self.rect = self.image.get_rect()


class Level(object):
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()

        self.player = player

    def update(self):
        self.platform_list.update()

    def draw(self, screen):
        screen.blit(bg, (0, 0))

        self.platform_list.draw(screen)


class Level_01(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        level = [[210, 32, 500, 500], [210, 32, 200, 400]]

        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)


def main():
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    start_screen()

    pygame.init()

    with open("gg.csv", 'r', encoding='utf-8', newline='') as csvfile:
        file = csv.reader(csvfile)
        rows = []
        for row in file:
            rows.append(row)

    pygame.display.set_caption(row[0])

    player = Player()

    elf = Elf()

    level_list = []
    level_list.append(Level_01(player))

    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height

    elf.rect.x = 200
    elf.rect.y = 319

    active_sprite_list.add(player)
    active_sprite_list.add(elf)

    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_SPACE:
                    player.attack()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        active_sprite_list.update()

        current_level.update()

        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH

        if player.rect.left < 0:
            player.rect.left = 0

        current_level.draw(screen)
        active_sprite_list.draw(screen)

        clock.tick(25)

        pygame.display.flip()

    end_screen()
    print(player.kills)


if __name__ == "__main__":
    main()
