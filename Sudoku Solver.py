from tkinter import *
window = Tk()
window.title("Sudoku Solver")
window.geometry("500x500")


#input board parameters only digits 0 to 9: 0 signifying empty cell
board = [[1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

#set simple GUI board for visualisation
for i in range(9):
    for j in range(9):
        if (board[i][j] == 0):
            lb = Label(window, text = " ", borderwidth = 10, relief = RIDGE )
        else:
            lb = Label(window, text = board[i][j], borderwidth = 10, relief = RIDGE)
        lb.grid(row = i, column = j)


#get next empty cell from 9x9 board
def getEmptyCell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j)
    return None


#checks if the board is valid when a number is inserted at a target position
def valid(board, position, number):
    #check row
    for i in range(9):
        if board[position[0]][i] == number and position[1] != i:
            return False

    #check column
        if board[i][position[1]] == number and position[0] != i:
            return False
            
    #check for 3x3 box
    rowbatch = ((position[0]) //3)*3 
    colbatch = ((position[1]) //3)*3 
    for boxRow in range(rowbatch, rowbatch + 3):
        for boxCol in range(colbatch, colbatch + 3):
            if board[boxRow][boxCol] == number and (boxRow, boxCol) != position:
                return False
    
    
    return True
            

def dfs(board):
    #get next empty cell if any; if return True, board is completed
    if getEmptyCell(board) == None:
        return True
    else:
        row, col = getEmptyCell(board)

    #loop through digits 1 to 9
    for i in range(1, 10):

        #if board is valid
        if (valid(board, (row, col), i)):
            #set empty cell value
            board[row][col] = i

            #handle User Interface
            lb = Label(window, text = i, bg = "LIGHTGREEN")
            lb.grid(row = row, column = col)
            window.update_idletasks()
            window.after(5) #set time for colour change in UI

            #recursive step; to set next empty cell
            if dfs(board):
                return True

            #when further steps return false, reset the current cell to 0
            board[row][col] = 0
            lb = Label(window, text = 0, bg = "PINK")
            lb.grid(row = row, column = col)
            window.update_idletasks()
            window.after(5) #set time for colour change in UI
    return False
    
                
dfs(board)

for i in range(9):
    print(board[i])
# window.mainloop()
