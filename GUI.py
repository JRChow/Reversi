
import tkinter
import othello_logic


class OthelloOptions:
    def __init__(self):
        """Initialize all of the board options"""
        # size of window
        self._size_window = tkinter.Tk()
        self._size_window.title("Inputs Window")

        options = (4, 6, 8, 10, 12, 14, 16)
        self._usercol = tkinter.StringVar(self._size_window)
        self._usercol.set(options[0])
        self._col = tkinter.OptionMenu(
            self._size_window, self._usercol, *options)
        self._col.grid(row=0, column=1,
                       sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._userrow = tkinter.StringVar(self._size_window)
        self._userrow.set(options[0])
        self._row = tkinter.OptionMenu(
            self._size_window, self._userrow, *options)
        self._row.grid(row=1, column=1,
                       sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._col_label = tkinter.Label(
            self._size_window, text='Number of Columns: ')
        self._col_label.grid(row=0, column=0,
                             sticky=tkinter.W)

        self._row_label = tkinter.Label(
            self._size_window, text='Number of Rows: ')
        self._row_label.grid(row=1, column=0,
                             sticky=tkinter.W)

        self._size_window.rowconfigure(2, weight=5)
        self._size_window.rowconfigure(5, weight=5)
        self._size_window.rowconfigure(8, weight=5)
        self._size_window.rowconfigure(11, weight=5)
        self._size_window.columnconfigure(0, weight=5)
        self._size_window.columnconfigure(1, weight=5)

        # which player moves first button
        self._move_first = tkinter.StringVar(self._size_window)

        self._move_first.set(othello_logic.WHITE)
        self._first_button = tkinter.Radiobutton(
            self._size_window, variable=self._move_first, text='White', value=othello_logic.WHITE)
        self._second_button = tkinter.Radiobutton(
            self._size_window, variable=self._move_first, text='Black', value=othello_logic.BLACK)

        self._first_button.grid(
            row=3, column=1, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        self._second_button.grid(
            row=4, column=1, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._move_label = tkinter.Label(
            self._size_window, text='Which player moves first: ')
        self._move_label.grid(row=3, column=0, rowspan=2,
                              sticky=tkinter.W)
        # top left player button
        self._top_left = tkinter.StringVar(self._size_window)

        self._top_left.set(othello_logic.WHITE)
        self._third_button = tkinter.Radiobutton(
            self._size_window, variable=self._top_left, text='White', value=othello_logic.WHITE)
        self._fourth_button = tkinter.Radiobutton(
            self._size_window, variable=self._top_left, text='Black', value=othello_logic.BLACK)

        self._third_button.grid(
            row=6, column=1, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        self._fourth_button.grid(
            row=7, column=1, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._move_label = tkinter.Label(
            self._size_window, text='Which player in top\n left position: ')
        self._move_label.grid(row=6, column=0, rowspan=2,
                              sticky=tkinter.W)

        # how to win button
        self._winner = tkinter.StringVar(self._size_window)

        self._winner.set('Most')
        self._fifth_button = tkinter.Radiobutton(
            self._size_window, variable=self._winner, text='Most', value='Most')
        self._sixth_button = tkinter.Radiobutton(
            self._size_window, variable=self._winner, text='Least', value='Least')

        self._fifth_button.grid(
            row=9, column=1, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        self._sixth_button.grid(
            row=10, column=1, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._move_label = tkinter.Label(
            self._size_window, text='Win by most or least: ')
        self._move_label.grid(row=9, column=0, rowspan=2,
                              sticky=tkinter.W)

        # start button, destroy window
        self._start = tkinter.Button(self._size_window, text='PLAY GAME!')
        self._start.grid(row=12, column=0, columnspan=2, rowspan=2, padx=50, pady=15,
                         sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._start.bind('<Button-1>', self._on_play_game)

        self._size_window.mainloop()

    def _on_play_game(self, event: tkinter.Event) -> None:
        """starts othelloapplication board"""
        self._size_window.destroy()

        OthelloApplication(int(self._usercol.get()), int(self._userrow.get()), self._move_first.get(),
                           self._top_left.get(), self._winner.get())


class OthelloApplication:
    def __init__(self, columns: int, rows: int, move_first: str, top_left: str, win_type: str) -> None:

        # main window
        self._root_window = tkinter.Tk()
        self._root_window.title("Othello Game")

        self._columns = columns
        self._rows = rows
        self._move_first = move_first
        self._top_left = top_left
        self._win_type = win_type
        self._game_over = False

        self._othello_game = othello_logic.Game(
            columns, rows, move_first, top_left)
        self._current_board = self._othello_game._board

        self._canvas = tkinter.Canvas(
            master=self._root_window,
            width=500, height=500,
            background='darkgreen')
        self._canvas.grid(row=1, column=0,
                          sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._score = tkinter.Canvas(
            master=self._root_window, width=500, height=75, background='darkgreen',
            borderwidth=10, relief='raised')
        self._score.grid(
            row=0, column=0, pady=10,
            sticky=tkinter.N + tkinter.W + tkinter.E)

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)

        self._root_window.rowconfigure(1, weight=100)
        self._root_window.rowconfigure(0, weight=5)
        self._root_window.columnconfigure(0, weight=5)

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        """find the coordinates of where the user clicked"""
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        column_width = int(width / self._columns)
        row_width = int(height / self._rows)

        cell_column = int(event.x / column_width)
        cell_row = int(event.y / row_width)

        self._keep_score()
        # self._current_board.print_board()
        try:
            self._othello_game.drop_valid_piece(cell_column, cell_row)
        except ValueError:
            print('Invalid Move')
        except othello_logic.GameOverError:
            print('Game Over')
            self._game_over = True
            self._canvas.unbind('<Button-1>')

        # self._current_board.print_board()

        self._draw_circles()
        self._keep_score()

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        """Resize objects on the board"""
        print('resizing')
        self._canvas.delete(tkinter.ALL)

        self._draw_lines()
        self._draw_circles()
        self._keep_score()

    def _draw_lines(self) -> None:
        """draw the board lines"""
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        column_width = int(canvas_width / self._columns)
        row_width = int(canvas_height / self._rows)

        # column lines
        for i in range(0, self._columns):
            self._canvas.create_line(
                i * (column_width), 0, i * (column_width), canvas_height)
        # row lines
        for i in range(0, self._rows):
            self._canvas.create_line(
                0, i * row_width, canvas_width, i * row_width)

    def _draw_circles(self) -> None:
        """draw the pieces based on game logic"""
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        column_width = int(width / self._columns)
        row_width = int(height / self._rows)

        board = self._current_board.get_board()

        for column in board:
            for cell in column:
                if type(cell) == othello_logic.Piece:
                    cell_column = cell.get_col()
                    cell_row = cell.get_row()
                    if cell.get_color() == othello_logic.BLACK:
                        self._canvas.create_oval((cell_column * column_width,
                                                  cell_row *
                                                  row_width, (cell_column +
                                                              1) * column_width,
                                                  (cell_row + 1) * row_width), fill='black')
                    elif cell.get_color() == othello_logic.WHITE:
                        self._canvas.create_oval((cell_column * column_width,
                                                  cell_row *
                                                  row_width, (cell_column +
                                                              1) * column_width,
                                                  (cell_row + 1) * row_width), fill='white')

    def _keep_score(self) -> None:
        """keep the score of the number of pieces, determine turn, display winner"""
        self._score.delete(tkinter.ALL)
        width = self._score.winfo_width()
        height = self._score.winfo_height()
        win_type = self._win_type

        white = self._othello_game.num_white_piece()
        black = self._othello_game.num_black_piece()
        current_player = self._othello_game.get_current_player()

        if not self._game_over:
            self._score.create_text(width / 2, height / 2, text=get_turn(current_player),
                                    fill='white', font=("Purisa", 27))
        else:
            if white == black:
                self._score.create_text(width / 2, height / 2, text='TIE GAME',
                                        fill='white', font=("Purisa", 27))
            elif win_type == 'Most':
                if white > black:
                    self._score.create_text(width / 2, height / 2, text='Winner is WHITE!!!',
                                            fill='white', font=("Purisa", 27))
                elif black > white:
                    self._score.create_text(width / 2, height / 2, text='Winner is BLACK!!!',
                                            fill='white', font=("Purisa", 27))
            elif win_type == 'Least':
                if white < black:
                    self._score.create_text(width / 2, height / 2, text='Winner is WHITE!!!',
                                            fill='white', font=("Purisa", 27))
                elif black < white:
                    self._score.create_text(width / 2, height / 2, text='Winner is BLACK!!!',
                                            fill='white', font=("Purisa", 27))
        self._score.create_oval(0 + 15, 0 + 15, 0 + 85,
                                height - 15, fill='white')
        self._score.create_oval(
            width - 85, 0 + 15, width - 15, height - 15, fill='black')

        self._score.create_text(50, 50, text=white,
                                fill='black', font=("Purisa", 27))
        self._score.create_text(width - 50, 50, text=black,
                                fill='white', font=("Purisa", 27))
        #print(white, black, current_player)

    def start(self) -> None:
        """ Starts the Othello application. Will close when window is closed"""
        self._root_window.mainloop()


def get_turn(current_player: str) -> str:
    """Prints turn on board"""
    if current_player == 'O':
        return ("white's turn")
    elif current_player == 'X':
        return ("black's turn")


if __name__ == '__main__':
    OthelloOptions()
