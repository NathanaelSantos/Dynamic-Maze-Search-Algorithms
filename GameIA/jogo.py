import pygame

# Inicialize o Pygame
pygame.init()

# Defina a largura e altura da tela
largura_tela = 800
altura_tela = 600

# Crie a tela
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Carregue a imagem de fundo
fundo_img = pygame.image.load(r'C:\Users\Nathan\Documents\GameIA\bg.png')

# Defina a posição da imagem de fundo
fundo_pos = (0, 0)

# Defina a posição inicial do jogador
jogador_pos = [largura_tela/2, altura_tela/2]

# Defina a velocidade do jogador
velocidade_jogador = 5

# Defina o loop principal do jogo
terminou = False
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

    # Desenhe a imagem de fundo na tela
    tela.blit(fundo_img, fundo_pos)

    # Desenhe o jogador na tela
    jogador_cor = (255, 0, 0)
    width_jogador = 9
    height_jogador = 9
    jogador_rect = pygame.Rect(jogador_pos[0], jogador_pos[1], width_jogador, height_jogador)
    pygame.draw.rect(tela, jogador_cor, jogador_rect)

    # Verifique se o jogador chegou ao limite da tela
    if jogador_pos[0] < 0:
        jogador_pos[0] = 0
    elif jogador_pos[0] > largura_tela - jogador_rect.width:
        jogador_pos[0] = largura_tela - jogador_rect.width
    if jogador_pos[1] < 0:
        jogador_pos[1] = 0
    elif jogador_pos[1] > altura_tela - jogador_rect.height:
        jogador_pos[1] = altura_tela - jogador_rect.height

    # Atualize a tela do jogo
    pygame.display.update()

# Encerre o Pygame
pygame.quit()
