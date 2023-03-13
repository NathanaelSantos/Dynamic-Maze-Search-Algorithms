import pygame
import csv
import math

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
blue = (0, 0, 255)


# definindo a posição inicial do quadrado
x = 0
y = 50

speed = 50

# Define a matriz que representa o labirinto
maze = [[(i, j, 0) for j in range(16)] for i in range(12)]
# print(maze[0])

# Cria uma lista de cores para cada célula do labirinto
cell_colors = [[white for j in range(16)] for i in range(12)]


# Define se o modo de pintura está ativo ou não
paint_mode = True



def draw_cell(row, col):
    cell_size = 50
    cell_surf = pygame.Surface((cell_size, cell_size))
    if maze[row][col][2] == 1:
        cell_surf.fill(blue)
    else:
        cell_surf.fill(white)
    screen.blit(cell_surf, (col * cell_size, row * cell_size))


def verify_state(maze):
    states = []
    cont = 0
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (maze[i][j][2] == 0):
                aux = list(maze[i][j])
                aux.pop(2)
                distance = vertex_distance(tuple(aux), final_pos=(11, 15))
                rounded_distance = round(distance, 2)
                states.append([cont, tuple(aux), rounded_distance])
                cont += 1
    print("State List: ", states)
    return states

def verify_edges(stateList):
    edge_list = []
    for i in stateList:
        current_id = i[0]
        current_pos = i[1]
        #distance = vertex_distance(current_pos, final_pos=(11, 15))
        #rounded_distance = round(distance, 2)
        for j in range(4):
            new_current_pos = verify_adj_vertex(current_pos, j)
            for k in stateList:
                if new_current_pos == k[1]:
                    edge_list.append([current_id, k[0], 1])
    print("Edge List: ", edge_list)
    return edge_list

def verify_adj_vertex(current_pos, direction):
    if direction == 0 and current_pos[0] != 0: #cima
        aux = list(current_pos)
        aux[0] -= 1
        return tuple(aux)
    elif direction == 1 and current_pos[0] != 11: #baixo
        aux = list(current_pos)
        aux[0] += 1
        return tuple(aux)
    elif direction == 2 and current_pos[1] != 0: #esquerda
        aux = list(current_pos)
        aux[1] -= 1
        return tuple(aux)
    elif direction == 3 and current_pos[1] != 15: #direita
        aux = list(current_pos)
        aux[1] += 1
        return tuple(aux)
    
def vertex_distance(current_pos, final_pos):
    distance = math.sqrt((final_pos[0] - current_pos[0])**2 + (final_pos[1] - current_pos[1])**2)
    return distance

def export_csv_vertex(stateList):
    with open("vertex.csv", "w", newline="", encoding="utf-8") as f:
        file = csv.writer(f, delimiter=";")
        file.writerows(stateList)

def export_csv_edges(edgeList):
    with open("edges.csv", "w", newline="", encoding="utf-8") as f:
        file = csv.writer(f, delimiter=";")
        file.writerows(edgeList)

def read_file_path(arquivo):
    tuplas = []
    linhas = arquivo.readlines()
    for linha in linhas:
        campos = linha.strip().replace("(", "").replace(")", "").replace(" ","").split(',')
        tuplas.append((int(campos[0]),int(campos[1])))
    return tuplas
# Como chamar a função - Nathan
#file = open("Outputs/bfs_path.txt", "r")
#path = read_file_path(file)
#print(path)


# loop principal do jogo
running = True
while running:
    # eventos do teclado
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x > 0:
                x -= speed
            elif event.key == pygame.K_RIGHT and x < screen_width - 50:
                x += speed
            elif event.key == pygame.K_UP and y > 0:
                y -= speed
            elif event.key == pygame.K_DOWN and y < screen_height - 50:
                y += speed
            elif event.key == pygame.K_b:  # ativa/desativa o modo de pintura ao pressionar a tecla 'b'
                paint_mode = not paint_mode
                # Atualiza a cor de cada célula na lista de cores
                for i in range(len(maze)):
                    for j in range(len(maze[0])):
                        if maze[i][j][2] == 1:
                            cell_colors[i][j] = blue
                        else:
                            cell_colors[i][j] = white
            # Ativar função de exportar estados ao pressionar espaço
            elif event.key == pygame.K_SPACE:
                state_list = verify_state(maze)
                export_csv_vertex(state_list)
                edge_list = verify_edges(state_list)
                export_csv_edges(edge_list)


        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and paint_mode:  # detecta o clique do mouse no modo de pintura
            # Obtém a posição do mouse na tela
            mouse_pos = pygame.mouse.get_pos()
            # Obtém a posição da casa na matriz
            row = mouse_pos[1] // cell_size
            col = mouse_pos[0] // cell_size
            # Inverte o estado da casa atual
            if maze[row][col][2] == 0:
                maze[row][col] = (row, col, 1)
            else:
                maze[row][col] = (row, col, 0)
            # Desenha a célula
            draw_cell(row, col)

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

    cell_size = 50

    # loop que percorre toda a matriz e desenha cada célula com base em seu estado atual
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            # Cria uma nova superfície com as mesmas dimensões da casa
            cell_surf = pygame.Surface((cell_size, cell_size))
            # Preenche a superfície com a cor azul se a casa estiver marcada
            if maze[i][j][2] == 1:
                cell_surf.fill(blue)
            # Preenche a superfície com a cor branca se a casa não estiver marcada
            else:
                cell_surf.fill(white)
            # Desenha a superfície na tela
            screen.blit(cell_surf, (j * cell_size, i * cell_size))

    # desenhando as linhas do labirinto
    for i in range(len(maze)):
        pygame.draw.line(screen, black, (0, i * cell_size), (screen_width, i * cell_size))
    for j in range(len(maze[0])):
        pygame.draw.line(screen, black, (j * cell_size, 0), (j * cell_size, screen_height))

    # desenhando o quadrado vermelho
    rect = pygame.Rect(x, y, 50, 50)
    pygame.draw.rect(screen, red, rect)

    # atualizando a tela
    pygame.display.update()