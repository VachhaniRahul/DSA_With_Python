


n = 4
result = []
board = ['.'*n for i in range(n)]


def is_safe(row, col, board,n):
    dub_row = row
    dub_col = col

    while col >= 0 and row >=0:
        if board[row][col] == 'Q':
            return False
        row -=1
        col -= 1

    row = dub_row
    col = dub_col

    while col >= 0:
        if board[row][col] == 'Q':
            return False
        col -= 1

    row = dub_row
    col = dub_col

    while col >= 0 and row < n:
        if board[row][col] == 'Q':
            return False
        row += 1
        col -= 1

    return True


def queen(col, board, n):

    if col == n:
        result.append(board[:])
        return
    
    for row in range(n):
        if is_safe(row, col, board, n):
            board[row] = board[row][:col] + 'Q' + board[row][col+1:]
            queen(col+1, board, n)
            board[row] = board[row][:col] + '.' + board[row][col+1:]
        
    
queen(0, board, n)

# Optional: pretty print the solutions
for solution in result:
    for row in solution:
        print(row)
    print('---')

print(f"Total solutions: {len(result)}")




