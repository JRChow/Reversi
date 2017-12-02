from tkinter import *


class Board:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        for row in range(0, 8 + 1):  # TODO: remove hard-code
            for col in range(0, 8 + 1):  # TODO: remove hard-code
                if col > 0 and row > 0:
                    button = Button(frame, text=".")
                if col == 0:
                    button = Button(frame, text=str(row))
                if row == 0:
                    button = Button(frame, text=str(col))
                button.grid(row=row, column=col)


root = Tk()
board = Board(root)
root.mainloop()
