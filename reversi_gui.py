from tkinter import *


class Board:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        buttons = {}
        for row in range(0, 8 + 1):  # TODO: remove hard-code
            for col in range(0, 8 + 1):  # TODO: remove hard-code
                if col > 0 and row > 0:
                    button = Button(frame, text=".")
                    position = (col, row)  # (x, y)
                    button.bind("<Button-1>", lambda event,
                                arg=position: self.click(event, arg))
                    button.grid(row=row, column=col)
                    buttons[position] = button
                if col == 0 and row > 0:
                    label = Label(frame, text=str(row))
                    label.grid(row=row, column=col)
                if row == 0 and col > 0:
                    label = Label(frame, text=chr(col + 96))
                    label.grid(row=row, column=col)

    def click(event, arg):
        print("clicked!")
        print(arg)


root = Tk()
board = Board(root)
root.mainloop()
