from tkinter import *
import reversi_logic


class Board:
    def __init__(self, master, initial_state):
        frame = Frame(master)
        frame.pack()
        self.buttons = {}
        for row in range(0, 8 + 1):  # TODO: remove hard-code
            for col in range(0, 8 + 1):  # TODO: remove hard-code
                if col > 0 and row > 0:
                    if (col, row) in initial_state.board:
                        button = Button(frame, bg="black" if initial_state.board.get(
                            (col, row)) == 'B' else 'white', state=DISABLED)
                        button.grid(row=row, column=col)
                    else:
                        button = Button(frame, text=".", bg="green")
                        position = (col, row)  # (x, y)
                        button.bind("<Button-1>", lambda event,
                                    arg=position: self.click(event, arg))
                        button.grid(row=row, column=col)
                        self.buttons[position] = button
                if col == 0 and row > 0:
                    label = Label(frame, text=str(row))
                    label.grid(row=row, column=col)
                if row == 0 and col > 0:
                    label = Label(frame, text=chr(col + 96))
                    label.grid(row=row, column=col)

    def click(self, event, arg):
        print("clicked!")
        print(arg)
        self.buttons[arg].configure(bg="black")
        return arg


root = Tk()
game = reversi_logic.Reversi()
board = Board(root, game.initial)
root.mainloop()
