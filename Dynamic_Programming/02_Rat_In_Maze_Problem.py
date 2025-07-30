board = ['1000',
         '1111',
         '1101',
         '0111']

result = []

def is_safe(board, row, col, dir):
    print('IS_SAFE',row, col, dir)
    if dir == 'd':
        return row + 1 < 4 and board[row+1][col] == '1'
    
    elif dir == 'l':
        return col - 1 >= 0 and board[row][col-1] == '1'
    
    elif dir == 'r':
        return col + 1 < 4 and board[row][col+1] == '1'
    
    elif dir == 'u':
        return row - 1 >=0 and board[row-1][col] == '1'
           
    return False



def backtrack(board, row=0, col=0, path=''):
    if row == 3 and col == 3:
        result.append(path)
        print(path)
        return

    
    board[row]= board[row][:col]+'0'+board[row][col+1:]
    if is_safe(board, row, col, 'd'):
        backtrack(board, row+1, col, path+'D')
    if is_safe(board, row, col, 'l'):
        backtrack(board, row, col-1, path+'L')
    if is_safe(board, row, col, 'r'):
        backtrack(board, row, col+1, path+'R')
    if is_safe(board, row, col, 'u'):
        backtrack(board, row-1, col, path+'U')

    board[row]= board[row][:col]+'1'+board[row][col+1:]


backtrack(board)
print(result)


    