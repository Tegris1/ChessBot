

def assess(piece, pos):
    print('Entered assessment')
    match piece.id:
        case 0:
            return assessKing(piece, pos)

        case 1:
            return assessPawn(piece, pos)

        case 2:
            return assessKnight(piece, pos)

        case 3:
            return assessBishop(piece, pos)

        case 4:
            return assessRook(piece, pos)

        case 5:
            return assessQueen(piece, pos)


def assessPawn(pawn, pos):
    if pawn.team == 'white':
        print(pawn.move)
        diff = (pos[0] - pawn.x, pos[1] - pawn.y)
        if diff == (0, 2) and pawn.move == 0:
            pawn.move += 1
            return True
        elif diff == (0, 1):
            pawn.move += 1
            return True
    else:

        diff = (pos[0] - pawn.x, pos[1] - pawn.y)
        if diff == (0, -2) and pawn.move == 0:
            pawn.move += 1
            return True
        elif diff == (0, -1):
            pawn.move += 1
            return True
    return False


def assessKing(king, pos):
    diff = (pos[0] - king.x, pos[1] - king.y)
    print(diff)
    for change in king.allowedDiff:
        if change == diff:
            return True


def assessKnight(knight, pos):
    diff = (knight.x - pos[0], knight.y - pos[1])
    print(diff)
    for change in knight.allowedDiff:
        print(str(diff) + ' change: ' + str(change))
        print(diff == change)
        print(type(change))
        if change == diff:
            print('innnnn')
            return True


def assessRook(rook, pos):
    diff = (rook.x - pos[0], rook.y - pos[1])
    for change in rook.allowedDiff:
        if change == diff:
            print(str(diff) + ' change: ' + str(change))
            if checkChain([rook.x, rook.y], pos):
                return True
    return False

def assessBishop(bishop, pos):
    diff = (bishop.x - pos[0], bishop.y - pos[1])
    for change in bishop.allowedDiff:
        if change == diff:
            print(str(diff) + ' change: ' + str(change))
            if checkChain([bishop.x, bishop.y], pos):
                return True
    return False


def assessQueen(queen, pos):
    return True


def checkChain(start, target):
    import main

    #fix
    #region
    diff = [target[0] - start[0], target[1] - start[1]]
    step = diff
    if step[0] != 0:
        step[0] = diff[0]//abs(diff[0])
    if diff[1] != 0:
        step[1] = diff[1]//abs(diff[1])
    #endregion

    check = start
    directions = [[-1, 1], [0, 1], [1, 1],
                  [-1, 0], [1, 0],
                  [-1, -1], [0, -1], [1, -1]]


    for i in range(7):
        if not main.checkTileEmpty([check[0] + step[0], check[1] + step[1]]):
            return False
    return True
