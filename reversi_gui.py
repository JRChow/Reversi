from tkinter import *
import reversi_logic


class Board:
    def __init__(self, master, game):
        frame = Frame(master)
        frame.pack()
        self.buttons = {}
        initial_state = game.initial
        valid_moves = game.get_valid_moves(
            initial_state.board, initial_state.to_move)
        for row in range(0, 8 + 1):  # TODO: remove hard-code
            for col in range(0, 8 + 1):  # TODO: remove hard-code
                piece = Label(frame)
                if col > 0 and row > 0:
                    if (col, row) in initial_state.board:
                        piece = Button(frame, bg="black" if initial_state.board.get(
                            (col, row)) == 'B' else 'white', state=DISABLED)
                    elif (col, row) in valid_moves:
                        piece = Button(frame, text=".", bg="lawn green")
                        piece.bind("<Button-1>", lambda event,
                                   arg=(col, row): self.click(event, arg))
                    else:
                        piece = Button(frame, text=".", bg="green")
                        piece.bind("<Button-1>", lambda event,
                                   arg=(col, row): self.click(event, arg))
                        self.buttons[(col, row)] = piece
                if col == 0 and row > 0:
                    piece = Label(frame, text=str(row))
                if row == 0 and col > 0:
                    piece = Label(frame, text=chr(col + 96))
                piece.grid(row=row, column=col)

    def click(self, event, arg):
        print("clicked!")
        print(arg)
        self.buttons[arg].configure(bg="black")
        return arg

    # def update(self, state):


root = Tk()
game = reversi_logic.Reversi()
board = Board(root, game)
root.mainloop()
