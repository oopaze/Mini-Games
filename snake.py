from pygame.locals import *
import random
import pygame


SCREEN_SIZE = 500 #Tamanho da tela 
MAPA_SIZE = (SCREEN_SIZE - (SCREEN_SIZE - 60), SCREEN_SIZE - 60) # Tamanho do mapa do jogo

#Constante de cores
AZUL = [(0, 0, 128), (0, 0, 205), (0, 191, 255), (173, 216, 230), (135, 206, 250)]
VERMELHO = [(128,0,0), (139,0,0), (255,99,71), (255,0,0), (178,34,34), (165,42,42)]
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3 #Constantes de moviemnto

SCREEN_POS = list(range(MAPA_SIZE[0], MAPA_SIZE[1], 10)) #Posições na tela em que o maça pode aparecer


pygame.init()

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
bg = random.choice(AZUL)
pygame.display.set_caption("Snake v1.0")

mapa = pygame.Surface((MAPA_SIZE[1], MAPA_SIZE[1]))

#Informações de partida
score = 0
highscore = 0
attempt = 1

font = pygame.font.SysFont('Calibri', 20, True, False)

#Caracteristicas da Cobra
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((0, 0, 0))
snake_direction = LEFT

#Caracteristicas do maça 
apple = (random.choice(SCREEN_POS), random.choice(SCREEN_POS))
apple_skin = pygame.Surface((10, 10))

#Controle dos quadros
clock = pygame.time.Clock()
fps = 10

game_control = True
while game_control:
    clock.tick(round(fps)) #Limitando a taxa de quadros

    for event in pygame.event.get():
        if event.type == QUIT: #Fechando game se clicado no Xzin
            game_control = False
    
        if event.type == pygame.KEYDOWN: #Monitorando Teclado
            if event.key == K_w and snake_direction != DOWN: #Vendo se é o W
                snake_direction = UP
            elif event.key == K_s and snake_direction != UP: #Vendo se é o S
                snake_direction = DOWN
            elif event.key == K_a and snake_direction != RIGHT: #Vendo se é o A
                snake_direction = LEFT
            elif event.key == K_d and snake_direction != LEFT: #Vendo se é o D
                snake_direction = RIGHT
    
    for i in range(len(snake)-1, 0, -1): #Construindo movimento de cada pedaço da cobra
        snake[i] = snake[i-1]
        
    #Movendo a cobra de acordo com a direção
    if snake_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)

    elif snake_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)

    elif snake_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    elif snake_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    #Dando cor ao mapa
    mapa.fill((255, 255, 255))
    
    #Testando colisão da cobra com o maça
    if apple in snake:
        apple = (random.choice(SCREEN_POS), random.choice(SCREEN_POS))
        snake.append((0, 0))
        fps += fps * 0.01
        score += 1
        bg = random.choice(AZUL)

    #Testando colisao da cobra com paredes ou ela mesma e reiniciando o game 
    if snake[0] in snake[1:] or snake[0][0] in [-10, MAPA_SIZE[1]] or snake[0][1] in [-10, MAPA_SIZE[1]]:
        snake = [(200, 200), (210, 200), (220, 200)]
        snake_direction = LEFT
        fps = 10
        
        if score > highscore:
            highscore = score

        attempt += 1
        score -= score
    

    #Plotando cobra na tela
    for pos in snake:
        mapa.blit(snake_skin, pos)
    
    
    #Plotando maça na tela
    apple_skin.fill(random.choice(VERMELHO))
    mapa.blit(apple_skin, apple)
    screen.fill(bg)
    screen.blit(mapa, (30, 30))    
    text = font.render("Score: {0} | Attempt: {1} | High Score: {2} | Dificulty: {3}".format(score, attempt, highscore, round(fps-9, 2)), True, (255, 255, 255))   
    screen.blit(text, (30, 5))

    #Colocando mapa na tela
    
    pygame.display.update()
    
    

pygame.quit()


