from tkinter import *
import reversi_logic
import time


class Board:
    def __init__(self, master, game):
        frame = Frame(master)
        frame.pack()
        self.buttons = {}
        self.game = game
        self.state = game.initial
        self.valid_moves = game.get_valid_moves(
            self.state.board, self.state.to_move)
        for row in range(0, 8 + 1):  # TODO: remove hard-code
            for col in range(0, 8 + 1):  # TODO: remove hard-code
                piece = Label(frame)
                if col > 0 and row > 0:
                    if (col, row) in self.state.board:  # Black and white ones
                        piece = Button(frame, bg="black" if self.state.board.get(
                            (col, row)) == 'B' else 'white', state=DISABLED)
                    elif (col, row) in self.valid_moves:  # Valid moves
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
        if str(clicked_button['state']) == 'disabled':
            return
        print("clicked!")
        print(move)
        clicked_button.configure(bg="black")
        self.state = self.game.play_game(move, self.state)
        self.update()

        Tk.update()

        ai_move = reversi_logic.alphabeta_player(self.game, self.state)
        self.state = self.game.play_game(ai_move, self.state)

        self.update()

    def update(self):
        print("Update!!")
        # Update valid moves
        self.valid_moves = game.get_valid_moves(
            self.state.board, self.state.to_move)
        for pos in self.valid_moves:  # Valid moves
            self.buttons[pos].configure(
                bg="green" if self.state.to_move == 'W' else "lawn green",
                state=NORMAL if self.state.to_move == 'B' else DISABLED)
        for pos, color in self.state.board.items():  # Black and white
            self.buttons[pos].configure(
                bg="black" if color == 'B' else "white", state=DISABLED)
        # # valid_moves = game.get_valid_moves(self.state.board, self.state.to_move)
        # for row in range(0, self.game.height + 1):
        #     for col in range(0, self.game.width + 1):
        #         piece = Label(frame)
        #         if col > 0 and row > 0:
        #             if (col, row) in self.state.board:
        #                 piece = Button(frame, bg="black" if self.state.board.get(
        #                     (col, row)) == 'B' else 'white', state=DISABLED)
        #             elif (col, row) in valid_moves:
        #                 piece = Button(frame, bg="lawn green")
        #                 piece.bind("<Button-1>", lambda event,
        #                            move=(col, row): self.click(event, move))
        #             else:
        #                 piece = Button(frame, bg="green", state=DISABLED)
        #         if col == 0 and row > 0:
        #             piece = Label(frame, text=str(row))
        #         if row == 0 and col > 0:
        #             piece = Label(frame, text=chr(col + 96))
        #         self.buttons[(col, row)] = piece
        #         piece.grid(row=row, column=col)


root = Tk()
game = reversi_logic.Reversi()
board = Board(root, game)
root.mainloop()
