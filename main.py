# import random
#
# import pygame, sys
#
# pygame.init()
# Screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()
#
# dt = clock.tick(60)/1000
#
# # background
# bg = pygame.image.load('Images/background.png').convert_alpha()
# bg = pygame.transform.scale(bg, (800, 800))
#
# # Ground
# whole_ground = pygame.Surface((2400, 28))
# ground = pygame.image.load('Images/Track.png')
# whole_ground.blit(ground, (0, 0))
# whole_ground.blit(ground, (800, 0))
# whole_ground.blit(ground, (1600, 0))
#
#
#
#
# # Dinosaur
# class Dinosaur(pygame.sprite.Sprite):
#     def __init__(self, group):
#         super().__init__(group)
#         self.vel_y = 0
#         self.jump = True
#
#         self.index = 0
#
#         self.animation_list = self.updating_images()
#         self.image = self.animation_list[self.index]
#         self.rect = self.image.get_rect(bottomleft=(200, 580))
#
#     # def colision(self):
#     #     for obstacle in obstacle_group:
#     #         if obstacle.rect.colliderect(self.rect):
#     #             self.jump = True
#
#
#
#
#     def move(self):
#         dy = 0
#         gravity = 0.8
#         key = pygame.key.get_pressed()
#
#         if key[pygame.K_SPACE] and self.jump == False:
#             self.index = 0
#             self.image = self.animation_list[self.index]
#             self.vel_y = -25
#             self.jump = True
#         else:
#             self.index += 1
#             self.image = self.animation_list[self.index]
#             if self.index >= 2:
#                 self.index = 0
#
#         self.vel_y += gravity
#         dy += self.vel_y
#
#         if self.rect.bottom + dy >= 580:
#             dy = 580 - self.rect.bottom
#             self.jump = False
#
#         self.rect.y += dy
#
#     def updating_images(self):
#         self.temp_list = []
#         self.image1 = pygame.image.load('Images/DinoJump.png').convert_alpha()
#         self.image2 = pygame.image.load('Images/DinoRun1.png').convert_alpha()
#         self.image3 = pygame.image.load('Images/DinoRun2.png').convert_alpha()
#
#         self.temp_list.append(self.image1)
#         self.temp_list.append(self.image2)
#         self.temp_list.append(self.image3)
#
#
#         return self.temp_list
#
#     def update(self):
#         self.move()
#         for obstacle in obstacle_group:
#             if obstacle.rect.colliderect(self.rect):
#                 obstacle.can_move = False
#
#
# class Obstacle(pygame.sprite.Sprite):
#     def __init__(self, group, pos):
#         super().__init__(group)
#         if random.randint(0, 6) == 2:
#             self.count = 3
#         if random.randint(0, 6) == 4:
#             self.count = 2
#         else:
#             self.count = 1
#
#         self.index = 0
#
#         self.animation_list = self.updating_images(self.count)
#         self.image = self.animation_list[self.index]
#
#         self.rect = self.image.get_rect(bottomleft=(pos, 580))
#
#         self.pos = pygame.math.Vector2(self.rect.topleft)
#         self.direction = pygame.math.Vector2(-1, 0)
#         self.speed = 300
#
#         self.can_move = True
#
#
#
#
#
#     def move(self):
#         if score.text >= 100:
#             self.speed = 350
#         if score.text >= 300:
#             self.speed = 500
#         if score.text >= 600:
#             self.speed = 600
#         self.pos += self.direction * self.speed * dt
#         self.rect.topleft = (round(self.pos.x), round(self.pos.y))
#
#     def updating_images(self, count):
#         self.image_list = []
#         self.image1 = pygame.image.load(f'Images/LargeCactus{count}.png').convert_alpha()
#         self.image2 = pygame.image.load(f'Images/SmallCactus{count}.png').convert_alpha()
#         self.image_list.append(self.image1)
#         self.image_list.append(self.image2)
#
#         return self.image_list
#
#
#     def update(self):
#         self.move()
#
#
# class Score:
#     def __init__(self):
#         super().__init__()
#         self.text = 0
#         self.font = pygame.font.Font('font/Pixeltype.ttf', size=50)
#
#     def display_score(self):
#         score_surf = self.font.render(f'Score: {self.text}', False, 'black')
#         score_rect = score_surf.get_rect(midleft=(300, 200))
#         Screen.blit(score_surf, score_rect)
#
#
#
# obstacle_group = pygame.sprite.Group()
# obstacle_timer = pygame.event.custom_type()
# pygame.time.set_timer(obstacle_timer, 200)
#
# dino_group = pygame.sprite.Group()
# dinosaur = Dinosaur(dino_group)
#
#
# score_timer = pygame.USEREVENT + 1
# pygame.time.set_timer(score_timer, 100)
# score = Score()
#
#
# shift = 0
# count = 1
# index = 0
#
# run = True
#
#
#
# while run:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == obstacle_timer:
#             obstacle_creation = random.randint(0, 8)
#             if obstacle_creation == 6:
#                 obstacle = Obstacle(obstacle_group, random.randint(900, 1500))
#                 obstacle_creation = random.randint(0, 8)
#
#         if event.type == score_timer:
#             score.text += 1
#
#     Screen.blit(bg, (0, 0))
#     Screen.blit(whole_ground, (0-shift, 570))
#     score.display_score()
#     shift += 1
#     if shift >= 1600:
#         shift = 0
#     for dinosaur in dino_group:
#         Screen.blit(dinosaur.image, dinosaur.rect)
#         dinosaur.update()
#     for obstacle in obstacle_group:
#         Screen.blit(obstacle.image, obstacle.rect)
#         obstacle.update()
#     pygame.display.update()
#     clock.tick(120)


# when we are offline and suddenly opens the chrome browser we'll get to see a game that's called Trex dianasour
# Have you ever tried to code that... No
# Let's give it a try with python or more specifically through pygame


# There are some steps in which we cover this game
# Step 1 the default setting of pyagme to get the popup screen
import pygame, sys

pygame.init()

clock = pygame.time.Clock()

Screen = pygame.display.set_mode((800, 600))

# bg
bg = pygame.image.load('Images/background.png').convert_alpha()
bg = pygame.transform.scale(bg, (800, 800))

# Ground

ground = pygame.Surface((2400, 28)).convert_alpha()
ground.fill('white')

track = pygame.image.load('Images/Track.png').convert_alpha()
track = pygame.transform.scale(track, (800, 28))


ground.blit(track, (0, 0))
ground.blit(track, (800, 0))
ground.blit(track, (1600, 0))


class Dinasaur(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load("Images/DinoJump.png").convert_alpha()
        self.rect = self.image.get_rect(midleft=(50, 535))

        self.index = 0

        self.list = self.updating_animation()
        self.animation = self.list[self.index]

        self.vel_y = 0

        



    def move(self):
        dy = 0
        gravity = 2
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            self.vel_y = -30
            self.index = 1
            self.animation = self.list[self.index]

        self.vel_y += gravity
        dy += self.vel_y

        if self.rect.bottom + dy >= 580:
            dy = 580 - self.rect.bottom

        self.rect.y += dy

        if self.rect.bottom





    def updating_animation(self):
        self.animation_list = []

        self.image1 = pygame.image.load("Images/DinoJump.png").convert_alpha()
        self.image2 = pygame.image.load("Images/DinoRun1.png").convert_alpha()
        self.image3 = pygame.image.load("Images/DinoRun2.png").convert_alpha()

        self.animation_list.append(self.image1)
        self.animation_list.append(self.image2)
        self.animation_list.append(self.image3)

        return self.animation_list

    def update(self):
        self.move()



dino_group = pygame.sprite.Group()
dino = Dinasaur(dino_group)


shift = 0

run = True
while run:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    Screen.blit(bg, (0, 0))
    Screen.blit(ground, (0-shift, 570))

    for dino in dino_group:
        Screen.blit(dino.image, dino.rect)
        dino.update()

    shift += 1

    if shift >= 1600:
        shift = 0



    pygame.display.update()
    clock.tick(120)





























