import pygame
from Pieces.Pawn import Pawn
from Pieces.Rook import Rook
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.Queen import Queen
from Pieces.King import King
from Pieces import Piece
import AssessMoves

pygame.init()
scale = 1.6
WIDTH, HEIGHT = 640 * scale, 480 * scale
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Engine")
timer = pygame.time.Clock()
fps = 30
font = pygame.font.Font('freesansbold.ttf', 20)
tileSize = 60

capturedWhite = []
capturedBlack = []

turn = 0
hasSelectedPiece = False
heldPiece: Piece


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
    addPiece(Bishop(2, 0, 'white'))
    addPiece(Bishop(5, 0, 'white'))
    addPiece(Queen(3, 0, 'white'))
    addPiece(King(4, 0, 'white'))

    for i in range(8):
        pawn = Pawn(i, 6, 'black')
        addPiece(pawn)
    addPiece(Rook(0, 7, 'black'))
    addPiece(Rook(7, 7, 'black'))
    addPiece(Knight(6, 7, 'black'))
    addPiece(Knight(1, 7, 'black'))
    addPiece(Bishop(2, 7, 'black'))
    addPiece(Bishop(5, 7, 'black'))
    addPiece(Queen(4, 7, 'black'))
    addPiece(King(3, 7, 'black'))


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
                    pygame.draw.rect(screen, 'white',
                                     [80 * scale + (i * tileSize * scale), j * tileSize * scale, tileSize * scale,
                                      tileSize * scale])
            if i % 2 == 1:
                if j % 2 == 1:
                    pygame.draw.rect(screen, 'white',
                                     [80 * scale + (i * tileSize * scale), j * tileSize * scale, tileSize * scale,
                                      tileSize * scale, ])
    pygame.draw.rect(screen, 'gold', [80 * scale, 0, 480 * scale, 480 * scale], 3)


def getPieceScreenPos(piece):
    x = (piece.x * tileSize + piece.size / 2 + tileSize) * scale
    y = (piece.y * tileSize + tileSize - piece.size - (tileSize / 10)) * scale
    return x, y


def screenToTile(pos):
    if pos[0] < 80 * scale:
        pos = (-1, -1)
        return pos
    x = int((pos[0] - (80 * scale))//(tileSize * scale))
    y = (int(pos[1] // (tileSize * scale)))
    pos = (x, y)
    return pos


def findPieceInTile(pos):
    if turn % 2 == 0:
        for piece in whiteLivePieces:
            if piece.x == pos[0] and piece.y == pos[1]:
                return piece
    else:
        for piece in blackLivePieces:
            if piece.x == pos[0] and piece.y == pos[1]:
                return piece


def drawPieces():
    for i in range(len(whiteLivePieces)):
        piece = whiteLivePieces[i]
        screen.blit(piece.sprite, (getPieceScreenPos(piece)))
    for i in range(len(blackLivePieces)):
        piece = blackLivePieces[i]
        screen.blit(piece.sprite, (getPieceScreenPos(piece)))


run = True


def checkTileEmpty(pos):
    for piece in whiteLivePieces:
        if piece.x == pos[0] and piece.y == pos[1]:
            return False
    for piece in blackLivePieces:
        if piece.x == pos[0] and piece.y == pos[1]:
            return False
    return True


def getPieceAt(pos):
    if checkTileEmpty(pos):
        return None
    for piece in whiteLivePieces:
        if piece.x == pos[0] and piece.y == pos[1]:
            return piece
    for piece in blackLivePieces:
        if piece.x == pos[0] and piece.y == pos[1]:
            return piece

def getPieceId(pos):
    if checkTileEmpty(pos):
        return None
    for i in range(len(whiteLivePieces)):
        if whiteLivePieces[i].x == pos[0] and whiteLivePieces[i].y == pos[1]:
            return i
    for i in range(len(blackLivePieces)):
        if blackLivePieces[i].x == pos[0] and blackLivePieces[i].y == pos[1]:
            return i


def checkTileEnemy(pos, piece: Piece):
    if piece.team == 'white':
        for target in blackLivePieces:
            if target.x == pos[0] and target.y == pos[1]:
                return True
    else:
        for target in whiteLivePieces:
            if target.x == pos[0] and target.y == pos[1]:
                return True
    return False


def handleSelectPiece(event):
    global heldPiece
    x_coord = event.pos[0]
    y_coord = event.pos[1]
    clickCoords = (x_coord, y_coord)
    tileId = screenToTile(clickCoords)
    selectedPiece = findPieceInTile(tileId)

    if selectedPiece is not None:
        global hasSelectedPiece
        hasSelectedPiece = True
        heldPiece = selectedPiece
    screen.blit(font.render(str(screenToTile(clickCoords)), True, 'black'), (10 * scale, 100 * scale))


def handlePlacePiece(event):
    global hasSelectedPiece
    global heldPiece
    global turn
    x_coord = event.pos[0]
    y_coord = event.pos[1]
    clickCoords = (x_coord, y_coord)
    tileId = screenToTile(clickCoords)
    if checkTileEnemy(tileId, heldPiece) is True and AssessMoves.assess(heldPiece, tileId) is True:
        handleTakePiece(tileId)

    if checkTileEmpty(tileId) is True and AssessMoves.assess(heldPiece, tileId) is True:

        heldPiece.x = tileId[0]
        heldPiece.y = tileId[1]
        hasSelectedPiece = False
        #turn += 1


def handleTakePiece(pos):
    target = getPieceAt(pos)
    targetId = getPieceId(pos)
    if target is not None:
        if target.team == 'white':
            whiteLivePieces.pop(targetId)
        else:
            blackLivePieces.pop(targetId)


prepStartingPieces()

while run:
    timer.tick(fps)
    screen.fill('gray')
    drawBoard()
    drawPieces()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if hasSelectedPiece:
                handlePlacePiece(event)
            else:
                handleSelectPiece(event)

    pygame.display.flip()
pygame.quit()
