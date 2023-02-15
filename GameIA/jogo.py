import pygame

# Inicialize o Pygame
pygame.init()

# Defina a largura e altura da tela
largura_tela = 800
altura_tela = 600

# Crie a tela
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Crie um objeto para controlar a taxa de atualização da tela
clock = pygame.time.Clock()

# Defina as cores a serem utilizadas
cor_fundo = (255, 255, 255)
cor_parede = (0, 0, 0)
cor_jogador = (255, 0, 0)

# Defina a posição inicial do jogador
jogador_pos = [largura_tela/2, altura_tela/2]

# Defina a velocidade do jogador
velocidade_jogador = 20

# Crie uma lista vazia para armazenar as paredes do labirinto
paredes = []

# Defina o loop principal do jogo
terminou = False
desenhando_parede = False  # Flag que indica se o usuário está desenhando uma parede
while not terminou:
    # Verifique os eventos do Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        # Verifique se uma tecla foi pressionada
        if event.type == pygame.KEYDOWN:
            # Move o jogador para a esquerda
            if event.key == pygame.K_LEFT:
                jogador_pos[0] -= velocidade_jogador
            # Move o jogador para a direita
            elif event.key == pygame.K_RIGHT:
                jogador_pos[0] += velocidade_jogador
            # Move o jogador para cima
            elif event.key == pygame.K_UP:
                jogador_pos[1] -= velocidade_jogador
            # Move o jogador para baixo
            elif event.key == pygame.K_DOWN:
                jogador_pos[1] += velocidade_jogador
            # Inicia o desenho de uma parede
            elif event.key == pygame.K_d:
                desenhando_parede = True
            # Finaliza o desenho de uma parede
            elif event.key == pygame.K_f:
                desenhando_parede = False
        # Verifique se o botão do mouse foi pressionado
        elif event.type == pygame.MOUSEBUTTONDOWN and desenhando_parede:
            # Adiciona uma nova parede na lista de paredes
            posicao_mouse = pygame.mouse.get_pos()
            paredes.append(pygame.Rect(posicao_mouse[0], posicao_mouse[1], 30, 30))

    # Preenche o fundo da tela com a cor de fundo
    tela.fill(cor_fundo)

    # Desenha as paredes na tela
    for parede in paredes:
        pygame.draw.rect(tela, cor_parede, parede)

    # Desenha o jogador na tela
    width_jogador = 30
    height_jogador = 30
    jogador_rect = pygame.Rect(jogador_pos[0], jogador_pos[1], width_jogador, height_jogador)
    pygame.draw.rect(tela, cor_jogador, jogador_rect)

    # Atualiza a tela
    pygame.display.update()

    # Defina a taxa de quadros por segundo
    clock.tick(60)

    # Encerre o Pygame
pygame.quit()

