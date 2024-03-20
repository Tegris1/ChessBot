from Pieces.Piece import Piece


class Knight(Piece):
    size = 50
    value = 1

    def __init__(self, x: int, y: int, team: str):
        self.team = team
        self.spritePath = 'assets/images/' + team + '/' + 'knight.png'
        self.x = x
        self.y = y
        self.sprite = self.setSprite(self.spritePath, self.size)