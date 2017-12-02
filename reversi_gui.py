from tkinter import *
from reversi_logic import *


class Board:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.buttons = {}
        for row in range(0, 8 + 1):  # TODO: remove hard-code
            for col in range(0, 8 + 1):  # TODO: remove hard-code
                if col > 0 and row > 0:
                    button = Button(frame, text=".", bg="green")
                    position = (col, row)  # (x, y)
                    button.bind("<Button-1>", lambda event,
                                arg=position: self.query_player(event, arg))
                    button.grid(row=row, column=col)
                    self.buttons[position] = button
                if col == 0 and row > 0:
                    label = Label(frame, text=str(row))
                    label.grid(row=row, column=col)
                if row == 0 and col > 0:
                    label = Label(frame, text=chr(col + 96))
                    label.grid(row=row, column=col)

    # def click(self, event, arg):
    #     print("clicked!")
    #     print(arg)
    #     self.buttons[arg].configure(bg="black")
    def query_player(event, arg):
        # print("clicked!")
        # print(arg)
        board.buttons[arg].configure(bg="black")
        state = game.result(state, move)
        return eval(arg)


root = Tk()
game = Reversi()
# game.play_game(query_player)
board = Board(root)
root.mainloop()
