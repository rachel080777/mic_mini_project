# mic_mini_project
This is the final project for CS 6388 Model Integrated Computing (Vanderbilt University).
# Description
This project is a WebGme Design Studio for playing the game [Othello/ Reversi](https://en.wikipedia.org/wiki/Reversi). WebGME is a web-based, collaborative meta-modeling environment with centralized version-controlled model storage. I used WebGme to make a meta-model of the Othello game consisting of concepts such as a board, tile, piece, etc and pointers such as currentPlayer, currentMove, etc. To read more about meta-modeling, visit this [website](https://webgme.readthedocs.io/en/latest/meta_modeling/what_is_meta_modeling.html). Next, I created plugins using the icore visualizer in WebGme. Plugins are custom extension points to a webgme-deployment that are intended to be used querying, interpreting, providing functionality and building models. The framework and API are designed to enable both server- and browser-side execution of the same code. At the point where a plugin is executed it will have access to the context it was invoked and webgme APIs such as core. The plugins I made for successful play of the game are highlight valid tiles, flip tiles, and count pieces. Additionally, the auto and undo plugins provide some interesting functionality. 
## Othello meta-model
<img width="640" alt="Screenshot 2023-12-08 at 8 33 49 AM" src="https://github.com/sanjana3012/mic_mini_project/assets/143513691/20824210-efa5-4e6a-808b-f5276dac999b">
- Game: A class with unspecified attributes and connections to GameState and Player.

- GameState: A class containing attributes, constraints, and aspects related to the game's current state, with a recursive association to itself, indicating a tracking of previous game states.

- OthelloGameState: A subclass of GameState, tailored for the specific attributes and rules of Othello.

- Board: Associated with GameState, representing the game board. It has an aggregation relationship with Tile, suggesting the board is composed of tiles.

- Tile: A class with integer attributes column and row, representing its position on the board. It has an association with Piece, implying that a tile can hold a game piece.

- Piece: A class with a color attribute as a string, which is associated with the mightFlip connection, indicating the action pieces might perform during the game.

- Player: A class with a color attribute to denote player pieces, associated with Game, indicating that a game involves players.

- mightFlip: A connection class, likely representing the action of flipping opponent pieces in Othello.


## Installation
First, you need to install the following for the Webgme project to work:
- [NodeJS](https://nodejs.org/en/) (LTS recommended)
- [Python] (https://www.python.org/)
- [Docker desktop] (https://www.docker.com/products/docker-desktop/)
- [Mongo] Pull the mongodb image in docker desktop and make a new container from it.
  - Steps to create a new container:
    


Second, start mongodb locally by running the `mongod` executable in your mongodb installation (you may need to create a `data` directory or set `--dbpath`).

Then, run `webgme start` from the project root to start . Finally, navigate to `http://localhost:8888` to start using myproject!

