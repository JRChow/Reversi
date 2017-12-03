from tkinter import *
from tkinter import messagebox
import reversi_logic as logic


class Board:
    def __init__(self, master, reversi):
        frame = Frame(master)
        frame.pack()

        self.master = master
        self.buttons = {}
        self.game = reversi
        self.state = reversi.initial

        # Put buttons and labels
        for row in range(0, self.game.height + 1):
            for col in range(0, self.game.width + 1):
                piece = Label(frame)  # Dummy piece
                if col > 0 and row > 0:  # Actual buttons
                    if (col, row) in self.state.board:  # Black and white
                        piece = Button(frame, bg="black" if self.state.board.get(
                            (col, row)) == 'B' else 'white', state=DISABLED)
                    elif (col, row) in self.state.moves:  # Valid moves
                        piece = Button(frame, bg="lawn green", state=NORMAL)
                    else:  # Background
                        piece = Button(frame, bg="green", state=DISABLED)
                    self.buttons[(col, row)] = piece  # Record button
                    # Add listener
                    piece.bind("<Button-1>", lambda event, move=(col, row): self.click(move))
                if col == 0 and row > 0:  # Vertical number axis
                    piece = Label(frame, text=str(row))
                if row == 0 and col > 0:  # Horizontal letter axis
                    piece = Label(frame, text=chr(col + 96))
                # Place piece
                piece.grid(row=row, column=col)

    def click(self, move):
        clicked_button = self.buttons[move]
        # If clicked on a disabled button, just ignore it.
        if str(clicked_button['state']) == 'disabled':
            return

        # Player makes move, update state
        self.state = self.game.result(self.state, move)
        self.update()  # Update UI

        # AI makes move
        ai_move = logic.alphabeta_player(self.game, self.state)
        # AI's move updates state
        self.state = self.game.result(self.state, ai_move)
        self.update()  # Update UI
        # Latest move made by AI has a different color
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
        if self.game.terminal_test(self.state):
            messagebox.showinfo(
                "Game Ends", "You Win!" if self.state.utility == +100 else "You lose!")

if __name__ == "__main__":
    root = Tk()
    root.title('Reversi')
    game = logic.Reversi()
    board = Board(root, game)
    root.mainloop()
