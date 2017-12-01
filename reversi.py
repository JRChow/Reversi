"""Games, or Adversarial Search (Chapter 5)"""

from collections import namedtuple
import random

from utils import argmax

infinity = float('inf')
GameState = namedtuple('GameState', 'to_move, utility, board, moves')

# ______________________________________________________________________________


def alphabeta_search(state, game):
    """Search game to determine best action; use alpha-beta pruning.
    As in [Figure 5.7], this version searches all the way to the leaves."""

    player = game.to_move(state)

    # Functions used by alphabeta
    def max_value(state, alpha, beta):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = -infinity
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a), alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = infinity
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a), alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Body of alphabeta_cutoff_search:
    best_score = -infinity
    beta = infinity
    best_action = None
    for a in game.actions(state):
        v = min_value(game.result(state, a), best_score, beta)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action

# ______________________________________________________________________________
# Players for Games


def query_player(game, state):
    """Make a move by querying standard input."""
    print("current state:")
    game.display(state)
    print("available moves: {}".format(game.actions(state)))
    print("")
    move_string = input('Your move? ')
    try:
        move = eval(move_string)
    except NameError:
        move = move_string
    return move

def random_player(game, state):
    """A player that chooses a legal move at random."""
    return random.choice(game.actions(state))

def alphabeta_player(game, state):
    return alphabeta_search(state, game)


# ______________________________________________________________________________
# Some Sample Games


class Game:
    """A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost and a goal
    test. To create a game, subclass this class and implement actions,
    result, utility, and terminal_test. You may override display and
    successors or you can inherit their default methods. You will also
    need to set the .initial attribute to the initial state; this can
    be done in the constructor."""

    def actions(self, state):
        """Return a list of the allowable moves at this point."""
        raise NotImplementedError

    def result(self, state, move):
        """Return the state that results from making a move from a state."""
        raise NotImplementedError

    def utility(self, state, player):
        """Return the value of this final state to player."""
        raise NotImplementedError

    def terminal_test(self, state):
        """Return True if this is a final state for the game."""
        return not self.actions(state)

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return state.to_move

    def display(self, state):
        """Print or otherwise display the state."""
        print(state)

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    def play_game(self, *players):
        """Play an n-person, move-alternating game."""
        state = self.initial
        while True:
            for player in players:
                move = player(self, state)
                state = self.result(state, move)
                if self.terminal_test(state):
                    self.display(state)
                    return self.utility(state, self.to_move(self.initial))


class Reversi(Game):
    """Reversi game."""

    def __init__(self, height=8, width=8):
        self.height = height
        self.width = width
        init_white = [(4, 4), (5, 5)]
        init_black = [(4, 5), (5, 4)]
        moves = [(x, y) for x in range(1, width+1)
                        for y in range(1, height+1)]
        self.initial = GameState(to_move='B', utility=0, board={}, moves=moves)


    def capture_enemy(self, board, move, player, delta_x_y):
        """Returns true if any enemy is captured in the specified direction."""
        enemy = 'B' if player == 'W' else 'W'
        (delta_x, delta_y) = delta_x_y
        x, y = move
        x, y = x + delta_x, y + delta_y
        enemy_count = 0
        while board.get((x, y)) == enemy:
            board[(x, y)] = player  # Flip
            enemy_count += 1
            x, y = x + delta_x, y + delta_y
        if enemy_count > 0:
            return True
        else:
            # Opposite direction
            x, y = move
            x, y = x - delta_x, y - delta_y
            enemy_count = 0
            while board.get((x, y)) == enemy:
                board[(x, y)] = player  # Flip
                enemy_count += 1
                x, y = x + delta_x, y + delta_y
            return enemy_count > 0

    def move_is_valid(self, board, move, player):
        return (self.capture_enemy(board, move, player, (0, 1)) or
                self.capture_enemy(board, move, player, (1, 0)) or 
                self.capture_enemy(board, move, player, (1, -1)) or 
                self.capture_enemy(board, move, player, (1, 1)))

    def actions(self, state):
        return state.moves

    def result(self, state, move):
        # Invalid move
        if move not in state.moves:
            return state
        board = state.board.copy()
        board[move] = state.to_move
        moves = list(state.moves)
        moves.remove(move)
        moves = [mv for mv in moves if self.move_is_valid(state.board, mv, state.to_move)]
        return GameState(to_move=('W' if state.to_move == 'B' else 'B'),
                         utility=self.compute_utility(board, move, state.to_move),
                         board=board, moves=moves)

    def utility(self, state, player):
        return state.utility if player == 'B' else -state.utility

    def terminal_test(self, state):
        return state.utility != 0 or len(state.moves) == 0

    def display(self, state):
        board = state.board
        for y in range(1, self.height + 1):
            for x in range(1, self.width + 1):
                print(board.get((x, y), '.',), end=' ')
            print()

    def compute_utility(self, board, move, player):
        # TODO 
        return 0

game = Reversi()
game.play_game(query_player, random_player)