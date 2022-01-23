'''
Набор платформ типа:
 - Floor - пол (это на который ногами вставать будем),
 - FloorBottom - пол снизу (это нижняя часть платформы, об неё головой будем биться)
 - Sky - пустое пространство с которым персонаж ни как не взаимодействует, свободно проходит и пролетает через него
 - Other - любые другие блоки, я сделал этот тип платформы для обработки "земли" внутри "пола", потому что Floor
 и FloorBottom будут обрабатывать только верхний и нижний слой "земляной платформы", а средний слой тоже надо обрабатывать.
 Средний слой можно было оставить как Sky, всё равно персонаж с ним тоже не взаимодейтсвует, но я всё же решил сделать
 средний кусок платформы отдельным классом, чтобы в случае надобности для данного слоя можно было прописать свою отдельную
 логику (логика прописывается в методе update, сейчас классы Sky и Other абсолютно идентичны)
'''

from pygame import Rect


class BasePlatform:
    def __init__(self, x, y, width, height, image):
        self.rect = Rect(x, y, width, height)
        self.image = image

    def update(self, hero):
        pass


class Floor(BasePlatform):
    def update(self, hero):
        if self.rect.colliderect(hero.rect):
            if ((self.rect.left <= hero.rect.right <= self.rect.right)
                or (self.rect.left >= hero.rect.left <= self.rect.right)) \
                    and (self.rect.top <= hero.rect.bottom <= self.rect.bottom):
                hero.rect.bottom = self.rect.top
                hero.grounded = True
                hero.velocity_y = 0


class FloorBottom(BasePlatform):
    def update(self, hero):
        if self.rect.colliderect(hero.rect):
            if (hero.rect.left < self.rect.left < hero.rect.right) \
                    and (self.rect.top <= hero.rect.top <= self.rect.bottom):
                hero.rect.top = self.rect.bottom
                hero.velocity_y = 0


class Sky(BasePlatform):
    pass


class Other(BasePlatform):
    pass
