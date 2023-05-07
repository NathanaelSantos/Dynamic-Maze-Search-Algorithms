# Labirinto com Pygame

Este é um projeto que implementa um jogo de labirinto simples utilizando a biblioteca Pygame.

## Requisitos
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


## Como jogar

- Use as teclas de seta para mover o jogador pelo labirinto.
- Pressione a tecla `D` para desenhar uma nova parede no labirinto.
- Pressione a tecla `F` para finalizar o desenho de uma parede.


## Licença

Este projeto está licenciado sob a licença MIT.```

Lembre-se de substituir as informações do exemplo com as informações relevantes para o seu projeto.




