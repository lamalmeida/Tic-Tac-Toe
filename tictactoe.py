import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
 
sign = 0
global board
board = [[" " for x in range(3)] for y in range(3)]

def winner(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))
def isfull():
    flag = True
    for i in board:
        if(i.count(' ') > 0):
            flag = False
    return flag
def pc1():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner)-1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge)-1)
            return edge[move]
def evaluate() :   
    for row in range(3) :      
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]) :         
            if (board[row][0] == 'X') : 
                return 10
            elif (board[row][0] == 'O') : 
                return -10 
    for col in range(3) : 
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col]) : 
            if (board[0][col] == 'X') :  
                return 10
            elif (board[0][col] == 'O') : 
                return -10 
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) : 
        if (board[0][0] == 'X') : 
            return 10
        elif (board[0][0] == 'O') : 
            return -10
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) : 
        if (board[0][2] == 'X') : 
            return 10
        elif (board[0][2] == 'O') : 
            return -10 
    return 0
def minimax(depth, isMax) :  
    score = evaluate()  
    if (score == 10) :  
        return score 
    if (score == -10) : 
        return score 
    if (isfull() == True) : 
        return 0
    if (isMax) :     
        best = -1000  
        for i in range(3) :          
            for j in range(3) : 
                if (board[i][j]==' ') : 
                    board[i][j] = 'X'  
                    best = max(best, minimax(depth + 1, not isMax)) 
                    board[i][j] = ' '
        return best  
    else : 
        best = 1000 
        for i in range(3) :          
            for j in range(3) : 
                if (board[i][j] == ' ') : 
                    board[i][j] = 'O'  
                    best = min(best, minimax(depth + 1, not isMax))  
                    board[i][j] = ' '
        return best
def pc2():
    bestVal = 1000 
    bestMove = (-1, -1)  
    for i in range(3) :      
        for j in range(3) :  
            if (board[i][j] == ' ') :   
                board[i][j] = 'O'
                moveVal = minimax(0, True) 
                board[i][j] = ' ' 
                if (moveVal < bestVal) :                 
                    bestMove = (i, j) 
                    bestVal = moveVal 
    return bestMove 
def get_text_pc(i, j, gb, l1, l2, level):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        x = False
        box = messagebox.showinfo("Winner", "Player won the match")
        gb.destroy()
        play()
    elif winner(board, "O"):
        x = False
        box = messagebox.showinfo("Winner", "Computer won the match")
        gb.destroy()
        play()
    elif(isfull()):
        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")
        gb.destroy()
        play()
    if(x):
        if sign % 2 != 0:
            if level == 1:
                move = pc1()
            elif level == 2:
                move = pc2()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2, level)
def gameboard_pc(game_board, l1, l2, level):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2, level)
            button[i][j] = Button(game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()
    
def withpc(game_board, level):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Computer : O", width=10, state=DISABLED)
    l2.grid(row=2, column=1)
    gameboard_pc(game_board, l1, l2, level)
def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Tic Tac Toe")
    wpc1 = partial(withpc, menu, 1)
    wpc2 = partial(withpc, menu, 2)
    head = Button(menu, text="---Welcome to tic-tac-toe---",
                  activeforeground='red',
                  activebackground="yellow", bg="red",
                  fg="yellow", width=500, font='summer', bd=5)
    B1 = Button(menu, text="Play Level 1", command=wpc1,
                activeforeground='red',
                activebackground="yellow", bg="red",
                fg="yellow", width=500, font='summer', bd=5)
    B2 = Button(menu, text="Play Level 2", command=wpc2,
                activeforeground='red',
                activebackground="yellow", bg="red",
                fg="yellow", width=500, font='summer', bd=5)
    B3 = Button(menu, text="Exit", command=menu.quit, activeforeground='red',
                activebackground="yellow", bg="red", fg="yellow",
                width=500, font='summer', bd=5)
    global board 
    board =  [[" " for x in range(3)] for y in range(3)]
    global sign
    sign = 0
    head.pack(side='top')
    B1.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    menu.mainloop()
if __name__ == '__main__':
    play()
