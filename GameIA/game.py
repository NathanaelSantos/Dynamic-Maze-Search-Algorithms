import pygame

pygame.init()

# definindo as dimensões da tela
screen_width = 800
screen_height = 600

# criando a tela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Labirinto")

# definindo as cores
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Define a matriz que representa o labirinto
maze = [[(i, j, 0) for j in range(16)] for i in range(12)]

print(maze)

# definindo a posição inicial do quadrado
x = 0
y = 0

# loop principal do jogo
running = True
while running:
    # eventos do teclado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x > 0:
                x -= 50
            elif event.key == pygame.K_RIGHT and x < screen_width - 50:
                x += 50
            elif event.key == pygame.K_UP and y > 0:
                y -= 50
            elif event.key == pygame.K_DOWN and y < screen_height - 50:
                y += 50

    # Impede que o quadrado ande na diagonal
    if x < 0:
        x = 0
    elif x > screen_width - 50:
        x = screen_width - 50

    if y < 0:
        y = 0
    elif y > screen_height - 50:
        y = screen_height - 50

    # definindo a cor de fundo
    screen.fill(white)

    # desenhando as linhas do labirinto
    cell_size = 50
    for i in range(len(maze)):
        pygame.draw.line(screen, black, (0, i * cell_size), (screen_width, i * cell_size))
    for j in range(len(maze[0])):
        pygame.draw.line(screen, black, (j * cell_size, 0), (j * cell_size, screen_height))
        
    # desenhando o quadrado vermelho
    rect = pygame.Rect(x, y, 50, 50)
    pygame.draw.rect(screen, red, rect)

    # atualizando a tela
    pygame.display.flip()

# finalizando a biblioteca Pygame
pygame.quit()

