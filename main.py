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
# sprites
# region

capturedWhite = []
capturedBlack = []
turn = 47
# black_queen = pygame.image.load('assets/images/black queen.png')
# black_queen = pygame.transform.scale(black_queen, (80, 80))
# black_queen_small = pygame.transform.scale(black_queen, (45, 45))
# black_king = pygame.image.load('assets/images/black king.png')
# black_king = pygame.transform.scale(black_king, (80, 80))
# black_king_small = pygame.transform.scale(black_king, (45, 45))
# black_rook = pygame.image.load('assets/images/black rook.png')
# black_rook = pygame.transform.scale(black_rook, (80, 80))
# black_rook_small = pygame.transform.scale(black_rook, (45, 45))
# black_bishop = pygame.image.load('assets/images/black bishop.png')
# black_bishop = pygame.transform.scale(black_bishop, (80, 80))
# black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
# black_knight = pygame.image.load('assets/images/black knight.png')
# black_knight = pygame.transform.scale(black_knight, (80, 80))
# black_knight_small = pygame.transform.scale(black_knight, (45, 45))
# black_pawn = pygame.image.load('assets/images/black pawn.png')
# black_pawn = pygame.transform.scale(black_pawn, (65, 65))
# black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
# white_queen = pygame.image.load('assets/images/white queen.png')
# white_queen = pygame.transform.scale(white_queen, (80, 80))
# white_queen_small = pygame.transform.scale(white_queen, (45, 45))
# white_king = pygame.image.load('assets/images/white king.png')
# white_king = pygame.transform.scale(white_king, (80, 80))
# white_king_small = pygame.transform.scale(white_king, (45, 45))
# white_rook = pygame.image.load('assets/images/white rook.png')
# white_rook = pygame.transform.scale(white_rook, (80, 80))
# white_rook_small = pygame.transform.scale(white_rook, (45, 45))
# white_bishop = pygame.image.load('assets/images/white bishop.png')
# white_bishop = pygame.transform.scale(white_bishop, (80, 80))
# white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
# white_knight = pygame.image.load('assets/images/white knight.png')
# white_knight = pygame.transform.scale(white_knight, (80, 80))
# white_knight_small = pygame.transform.scale(white_knight, (45, 45))
# white_pawn = pygame.image.load('assets/images/white pawn.png')
# white_pawn = pygame.transform.scale(white_pawn, (65, 65))
# white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))
# white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
# small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
#                       white_rook_small, white_bishop_small]
# black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
# small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
#                       black_rook_small, black_bishop_small]
# piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']


# endregion
# Base engine loop
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
