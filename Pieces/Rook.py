from Pieces.Piece import Piece


class Rook(Piece):
    size = 50
    value = 5
    id = 4
    allowedDiff = []

    def __init__(self, x: int, y: int, team: str):
        self.team = team
        self.spritePath = 'assets/images/'+team +'/'+'rook.png'
        self.x = x
        self.y = y
        self.sprite = self.setSprite(self.spritePath,self.size)
        for i in range(7):
            self.allowedDiff.append((0, i))
            self.allowedDiff.append((0, -i))
            self.allowedDiff.append((i, 0))
            self.allowedDiff.append((-i, 0))