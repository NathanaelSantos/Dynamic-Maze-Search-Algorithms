import pygame
from constants import *
from game import game

pygame.init()

# cria a tela do menu
menu_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu")


def draw_menu():
    menu_screen.fill(white)

    # desenha um texto "Jogar"
    font = pygame.font.Font(None, 25)


    # desenha um botão "Busca em Profundidade"
    pygame.draw.rect(menu_screen, blue, (280, 50, 280, 50))

    # desenha um texto "Busca em Profundidade"
    text = font.render("Busca em Profundidade", True, white)
    menu_screen.blit(text, (325, 68))

    # desenha um botão "Busca em Largura"
    pygame.draw.rect(menu_screen, blue, (280, 125, 280, 50))

    # desenha um texto "Busca em Largura"
    text = font.render("Busca em Largura", True, white)
    menu_screen.blit(text, (340, 143))

    # desenha um botão "Busca por Custo Uniforme"
    pygame.draw.rect(menu_screen, blue, (280, 200, 280, 50))

    # desenha um texto "Busca por Custo Uniforme"
    text = font.render("Busca por Custo Uniforme", True, white)
    menu_screen.blit(text, (310, 218))

    # desenha um botão "Busca Gulosa
    pygame.draw.rect(menu_screen, blue, (280, 275, 280, 50))

    # desenha um texto "Busca Gulosa"
    text = font.render("Busca Gulosa", True, white)
    menu_screen.blit(text, (365, 293))

    # desenha um botão "Busca A estrela"
    pygame.draw.rect(menu_screen, blue, (280, 350, 280, 50))

    # desenha um texto "Busca A estrela"
    text = font.render("Busca A estrela", True, white)
    menu_screen.blit(text, (355, 368))

    # desenha um botão "Q-Learning"
    pygame.draw.rect(menu_screen, blue, (280, 425, 280, 50))

    # desenha um texto "Q-Learning"
    text = font.render("Q-Learning", True, white)
    menu_screen.blit(text, (380, 443))

    # desenha um botão "Sair"
    pygame.draw.rect(menu_screen, red, (280, 500, 280, 50))

    # desenha um texto "Sair"
    text = font.render("Sair", True, white)
    menu_screen.blit(text, (380, 518))

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
            if 280 <= mouse_pos[0] <= 560 and 50 <= mouse_pos[1] <= 100:
                # Iniciar jogo com busca em profundidade
                menu_running = False
                game(busca=1)

            # Verifica se clicou no botão "Busca em Largura"
            elif 280 <= mouse_pos[0] <= 560 and 125 <= mouse_pos[1] <= 175:
                # Iniciar jogo com busca em largura
                menu_running = False
                game(busca=2)

            # Verifica se clicou no botão "Busca por Custo Uniforme"
            elif 280 <= mouse_pos[0] <= 560 and 200 <= mouse_pos[1] <= 250:
                # Iniciar jogo com busca por custo uniforme
                menu_running = False
                game(busca=3)

            # Verifica se clicou no botão "Busca Gulosa"
            elif 280 <= mouse_pos[0] <= 560 and 275 <= mouse_pos[1] <= 325:
                # Iniciar jogo com busca gulosa
                menu_running = False
                game(busca=4)

            # Verifica se clicou no botão "Busca A estrela"
            elif 280 <= mouse_pos[0] <= 560 and 350 <= mouse_pos[1] <= 400:
                # Iniciar jogo com busca A estrela
                menu_running = False
                game(busca=5)

            # Verifica se clicou no botão "Busca A estrela"
            elif 280 <= mouse_pos[0] <= 560 and 425 <= mouse_pos[1] <= 475:
                # Iniciar jogo com busca A estrela
                menu_running = False
                game(busca=6)

            # Verifica se clicou no botão "Sair"
            elif 280 <= mouse_pos[0] <= 560 and 500 <= mouse_pos[1] <= 550:
                pygame.quit()
                
    # desenha o menu
    draw_menu()