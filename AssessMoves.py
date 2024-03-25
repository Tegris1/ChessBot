

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
        if change == diff:
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
            if checkChain([bishop.x, bishop.y], pos):
                return True
    return False


def assessQueen(queen, pos):
    diff = (queen.x - pos[0], queen.y - pos[1])
    for change in queen.allowedDiff:
        if change == diff:
            if checkChain([queen.x, queen.y], pos):
                return True
    return False


def checkChain(start, target):
    import main

    diff = [target[0] - start[0], target[1] - start[1]]
    step = diff
    print(str(diff))
    dist = max(abs(diff[0]), abs(diff[1]))
    if step[0] != 0:
        step[0] = diff[0]//abs(diff[0])
    if diff[1] != 0:
        step[1] = diff[1]//abs(diff[1])


    #print('Starting from' + str(start) + ' repeating: ' + str(dist))
    #print('step' + str(step))

    for i in range(dist - 1):
        start[0] += step[0]
        start[1] += step[1]
        #print('Checking at' + str(start))

        if not main.checkTileEmpty(start):
            #print('Failed at' + str(start))

            return False

        if start[0] < 0:
            break
        if start[1] < 0:
            break
        if start == target:
            return True
    return True
