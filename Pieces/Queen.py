from Pieces.Piece import Piece


class Queen(Piece):
    size = 50
    value = 9
    id = 5

    def __init__(self, x: int, y: int, team: str):
        self.team = team
        self.spritePath = 'assets/images/' + team + '/' + 'queen.png'
        self.x = x
        self.y = y
        self.sprite = self.setSprite(self.spritePath, self.size)
