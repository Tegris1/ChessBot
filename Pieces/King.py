from Pieces.Piece import Piece


class King(Piece):
    size = 50
    value = 0
    allowedDiff = ((-1, 1), (0, 1), (1,1),
                   (-1, 0), (0, 0), (1, 0),
                   (-1, -1), (0, -1), (1,-1))
    id = 0


    def __init__(self, x: int, y: int, team: str):
        self.team = team
        self.spritePath = 'assets/images/' + team + '/' + 'king.png'
        self.x = x
        self.y = y
        self.sprite = self.setSprite(self.spritePath, self.size)