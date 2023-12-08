# mic_mini_project
This is the final project for CS 6388 Model Integrated Computing (Vanderbilt University).
# Description
This project is a WebGme Design Studio for playing the game [Othello/ Reversi]. (https://en.wikipedia.org/wiki/Reversi). WebGME is a web-based, collaborative meta-modeling environment with centralized version-controlled model storage. I used WebGme to make a meta-model of the Othello game consisting of concepts such as a board, tile, piece, etc and pointers such as currentPlayer, currentMove, etc. To read more about met-modeling go to https://webgme.readthedocs.io/en/latest/meta_modeling/what_is_meta_modeling.html. Next, I created plugins using the icore visualizer in WebGme. Plugins are custom extension points to a webgme-deployment that are intended to be used querying, interpreting, providing functionality and building models. The framework and API are designed to enable both server- and browser-side execution of the same code. At the point where a plugin is executed it will have access to the context it was invoked and webgme APIs such as core. The plugins I made for successful play of the game are for highlighting valid tiles in a gamestate, flipping tiles, and counting pieces on the board at any given state. Additionally, the plugin auto mimicks a computer mechanism playing the game and the undo plugin goes back to the previous gamestate. 

## Installation
First, you need to install the following for the Webgme project to work:
- [NodeJS](https://nodejs.org/en/) (LTS recommended)
- [Python] (https://www.python.org/)
- [Docker desktop] (https://www.docker.com/products/docker-desktop/)
- [Mongo] Pull the mongodb image in docker desktop and make a new container from it.
  - Steps to create a new container:
    


Second, start mongodb locally by running the `mongod` executable in your mongodb installation (you may need to create a `data` directory or set `--dbpath`).

Then, run `webgme start` from the project root to start . Finally, navigate to `http://localhost:8888` to start using myproject!

