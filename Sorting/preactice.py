
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "A"


def backtrack():
    row,col = len(board),len(board[0])

    def dfs(i, j, index):
        if index >= len(word):
            return True
        
        if i < 0 or i>=row or j >= col or j < 0:
            return False
        
        if board[i][j] != word[index]:
            return False
        
        temp = board[i][j]
        board[i][j] = '#'

        found = (
            dfs(i+1, j, index+1) or dfs(i-1, j, index+1) or dfs(i, j-1, index+1) or dfs(i, j+1, index+1)
        )

        board[i][j] = temp

        return found
        

    for i in range(row):
        for j in range(col):
            if board[i][j] == word[0]:
                if dfs(i,j, 0):
                    return True
                
    return False

print(backtrack())
                 







            
