import pygame
import csv
import math
from constants import *
import importlib
import os

os.environ['SDL_AUDIODRIVER'] = 'dummy'

pygame.init()


# cria a tela
screen = pygame.display.set_mode((screen_width, screen_height))

# carrega a imagem de fundo
background = pygame.image.load("Play.png")

# ajusta a imagem de fundo ao tamanho da tela
background = pygame.transform.scale(background, (screen_width, screen_height))

# desenha a imagem de fundo na tela
screen.blit(background, (0, 0))

# atualiza a tela
pygame.display.update()

# aguarda 2 segundos
pygame.time.delay(2000)


# cria a tela do menu
menu_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu")

# criando a tela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Labirinto")


# Define a matriz que representa o labirinto
maze = [[(i, j, 0) for j in range(16)] for i in range(12)]
# print(maze[0])

# Cria uma lista de cores para cada célula do labirinto
cell_colors = [[white for j in range(16)] for i in range(12)]


# Defina a lista de coordenadas para o quadrado seguir
coord_list = []

# Define se o modo de pintura está ativo ou não
paint_mode = True

class Color:
    color = (255, 255, 255)
    algoritmo = ""

    @staticmethod
    def get_color():
        return Color.color
    
    @staticmethod
    def set_color(new_color):
        Color.color = new_color

    @staticmethod
    def get_algoritmo_name():
        return Color.algoritmo
    
    @staticmethod
    def set_algoritmo_name(new_algoritmo):
        Color.algoritmo = new_algoritmo


def draw_menu():
    menu_screen.fill(white)

    # desenha um texto "Jogar"
    font = pygame.font.Font(None, 25)


    # desenha um botão "Busca em Profundidade"
    pygame.draw.rect(menu_screen, blue, (280, 55, 280, 45))

    # desenha um texto "Busca em Profundidade"
    text = font.render("Busca em Profundidade", True, white)
    menu_screen.blit(text, (322, 70))

    # desenha um botão "Busca em Largura"
    pygame.draw.rect(menu_screen, blue, (280, 105, 280, 45))

    # desenha um texto "Busca em Largura"
    text = font.render("Busca em Largura", True, white)
    menu_screen.blit(text, (345, 120))

    # desenha um botão "Busca por Custo Uniforme"
    pygame.draw.rect(menu_screen, blue, (280, 155, 280, 45))

    # desenha um texto "Busca por Custo Uniforme"
    text = font.render("Busca por Custo Uniforme", True, white)
    menu_screen.blit(text, (315, 170))

    # desenha um botão "Busca Gulosa"
    pygame.draw.rect(menu_screen, blue, (280, 205, 280, 45))

    # desenha um texto "Busca Gulosa"
    text = font.render("Busca Gulosa", True, white)
    menu_screen.blit(text, (363, 220))


    # desenha um botão "Busca A estrela"
    pygame.draw.rect(menu_screen, blue, (280, 255, 280, 45))

    # desenha um texto "Busca A estrela"
    text = font.render("Busca A*", True, white)
    menu_screen.blit(text, (385, 270))


    # desenha um botão "Q-Learning"
    pygame.draw.rect(menu_screen, blue, (280, 305, 280, 45))

    # desenha um texto "Q-Learning"
    text = font.render("Q-Learning", True, white)
    menu_screen.blit(text, (375, 320))

    # desenha um botão "Sair"
    pygame.draw.rect(menu_screen, red, (280, 355, 280, 45))

    # desenha um texto "Sair"
    text = font.render("Sair", True, white)
    menu_screen.blit(text, (405, 370))

    pygame.display.update()


def menuInicial():
    menu_screen.fill(white)

    # desenha um texto "Jogar"
    font = pygame.font.Font(None, 25)

    # desenha um botão "Importar Save"
    pygame.draw.rect(menu_screen, blue, (280, 55, 280, 45))

    # desenha um texto "Importar Save"
    text = font.render("Importar Save", True, white)
    menu_screen.blit(text, (320, 70))

    # desenha um botão "Desenhar Manualmente"
    pygame.draw.rect(menu_screen, blue, (280, 105, 280, 45))

    # desenha um texto "Desenhar Manualmente"
    text = font.render("Desenhar Manualmente", True, white)
    menu_screen.blit(text, (310, 120))

    # desenha um botão "Gerar Labirinto Automático"
    pygame.draw.rect(menu_screen, blue, (280, 155, 280, 45))

    # desenha um texto "Gerar Labirinto Automático"
    text = font.render("Gerar Labirinto Automático", True, white)
    menu_screen.blit(text, (285, 170))

    # desenha um botão "Sair"
    pygame.draw.rect(menu_screen, red, (280, 355, 280, 45))

    # desenha um texto "Sair"
    text = font.render("Sair", True, white)
    menu_screen.blit(text, (405, 370))

    pygame.display.update()



def draw_cell(row, col):
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

#Cria a lista de tuplas do caminho a ser seguido até o estado final
def read_file_path(arquivo):
    linhas = arquivo.readlines()
    for linha in linhas:
        campos = linha.strip().replace("(", "").replace(")", "").replace(" ","").split(',')
        coord_list.append((int(campos[0]),int(campos[1])))
    return coord_list



def menu():
    # loop principal do menu
    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Verifica se clicou no botão "Busca em Profundidade"
                if 280 <= mouse_pos[0] <= 560 and 55 <= mouse_pos[1] <= 100:
                    # Iniciar jogo com busca em profundidade
                    menu_running = False
                    importlib.import_module('buscaProfundidade')
                    read_file_path(open("Outputs/dfs_path.txt", "r"))

                    Color.set_algoritmo_name('buscaProfundidade')
                    Color.set_color(buscaProfundidadeColor)

                # Verifica se clicou no botão "Busca em Largura"
                elif 280 <= mouse_pos[0] <= 560 and 105 <= mouse_pos[1] <= 150:
                    cor = 1
                    menu_running = False
                    importlib.import_module('buscaLargura')
                    read_file_path(open("Outputs/bfs_path.txt", "r"))
                    
                    Color.set_algoritmo_name('buscaLargura')
                    Color.set_color(buscaLarguraColor)

                # Verifica se clicou no botão "Busca por Custo Uniforme"
                elif 280 <= mouse_pos[0] <= 560 and 155 <= mouse_pos[1] <= 200:
                    menu_running = False
                    importlib.import_module('buscaCustoUni')
                    read_file_path(open("Outputs/djkistra_path.txt", "r"))

                    Color.set_algoritmo_name('buscaCustoUniforme')
                    # atualiza a cor
                    Color.set_color(buscaCustoUniformeColor)

                # Verifica se clicou no botão "Busca Gulosa"
                elif 280 <= mouse_pos[0] <= 560 and 205 <= mouse_pos[1] <= 250:
                    menu_running = False
                    importlib.import_module('buscaGulosa')
                    read_file_path(open("Outputs/greedy_path.txt", "r"))
                    
                    Color.set_algoritmo_name('buscaGulosa')
                    Color.set_color(buscaGulosaColor)

                # Verifica se clicou no botão "Busca A*"
                elif 280 <= mouse_pos[0] <= 560 and 255 <= mouse_pos[1] <= 300:
                    menu_running = False
                    importlib.import_module('buscaAestrela')
                    read_file_path(open("Outputs/A_star_path.txt", "r"))
                    
                    Color.set_algoritmo_name('buscaAestrela')
                    Color.set_color(buscaAestrelaColor)

                # Verifica se clicou no botão "Q-Learning"
                elif 280 <= mouse_pos[0] <= 560 and 305 <= mouse_pos[1] <= 350:
                    menu_running = False
                    importlib.import_module('qLearning')
                    read_file_path(open("Outputs/qLearning_path.txt", "r"))
                    
                    Color.set_algoritmo_name('qLearning')
                    Color.set_color(qLearningColor)

                # Verifica se clicou no botão "Sair"
                elif 280 <= mouse_pos[0] <= 560 and 355 <= mouse_pos[1] <= 400:
                    pygame.quit()
                    
        # desenha o menu
        draw_menu()


# Defina a velocidade de movimentação e o índice atual da lista de coordenadas
coord_index = 0

# exibe a tela de menu inicial

def menuInicial():
    menu_screen.fill(white)

    # desenha um texto "Jogar"
    font = pygame.font.Font(None, 25)

    # desenha um botão "Importar Save"
    pygame.draw.rect(menu_screen, blue, (280, 55, 280, 45))

    # desenha um texto "Importar Save"
    text = font.render("Importar Save", True, white)
    menu_screen.blit(text, (320, 70))

    # desenha um botão "Desenhar Manualmente"
    pygame.draw.rect(menu_screen, blue, (280, 105, 280, 45))

    # desenha um texto "Desenhar Manualmente"
    text = font.render("Desenhar Manualmente", True, white)
    menu_screen.blit(text, (310, 120))


    # desenha um botão "Sair"
    pygame.draw.rect(menu_screen, red, (280, 355, 280, 45))

    # desenha um texto "Sair"
    text = font.render("Sair", True, white)
    menu_screen.blit(text, (405, 370))

    pygame.display.update()

    # loop para esperar um clique do mouse
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 280 <= x <= 560 and 105 <= y <= 150:  # verifica se o botão "Desenhar Manualmente" foi clicado
                    waiting = False
                    running = True
                elif 280 <= x <= 560 and 355 <= y <= 400:  # verifica se o botão "Sair" foi clicado
                    pygame.quit()

menuInicial()

# loop principal do jogo
running = True
visited_coords = []  # Definindo a lista de coordenadas visitadas
while running:
    # eventos do teclado
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:  # ativa/desativa o modo de pintura ao pressionar a tecla 'b'
                paint_mode = not paint_mode
                # Atualiza a cor de cada célula na lista de cores
                for i in range(len(maze)):
                    for j in range(len(maze[0])):
                        if maze[i][j][2] == 1:
                            cell_colors[i][j] = blue
                        else:
                            cell_colors[i][j] = white
            elif event.key == pygame.K_SPACE:
                state_list = verify_state(maze)
                export_csv_vertex(state_list)
                edge_list = verify_edges(state_list)
                export_csv_edges(edge_list)
                paint_mode = False
                menu()



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

    # Movimentação automática
    if coord_index < len(coord_list):
        # Obtém as coordenadas atuais
        current_coord = coord_list[coord_index]

        # Movimenta o jogador em direção às coordenadas atuais
        if x < current_coord[1] * cell_size:
            x += speed
        elif x > current_coord[1] * cell_size:
            x -= speed
        elif y < current_coord[0] * cell_size:
            y += speed
        elif y > current_coord[0] * cell_size:
            y -= speed
        else:
            # Se o jogador chegou às coordenadas atuais, atualize o índice e insira um delay
            coord_index += 1
            visited_coords.append((current_coord[0], current_coord[1]))  # Adicionando as coordenadas visitadas
            pygame.time.delay(500)  # Delay de 500ms (0.5s)
        
            # Verifica se o jogador chegou à coordenada final
            if current_coord == (row_final, col_final):
                current_dir = os.path.abspath(os.path.dirname(__file__))
                image_dir = "img"
                full_path = os.path.join(current_dir, image_dir)
                # save the image with the full path
                pygame.image.save(screen, os.path.join(full_path, Color.get_algoritmo_name() + ".png"))
                print("Print tirado e imagem salva com sucesso!")
                visited_coords = []  # redefine a lista de coordenadas visitadas para vazia


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
            elif maze[i][j] == maze[row_final][col_final]:
                cell_surf.fill((80, 200, 120))
            # Preenche a superfície com a cor branca se a casa não estiver marcada
            else:
                cell_surf.fill(white)
            # Desenha a superfície na tela
            screen.blit(cell_surf, (j * cell_size, i * cell_size))

    # desenhando o quadrado vermelho
    rect = pygame.Rect(x, y, 50, 50)
    pygame.draw.rect(screen, red, rect)
 
    for coord in visited_coords:
        visited_rect = pygame.Rect(coord[1] * cell_size, coord[0] * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, Color.get_color(), visited_rect) 
 
    # desenhando as linhas do labirinto
    for i in range(len(maze)):
        pygame.draw.line(screen, black, (0, i * cell_size), (screen_width, i * cell_size))
    for j in range(len(maze[0])):
        pygame.draw.line(screen, black, (j * cell_size, 0), (j * cell_size, screen_height))

    # atualizando a tela
    pygame.display.update()
