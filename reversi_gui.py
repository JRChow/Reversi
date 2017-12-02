from tkinter import *


class Board:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        for row in range(1, 8 + 1):  # TODO: remove hard-code
            for col in range(1, 8 + 1):  # TODO: remove hard-code
                button = Button(frame, text="Hi")
                button.grid(row=row, column=col)


root = Tk()
board = Board(root)
root.mainloop()
