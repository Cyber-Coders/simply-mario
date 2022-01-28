import pygame
import config


# Класс для отображения монет и взаимодействия с ними
class Coin:
    def __init__(self, position):
        # Отрисовка монеты
        self.count = 0
        icon = pygame.image.load('data/sprites/coin/animation_1.png')
        self.image = pygame.Surface((25, 27))
        self.image.blit(icon, (0, 0))
        self.image.set_colorkey((0, 0, 0))

        # Применение положения относительно карты
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

        pygame.mixer.music.load("data/sounds/sound_coin.mp3")

    # Проверка совпадений координат персонажа и монеты
    def check(self, position):
        if position[0] == self.rect.x and (position[1] == 606 or position[1] == 607) and self.count == 0:
            self.image.fill((0, 0, 0))
            config.score += 5
            self.count = 1
            pygame.mixer.music.play(1)