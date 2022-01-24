"""
Идея камеры довольно проста.
Функция camera_configure получает персонажа, по его координатам вычисляет насколько нужно "сдвигать" отрисовку уровня
относительно героя так чтобы герой всегда оставался в центре экрана (кроме крайних случаев).
Например, если ширина окна 1200, а у героя X-координата 601, то все остальные блоки на уровне должны отрисоваться
по своей X-коордиинате-1 и затем нужно пересчитать координату самого персонажа, чтобы он тоже отрисовался в центре экрана.

camera_configure - вычисляет "сдвиг" для отрисовки изображения в окне.
Camera.apply - на основе полученного сдвига вычисляет координаты для отрисовки ОТДЕЛЬНОГО блока (изображение на экране
ведь состоит из блоков, в текущем коде наши блоки это кусочки изображений размером 8*8 пикселей)

Сходу понять всю логику происходящего сложновато, поэтому рекомендую просто знать что оно работает и не заморачиваться.
Разобраться с логикой можно будет и потом, после сдачи проекта.
"""

from pygame import Rect
from config import W, H


class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l = -target_rect.x + W/2
    t = -target_rect.y + H/2
    w, h = camera.width, camera.height

    l = min(0, l)
    l = max(-(w-W), l)
    t = max(-(h-H), t)
    t = min(0, t)

    return Rect(l, t, w, h)
