import pygame
from Pieces.Pawn import Pawn
from Pieces.Rook import Rook
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.Queen import Queen
from Pieces.King import King

pygame.init()
scale = 1.5
WIDTH, HEIGHT = 640* scale, 480* scale
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Engine")
timer = pygame.time.Clock()
fps = 30
font = pygame.font.Font('freesansbold.ttf', 20)
tileSize = 60

capturedWhite = []
capturedBlack = []
turn = 47

whiteLivePieces = []
blackLivePieces = []


def prepStartingPieces():
    for i in range(8):
        pawn = Pawn(i, 1, 'white')
        addPiece(pawn)
    addPiece(Rook(0, 0, 'white'))
    addPiece(Rook(7, 0, 'white'))
    addPiece(Knight(1, 0, 'white'))
    addPiece(Knight(6, 0, 'white'))
    addPiece(Bishop(2,0,'white'))
    addPiece(Bishop(5,0,'white'))
    addPiece(Queen(3,0,'white'))
    addPiece(King(4,0,'white'))

    for i in range(8):
        pawn = Pawn(i, 6, 'black')
        addPiece(pawn)
    addPiece(Rook(0, 7, 'black'))
    addPiece(Rook(7, 7, 'black'))
    addPiece(Knight(6, 7, 'black'))
    addPiece(Knight(1, 7, 'black'))
    addPiece(Bishop(2,7,'black'))
    addPiece(Bishop(5,7,'black'))
    addPiece(Queen(4,7,'black'))
    addPiece(King(3,7,'black'))

def addPiece(piece):
    if piece.team == 'white':
        whiteLivePieces.append(piece)
    if piece.team == 'black':
        blackLivePieces.append(piece)


def drawBoard():
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    pygame.draw.rect(screen, 'white', [80 * scale + (i * tileSize*scale), j * tileSize*scale, tileSize * scale, tileSize * scale ])
            if i % 2 == 1:
                if j % 2 == 1:
                    pygame.draw.rect(screen, 'white', [80 * scale + (i * tileSize * scale), j * tileSize * scale, tileSize * scale, tileSize * scale, ])
    pygame.draw.rect(screen, 'gold', [80 * scale, 0, 480 * scale, 480 * scale], 3)
    turnText = ['White', 'Black']
    screen.blit(font.render(turnText[turn % 2], True, (turnText[turn % 2])), (10 *  scale, 30 * scale))


def getPieceScreenPos(piece):
    x = (piece.x * tileSize + piece.size / 2 + tileSize) * scale
    y = (piece.y * tileSize + tileSize - piece.size - (tileSize / 10)) * scale
    return x, y


def drawPieces():
    for i in range(len(whiteLivePieces)):
        piece = whiteLivePieces[i]
        screen.blit(piece.sprite, (getPieceScreenPos(piece)))
    for i in range(len(blackLivePieces)):
        piece = blackLivePieces[i]
        screen.blit(piece.sprite, (getPieceScreenPos(piece)))


run = True
while run:
    timer.tick(fps)
    screen.fill('gray')
    drawBoard()
    prepStartingPieces()
    drawPieces()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
