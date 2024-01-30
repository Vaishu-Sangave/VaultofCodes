import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player = 'X'

        self.buttons = [[None, None, None] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text='', font=('normal', 20), width=35, height=5,
                                              command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.buttons[row][col]['text'] == '':
            self.buttons[row][col]['text'] = self.current_player
            self.buttons[row][col]['bg'] = 'cyan'  # Light Greenr

            if self.check_winner(row, col):
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        # Check row
        if all(self.buttons[row][c]['text'] == self.current_player for c in range(3)):
            self.highlight_winner_cells(row, range(3))
            return True

        # Check column
        if all(self.buttons[r][col]['text'] == self.current_player for r in range(3)):
            self.highlight_winner_cells(range(3), col)
            return True

        # Check diagonals
        if all(self.buttons[i][i]['text'] == self.current_player for i in range(3)):
            self.highlight_winner_cells(range(3), range(3))
            return True
        if all(self.buttons[i][2 - i]['text'] == self.current_player for i in range(3)):
            self.highlight_winner_cells(range(3), range(2, -1, -1))
            return True

        return False

    def highlight_winner_cells(self, rows, cols):
        for row in rows:
            for col in cols:
                self.buttons[row][col]['bg'] = 'red'  # Gold

    def is_board_full(self):
        return all(self.buttons[i][j]['text'] != '' for i in range(3) for j in range(3))

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''
                self.buttons[i][j]['bg'] = 'SystemButtonFace'
        self.current_player = 'X'

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
