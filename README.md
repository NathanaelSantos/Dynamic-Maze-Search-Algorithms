![](Maze-IA/Play.png)

![](Maze-IA/meu.png)

## Running AI-Maze-Game with Docker and Xming on Windows

This guide provides step-by-step instructions for running the AI-Maze-Game application using Docker and Xming on a Windows machine.

### Prerequisites

Before you begin, make sure you have the following installed:

- Docker: [Install Docker for Windows](https://docs.docker.com/docker-for-windows/install/)
- Xming: [Download Xming](https://sourceforge.net/projects/xming/files/latest/download)

### Instructions

1. Install Xming by running the `Xming-6-9-0-31-setup` installer.
2. Open a terminal where the Dockerfile is located.
3. Build the Docker image by running the following command: `docker build -t projetoia .`
4. Run the Docker container with Xming by running the following command: `docker run -it --name projetoia -e DISPLAY=host.docker.internal:0 projetoia`
   - Note: Make sure to replace `projetoia` with the name of your Docker image if you used a different name in step 3.
5. Navigate to the Maze-IA directory by running the following command: `cd AI-Maze-Game/ && cd Maze-IA && ls`
6. Run the AI-Maze-Game application by running the following command: `python3 game.py`


## How to Play
- Use the arrow keys to move the player through the maze.
- Press the D key to draw a new wall in the maze.
- Press the F key to finish drawing a wall.

## Creators
#### GUILHERME SANTOS COSTA
![](img/guilherme.jpg)

#### JOSE NATHANAEL SANTOS MATOS 
![](img/nathan.jpg)

#### PEDRO ANTONIO SANTOS LIMA
![](img/pedro.jpg)


## License
This project is licensed under the MIT License.

Remember to replace the example information with relevant information for your project.




