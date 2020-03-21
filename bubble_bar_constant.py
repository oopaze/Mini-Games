import pygame

AZUL = [(0, 0, 128), (0, 0, 205), (0, 191, 255), (173, 216, 230), (135, 206, 250)]
VERMELHO = [(189,83,107), (210,105,30), (184,134,11), (255,215,0), (255,255,0), (255,140,0)]
AMARELO = [ (255,160,122), (255,0,0), (178,34,34), (233,150,122), (250,128,114), (128,0,0)]
ROXO = [(148,0,211), (139,0,139), (75,0,130), (186,85,211), (147,112,219), (221,160,221)]
CORES = [AZUL]

pontos = 0
tentativas = 1
highscore = 0
season = 1

X_TELA, Y_TELA = (600, 400)
tela = pygame.display.set_mode([X_TELA, Y_TELA])
fundo_tela = (248, 248, 255)


sup_top = pygame.Surface((600, 150))
pos_sup_top = [0, 30]

sup_base = pygame.Surface((600, 100))
pos_sup_base = [0, 350]

x_barra, y_barra = 200, 370
barra_base = pygame.Rect(x_barra, y_barra, 200, 20)

BLACK = (128, 128, 128)

RELOGIO = pygame.time.Clock()

pos_barra_l1 = [[30, 30], [120, 30], [210, 30], [300, 30], [390, 30], [480, 30]]
pos_barra_l2 = [[30, 60], [120, 60], [210, 60], [300, 60], [390, 60], [480, 60]]
pos_barra_l3 = [[30, 90], [120, 90], [210, 90], [300, 90], [390, 90], [480, 90]]
pos_barra_l4 = [[30, 120], [120, 120], [210, 120], [300, 120], [390, 120], [480, 120]]
pos_barras = [pos_barra_l1, pos_barra_l2, pos_barra_l3, pos_barra_l4]


barras_l1 = [pygame.Rect(pos_barra_l1[0][0], pos_barra_l1[0][1], 80, 20), pygame.Rect(pos_barra_l1[1][0], pos_barra_l1[1][1], 80, 20), pygame.Rect(pos_barra_l1[2][0], pos_barra_l1[2][1], 80, 20), pygame.Rect(pos_barra_l1[3][0], pos_barra_l1[3][1], 80, 20), pygame.Rect(pos_barra_l1[4][0], pos_barra_l1[4][1], 80, 20), pygame.Rect(pos_barra_l1[5][0], pos_barra_l1[5][1], 80, 20)]
barras_l2 = [pygame.Rect(pos_barra_l2[0][0], pos_barra_l2[0][1], 80, 20), pygame.Rect(pos_barra_l2[1][0], pos_barra_l2[1][1], 80, 20), pygame.Rect(pos_barra_l2[2][0], pos_barra_l2[2][1], 80, 20), pygame.Rect(pos_barra_l2[3][0], pos_barra_l2[3][1], 80, 20), pygame.Rect(pos_barra_l2[4][0], pos_barra_l2[4][1], 80, 20), pygame.Rect(pos_barra_l2[5][0], pos_barra_l2[5][1], 80, 20)]
barras_l3 = [pygame.Rect(pos_barra_l3[0][0], pos_barra_l3[0][1], 80, 20), pygame.Rect(pos_barra_l3[1][0], pos_barra_l3[1][1], 80, 20), pygame.Rect(pos_barra_l3[2][0], pos_barra_l3[2][1], 80, 20), pygame.Rect(pos_barra_l3[3][0], pos_barra_l3[3][1], 80, 20), pygame.Rect(pos_barra_l3[4][0], pos_barra_l3[4][1], 80, 20), pygame.Rect(pos_barra_l3[5][0], pos_barra_l3[5][1], 80, 20)]
barras_l4 = [pygame.Rect(pos_barra_l4[0][0], pos_barra_l4[0][1], 80, 20), pygame.Rect(pos_barra_l4[1][0], pos_barra_l4[1][1], 80, 20), pygame.Rect(pos_barra_l4[2][0], pos_barra_l4[2][1], 80, 20), pygame.Rect(pos_barra_l4[3][0], pos_barra_l4[3][1], 80, 20), pygame.Rect(pos_barra_l4[4][0], pos_barra_l4[4][1], 80, 20), pygame.Rect(pos_barra_l4[5][0], pos_barra_l4[5][1], 80, 20)]
barras = [barras_l1, barras_l2, barras_l3, barras_l4]

x, y, x_move, y_move = 290, 150, 0, 10
bola = pygame.Rect(x, y, 20, 20)
ball_colisao = False
barra_colisao = False
barra_base_colisao = False
