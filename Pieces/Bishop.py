from Pieces.Piece import Piece


class Bishop(Piece):
    size = 50
    value = 3
    allowedDiff = []
    id = 3

    def __init__(self, x: int, y: int, team: str):
        self.team = team
        self.spritePath = 'assets/images/' + team + '/' + 'bishop.png'
        self.x = x
        self.y = y
        self.sprite = self.setSprite(self.spritePath, self.size)
        for i in range(7):
            self.allowedDiff.append((i, i))
            self.allowedDiff.append((-i, -i))
            self.allowedDiff.append((i, -i))
            self.allowedDiff.append((-i, i))