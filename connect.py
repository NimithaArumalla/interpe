import tkinter as tk
from tkinter import messagebox

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = SQUARESIZE // 2 - 5
WINDOW_WIDTH = COLUMN_COUNT * SQUARESIZE
WINDOW_HEIGHT = (ROW_COUNT + 1) * SQUARESIZE

BACKGROUND_COLOR = "cyan"
EMPTY_COLOR = "black"
PLAYER1_COLOR = "red"
PLAYER2_COLOR = "yellow"

class ConnectFour:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")

        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=BACKGROUND_COLOR)
        self.canvas.pack()

        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game)
        self.reset_button.pack()

        self.board = [[0] * COLUMN_COUNT for _ in range(ROW_COUNT)]
        self.current_player = 1

        self.draw_board()

        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_board(self):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                x0 = c * SQUARESIZE
                y0 = (r + 1) * SQUARESIZE
                x1 = (c + 1) * SQUARESIZE
                y1 = (r + 2) * SQUARESIZE
                self.canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill=EMPTY_COLOR, outline=BACKGROUND_COLOR)

    def reset_game(self):
        self.board = [[0] * COLUMN_COUNT for _ in range(ROW_COUNT)]
        self.current_player = 1
        self.canvas.delete("all")
        self.draw_board()

    def handle_click(self, event):
        col = event.x // SQUARESIZE
        if col >= 0 and col < COLUMN_COUNT:
            row = self.get_next_open_row(col)
            if row is not None:
                self.board[row][col] = self.current_player
                self.draw_piece(row, col)
                if self.check_for_win(row, col):
                    self.game_over(f"Player {self.current_player} wins!")
                elif self.check_for_draw():
                    self.game_over("The game is a draw!")
                else:
                    self.current_player = 3 - self.current_player 

    def get_next_open_row(self, col):
        for r in range(ROW_COUNT):
            if self.board[r][col] == 0:
                return r
        return None

    def draw_piece(self, row, col):
        x0 = col * SQUARESIZE
        y0 = (ROW_COUNT - row) * SQUARESIZE
        x1 = (col + 1) * SQUARESIZE
        y1 = (ROW_COUNT - row + 1) * SQUARESIZE
        color = PLAYER1_COLOR if self.current_player == 1 else PLAYER2_COLOR
        self.canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill=color, outline=BACKGROUND_COLOR)

    def check_for_win(self, row, col):
        piece = self.current_player
        
        for c in range(COLUMN_COUNT - 3):
            if self.board[row][c] == piece and self.board[row][c+1] == piece and \
               self.board[row][c+2] == piece and self.board[row][c+3] == piece:
                return True
        
        for r in range(ROW_COUNT - 3):
            if self.board[r][col] == piece and self.board[r+1][col] == piece and \
               self.board[r+2][col] == piece and self.board[r+3][col] == piece:
                return True
        
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and \
                   self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True
        
        for r in range(3, ROW_COUNT):
            for c in range(COLUMN_COUNT - 3):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and \
                   self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True
        return False

    def check_for_draw(self):
        for c in range(COLUMN_COUNT):
            if self.board[ROW_COUNT-1][c] == 0:
                return False
        return True

    def game_over(self, message):
        messagebox.showinfo("Game Over", message)
        self.reset_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFour(root)
    root.mainloop()
