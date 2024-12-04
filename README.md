# mic_mini_project
This is the final project for CS 6388 Model Integrated Computing (Vanderbilt University).
## Description
This project is a WebGme Design Studio for playing the game [Othello/ Reversi](https://en.wikipedia.org/wiki/Reversi). WebGME is a web-based, collaborative meta-modeling environment with centralized version-controlled model storage. I used WebGme to make a meta-model of the Othello game consisting of concepts such as a board, tile, piece, etc and pointers such as currentPlayer, currentMove, etc. To read more about meta-modeling, visit this [website](https://webgme.readthedocs.io/en/latest/meta_modeling/what_is_meta_modeling.html). Next, I created plugins using the icore visualizer in WebGme. Plugins are custom extension points to a webgme-deployment that are intended to be used querying, interpreting, providing functionality and building models. The framework and API are designed to enable both server- and browser-side execution of the same code. At the point where a plugin is executed it will have access to the context it was invoked and webgme APIs such as core. The plugins I made for successful play of the game are highlight valid tiles, flip tiles, and count pieces. Additionally, the auto and undo plugins provide some interesting functionality. 
## Othello meta-model
<img width="640" alt="Screenshot 2023-12-08 at 8 33 49 AM" src="https://github.com/sanjana3012/mic_mini_project/assets/143513691/20824210-efa5-4e6a-808b-f5276dac999b">

### Concepts:
- Game: A general game class containing gamestates.It points to the current gamestate using the currentGS pointer.

- GameState: A class containing attributes, constraints, and aspects related to the game's current state, with a recursive association to itself, indicating a tracking of previous game states. Additionally, it points to the current player (last played player) and current move (last piece placed) using the currentPlayer and currentMove pointers.

- OthelloGameState: A subclass of GameState, tailored for the specific attributes and rules of Othello.

- Board: Associated with GameState, representing the game board. It has an aggregation relationship with Tile, suggesting the board is composed of tiles.

- Tile: A class with integer attributes column and row, representing its position on the board. It has an association with Piece, implying that a tile can hold a game piece.

- Piece: A class with a color attribute as a string, which is associated with the mightFlip connection, indicating the action pieces might perform during the game.

- Player: A class with a color attribute to denote player pieces, associated with Game, indicating that a game involves players.

- mightFlip: A connection class, representing the action of flipping opponent pieces in Othello.

## Plugins
- Highlight valid tiles for the next move : at each state of the game, the valid tiles for the current player are highlighted. A list of valid tiles is printed [[row, column]]
- Counting pieces: at any state of the game, the number of black and white pieces are counted and printed. First black pieces are logged then the white ones are logged.
- Flipping:  Given the last piece put onto the board, the next state of the game is generated after flipping all the necessary pieces.
- Undo : Takes the game back to the previous state, allowing the last user to make a different move. 
- Auto: Implements a computer mechanism that can play the game, and if this functionality is used, then it makes a valid move.



## Installation
### Prerequisites
First, you need to install the following for the Webgme project to work:
- git using homebrew
  ```
  brew install git

  ```
- [NodeJS](https://nodejs.org/en/) (LTS recommended)
- [Python](https://www.python.org/)
- [Docker desktop](https://www.docker.com/products/docker-desktop/)
- MongoDB. Pull the mongodb image in docker desktop and make a new container fro.
  - Steps to create a new container from the image:
    - Click the run button beside the mongo image and set the optional settings

Give a name to your container. I gave it sanjanadb.
Set host path as :

```
/Users/yourname/DB
```
Where DB is a folder I created to store all the database contents.
​Set the Container path as

```
/data/db
```
### Dependencies and deployment
Once you have all the preqreuisities, we can get to the fun part!
- To run my project, first clone it using :

```
git clone https://github.com/sanjana3012/mic_mini_project.git

```
- Install webgme and webgme cli:

```
npm install webgme
npm install -g webgme-cli
    
```
- Navigate to the project using cd and install the following dependencies:
```
npm i
npm i webgme-bindings   / pip install webgme-bindings

```
- Start mongodb container in the docker desktop
- Start the webgme server using:
```
node app.js
```
or
```
webgme start
```
- copy http://127.0.0.1:8888 to your browser
- Tada!! You are looking at my project now. Select the new_project to play with the plugins. Two states have already been created for you!
  
<img width="899" alt="Screenshot 2023-12-08 at 2 13 20 PM" src="https://github.com/sanjana3012/mic_mini_project/assets/143513691/04c7f004-8bf3-43d8-926a-5142c9719b85">

## Where to run the plugins
- The highlight valid tiles, count pieces, auto and undo can be run from the games folder.
- The flip tiles has to be run from a tile in the board of a gamestate

## Some extra notes
- The current player and current move actually point to the last placed player and last placed piece not to the player that is about to play or the move that is about to be placed.
- In the games folder, you may need to make to sure that the currentGS pointer points to a gamestate if you delete the current gamestate from the object browser. If you delete a state using undo it will be fine.
- My auto works correctly now!!!

## Steps I used to create my webgme project, seeds, etc
- To create your own project and work with it you will need to do all of the above steps except cloning my git repo.
  ```
  webgme init <project_name>

  ```
- Navigate to the project directory, install the dependencies using the above steps then create a new seed using:
  
```
  webgme new seed -n <seed_name> -f <file_name.webgmex> <project_name>

```
- To create a new plugin :
  ```
  webgme new plugin --language Python <pluginID>
  
  ```
- To create a new visualizer:
  ```
  webgme new viz <vizID>
  ```

  

  





