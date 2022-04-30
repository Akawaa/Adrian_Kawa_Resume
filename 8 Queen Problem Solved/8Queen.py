def makeboard(n):
    board = []
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append(0)
    return board

def valid(board, spot, n):
    row = spot[0]
    qcol = spot[1]
    validrow = 0
    for col in range(n):
        if col != qcol:
            validrow += board[row][col]
        if validrow > 0:
            return False
    validrow = 0

    qrow = spot[0]
    col = spot[1]
    validcol = 0
    for row in range(n):
        if row != qrow:
            validcol += board[row][col]
        if validcol > 0:
            return False
    validcol = 0

    row = spot[0]
    col = spot[1]
    counter = 0
    for i in range(1, n):
        check = [[row + i, col + i], [row + i, col - i], [row - i, col + i], [row - i, col - i]]
        try:
            if check[0][0] >= 0 and check[0][1] >= 0:
                if board[check[0][0]][check[0][1]] == 1:
                    counter += 1
        except:
            pass

        try:
            if check[1][0] >= 0 and check[1][1] >= 0:
                if board[check[1][0]][check[1][1]] == 1:
                    counter += 1
        except:
            pass

        try:
            if check[2][0] >= 0 and check[2][1] >= 0:
                if board[check[2][0]][check[2][1]] == 1:
                    counter += 1
        except:
            pass

        try:
            if check[3][0] >= 0 and check[3][1] >= 0:
                if board[check[3][0]][check[3][1]] == 1:
                    counter += 1
        except:
            pass

        if counter > 0:
            return False
    return True


def solve(board, col, n, counter):
    if counter == n:
        return board

    for row in range(n):
        board[row][col] = 1
        place = (row,col)
        if valid(board, place,  n):
            counter += 1
            if solve(board, col + 1, n, counter):
                return board
            board[row][col] = 0
            counter -= 1
        else:
            board[row][col] = 0
    return False


def queens(n):
    qboard = makeboard(n)
    solve(qboard, 0, n, 0)
    return qboard

grid = queens(11)
def makegrid(list, n):
    for i in range(n):
        print(list[i])
print(makegrid(grid, 11))
#print(makeboard(8))
