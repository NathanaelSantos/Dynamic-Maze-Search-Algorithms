import pygame

pygame.init()

# definindo as dimensões da tela
screen_width = 800
screen_height = 600

# cria a tela do menu
menu_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu")

# criando a tela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Labirinto")

# definindo as cores
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)

def draw_menu():
    menu_screen.fill(white)

    # desenha um texto "Jogar"
    font = pygame.font.Font(None, 25)


    # desenha um botão "Busca em Profundidade"
    pygame.draw.rect(menu_screen, blue, (280, 100, 280, 50))

    # desenha um texto "Busca em Profundidade"
    text = font.render("Busca em Profundidade", True, white)
    menu_screen.blit(text, (319, 118))

    # desenha um botão "Busca em Largura"
    pygame.draw.rect(menu_screen, blue, (280, 200, 280, 50))

    # desenha um texto "Busca em Largura"
    text = font.render("Busca em Largura", True, white)
    menu_screen.blit(text, (340, 218))

    # desenha um botão "Busca por Custo Uniforme"
    pygame.draw.rect(menu_screen, blue, (280, 300, 280, 50))

    # desenha um texto "Busca por Custo Uniforme"
    text = font.render("Busca por Custo Uniforme", True, white)
    menu_screen.blit(text, (310, 318))

    # desenha um botão "Sair"
    pygame.draw.rect(menu_screen, red, (280, 400, 280, 50))

    # desenha um texto "Sair"
    text = font.render("Sair", True, white)
    menu_screen.blit(text, (400, 418))

    pygame.display.update()



# loop principal do menu
menu_running = True
while menu_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
             # Verifica se clicou no botão "Busca em Profundidade"
            if 280 <= mouse_pos[0] <= 560 and 100 <= mouse_pos[1] <= 150:
                # Iniciar jogo com busca em profundidade
                menu_running = False

            # Verifica se clicou no botão "Busca em Largura"
            elif 280 <= mouse_pos[0] <= 560 and 200 <= mouse_pos[1] <= 250:
                # Iniciar jogo com busca em largura
                game_loop("breadth")

            # Verifica se clicou no botão "Busca por Custo Uniforme"
            elif 280 <= mouse_pos[0] <= 560 and 300 <= mouse_pos[1] <= 350:
                # Iniciar jogo com busca por custo uniforme
                game_loop("uniform")

            # Verifica se clicou no botão "Sair"
            elif 280 <= mouse_pos[0] <= 560 and 400 <= mouse_pos[1] <= 450:
                pygame.quit()
                sys.exit()
                
    # desenha o menu
    draw_menu()

keys = pygame.key.get_pressed()

# Define a matriz que representa o labirinto
maze = [[(i, j, 0) for j in range(16)] for i in range(12)]

# Cria uma lista de cores para cada célula do labirinto
cell_colors = [[white for j in range(16)] for i in range(12)]

# definindo a posição inicial do quadrado
x = 0
y = 0

speed = 50
row_final = 11
col_final = 15

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

# loop principal do jogo
running = True
while running:
    # eventos do teclado
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            
            
            # verifica se a célula atual está marcada em azul
            row = y // cell_size
            col = x // cell_size
            if maze[row][col][2] == 1:
                # se estiver marcada em azul, mantém a posição anterior do quadrado vermelho
                x, y = old_x, old_y

            # salva a posição atual do quadrado vermelho
            old_x, old_y = x, y
            
            if event.key == pygame.K_LEFT and x > 0:
                x -= speed
            elif event.key == pygame.K_RIGHT and x < screen_width - 50:
                x += speed
            elif event.key == pygame.K_UP and y > 0:
                y -= speed
            elif event.key == pygame.K_DOWN and y < screen_height - 50:
                y += speed
            elif event.key == pygame.K_b: # ativa/desativa o modo de pintura ao pressionar a tecla 'b'
                    paint_mode = not paint_mode
                    # Atualiza a cor de cada célula na lista de cores
                    for i in range(len(maze)):
                        for j in range(len(maze[0])):
                            if maze[i][j][2] == 1:
                                cell_colors[i][j] = blue
                            else:
                                cell_colors[i][j] = white
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and paint_mode: # detecta o clique do mouse no modo de pintura
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


        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and paint_mode: # detecta o clique do mouse no modo de pintura
            # Obtém a posição do mouse na tela
            mouse_pos = pygame.mouse.get_pos()
            # Obtém a posição da casa na matriz
            row_final = mouse_pos[1] // cell_size
            col_final = mouse_pos[0] // cell_size
    


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
            elif maze[i][j] == maze[row_final][col_final]:
                cell_surf.fill((204,255,51))
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
