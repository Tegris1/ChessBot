import pygame


class Piece(object):
    scale = 1.6
    x, y = 0, 0
    size = 50
    value = 0
    team = ''
    spritePath = ''
    sprite = pygame.image

    def setSprite(self, spritePath, size):
        sprite = pygame.image.load(spritePath)
        sprite = pygame.transform.scale(sprite, (size * self.scale, size * self.scale))
        return sprite

    def getBoardPosition(self):
        return self.x * self.scale, self.y* self.scale, self.scale
