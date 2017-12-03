# Reversi

This is a Python program for playing **Othello** (or **Reversi**) against an AI player.

This project is developed on Ubuntu 16.04 LTS.

## Requirements

- [Python 3.6](https://www.python.org/downloads/release/python-363/)
- [TkInter](https://www.python.org/download/mac/tcltk/)

## How to Run

1. Download all the files [here](https://github.com/JRChow/Reversi).

2. Unzip.

3. Open Terminal, `cd` into this directory and type:

   ```shell
   python3.6 reversi_gui.py
   ```

> Please note that a command-line version of the game is also available. To run the command-line version, type:
>
> ```Shell
> python3.6 reversi_cmd_line.py
> ```

## Rules

### Basic Rules

Each **reversi piece** has a black side and a white side. On your turn, you place one piece on the board with your color facing up. You must place the piece so that an opponent's piece, or a row of opponent's pieces, is flanked by your pieces. All of the opponent's pieces between your pieces are then turned over to become your color. 

### Aim of the Game

The object of the game is to own more pieces than your opponent when the game is over. The game is over when neither player has a move. Usually, this means the board is full. 

### Start of the Game

The game is started in the position shown below on a reversi board consisting of 64 squares in an 8x8 grid. 

![start](/img/start.png)

### Playing the Game

A move consists of placing one piece on an empty square.	

#### Capture

You can capture vertical, horizontal, and diagonal rows of pieces. Also, you can capture more than one row at once. 

### End of the Game

The game ends when: 

- One player wins, by making his color dominant on the board.The players agree to finish the game (as a resignation, or a draw).
- One player wins, by making his color dominant on the board.The players agree to finish the game (as a resignation, or a draw).

## Methodology

### Search Engine

### Alpha-beta Pruning

### Heuristics Applied

#### Coin Parity

#### Mobility

#### Corners Captured

#### Corner Closeness

### Evaluation Function

## Future Releases

## Reference

http://www.flyordie.com/games/help/reversi/en/games_rules_reversi.html
