"""
(C) CyberCoders, 2022
Gadzhimuradov M.
"""

# Импорт библиотек и модулей
from pygame import Rect
from config import W, H


# Вычисляет сдвиг для отрисовки изображения в окне
def camera_configure(camera, target_rect):
    l = -target_rect.x + W / 2
    t = -target_rect.y + H / 2
    w, h = camera.width, camera.height

    l = min(0, l)
    l = max(-(w - W), l)
    t = max(-(h - H), t)
    t = min(0, t)

    return Rect(l, t, w, h)

# На основе полученного сдвига вычисляет координаты для отрисовки отдельного блока
class Camera:
    def __init__(self, width, height):
        # Применяем переданные значения для констант
        self.width, self.height = width, height
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = camera_configure(self.state, target.rect)
