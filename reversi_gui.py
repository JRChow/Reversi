from tkinter import *
from tkinter import messagebox
import reversi_logic
import time


class Board:
    def __init__(self, master, game):
        messagebox.showinfo("Title", "a Tk MessageBox")
        frame = Frame(master)
        frame.pack()
        self.master = master
        self.buttons = {}
        self.game = game
        self.state = game.initial
        # self.valid_moves = game.get_valid_moves(
        # self.state.board, self.state.to_move)
        for row in range(0, self.game.height + 1):
            for col in range(0, self.game.width + 1):
                piece = Label(frame)
                if col > 0 and row > 0:
                    if (col, row) in self.state.board:  # Black and white ones
                        piece = Button(frame, bg="black" if self.state.board.get(
                            (col, row)) == 'B' else 'white', state=DISABLED)
                    elif (col, row) in self.state.moves:  # Valid moves
                        piece = Button(frame, bg="lawn green", state=NORMAL)
                    else:  # Background
                        piece = Button(frame, bg="green", state=DISABLED)
                if col == 0 and row > 0:
                    piece = Label(frame, text=str(row))
                if row == 0 and col > 0:
                    piece = Label(frame, text=chr(col + 96))
                self.buttons[(col, row)] = piece
                piece.bind("<Button-1>", lambda event,
                           move=(col, row): self.click(event, move))
                piece.grid(row=row, column=col)

    def click(self, event, move):
        clicked_button = self.buttons[move]
        # If clicked on a disabled button, just ignore it.
        if str(clicked_button['state']) == 'disabled':
            return
        self.state = self.game.result(
            self.state, move)  # Player makes move, update state
        self.update()

        ai_move = reversi_logic.alphabeta_player(self.game, self.state)
        # AI makes move, update state
        self.state = self.game.result(self.state, ai_move)
        self.update()
        self.buttons[ai_move].configure(bg="light cyan")
        self.master.update()  # Refresh UI

    def update(self):
        for row in range(1, self.game.height + 1):
            for col in range(1, self.game.width + 1):
                pos = (col, row)
                if pos in self.state.board:  # Black and white
                    color = self.state.board.get(pos)
                    self.buttons[pos].configure(
                        bg="black" if color == 'B' else "white", state=DISABLED)
                elif pos in self.state.moves:  # Valid moves
                    self.buttons[pos].configure(
                        bg="green" if self.state.to_move == 'W' else "lawn green",
                        state=NORMAL if self.state.to_move == 'B' else DISABLED)
                else:  # Background
                    self.buttons[pos].configure(bg="green", state=DISABLED)
        self.master.update()  # Refresh UI


root = Tk()
root.title('Reversi')
game = reversi_logic.Reversi()
board = Board(root, game)
root.mainloop()
