board=[["-" for _ in range(3)] for _ in range(3)]
player="X"
winner=None
gameContinue=True
def printBoard():
    for row in board:
        print(" ".join(row))



def playerInput():
    num=int(input("enter number in range of 1 to 9"))
    if num>=1 and num<=9 and board[num-1]=="-":
        board[num-1]=player
while gameContinue:
    printBoard()
    playerInput()
    
        
    
