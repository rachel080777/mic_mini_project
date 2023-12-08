# myproject
## Installation
First, you need to install the following for the Webgme project to work:
- [NodeJS](https://nodejs.org/en/) (LTS recommended)
- [Python] https://www.python.org/
- [Docker desktop] https://www.docker.com/products/docker-desktop/
- [Mongo] Pull the mongodb image in docker desktop and make a new container from it.
  - Steps to create a new container:
    


Second, start mongodb locally by running the `mongod` executable in your mongodb installation (you may need to create a `data` directory or set `--dbpath`).

Then, run `webgme start` from the project root to start . Finally, navigate to `http://localhost:8888` to start using myproject!

