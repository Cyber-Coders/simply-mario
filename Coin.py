import pygame
import config


# Класс для отображеня монет и взаимодействия с ними
class Coin:
    def __init__(self, position):
        # Отрисовка монеты
        self.count = 0
        self.image = pygame.Surface((25, 34))
        pygame.draw.circle(
            self.image,
            (255, 255, 0),
            (self.image.get_width() // 2, self.image.get_height() // 2),
            self.image.get_width() // 2)
        self.image.set_colorkey((0, 0, 0))

        # Применение положения относительно карты
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

        pygame.mixer.music.load("data/sounds/sound_coin.mp3")

    # Проверка совпадений координат персонажа и монеты
    def check(self, position):
        if position[0] == self.rect.x and (position[1] == 606 or position[1] == 607) and self.count == 0:
            self.image.fill((0, 0, 0))
            config.score += 50
            self.count = 1
            pygame.mixer.music.play(1)