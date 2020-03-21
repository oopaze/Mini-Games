import pygame
import time
from random import choice
from bubble_bar_constant import *



def getting_pos(pos_barras):
    x_barra_tirar, y_barra_tirar = pos_barras[contador_matriz][contador_barra][0], pos_barras[contador_matriz][contador_barra][1]
    x_barra_tirar, y_barra_tirar = round(x_barra_tirar/90), int((y_barra_tirar/30)-1)
    
    return (y_barra_tirar, x_barra_tirar)

def save_weights(a, season):
    try:
        arq_w = open("w.ini", "a")
        arq_w.write("{}|{}|{}|{}|{}|\n".format(a.b, a.w[0], a.w[1], a.w[2], season))
        arq_w.close()
    except FileNotFoundError:
        arq_w = open("w.ini", "w")
        arq_w.write("")
        arq_w.close()

def data_base_test(data):
    arq_w = open("DataBase.ini", "a")
    arq_w.write("{}|{}|{}|{}|\n".format(data[0], data[1], data[2], data[3]))
    arq_w.close()

def training_nw(inputs, output, nw):
    nw.training_loop(inputs, output)
    return round(nw.output)

def output_right(bola_pos, movimento, base_pos):
    x, y = bola_pos
    x_move, y_move = movimento
    x_base, y_base = base_pos
    x_base, x = x_base, x-100
    x_movimento, y_movimento = x-x_base, y-y_base
    if x_move != 0 and y_move != 0:
        x_movimento_vezes, y_movimento_vezes = x_movimento/x_move, y_movimento/y_move
    
        x_result, y_result = x_movimento_vezes*x_move, y_movimento_vezes*y_move
        if x < 500 or x > 0:
            if x_result > 0:
                x_result = 1
            else:
                x = -x
                x_base = -x_base
                x_result = 0
            return [x, x_move, x_base, x_result]
    return [2, 2]


pygame.init()
legenda_tela = pygame.display.set_caption("Jogo de Blocos")
font = pygame.font.SysFont('Calibri', 25, True, False)


#ball moviment variables 
move_random_x = [10]
move_random_y = [0]

#movement control variables
control_move = 2
ball_speed = 10
barra_speed = 80
barra_colidida = []

#variables to control the train
trained_w = []
train = 0
count_train = 0


player_control = True
control = True

while control:
    
    #Moving our ball and updating its position 
    bola = bola.move(x_move, y_move)
    x += x_move
    y += y_move
        
    #reading the event of onboard if the user do not want to leave the NN play the Game
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            control = False
        
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and x_barra < 379:
                x_barra += 80
                barra_base = barra_base.move(80, 0)

            if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and x_barra > 20:
                x_barra += -80
                barra_base = barra_base.move(-80, 0)
    
    #Reading the NN output to move our base bar
    if control_move == 1 and x_barra < 500:
        x_barra += barra_speed
        barra_base, control_move = barra_base.move(barra_speed, 0), 2
    elif control_move == 0 and x_barra > -79:
        x_barra += -barra_speed
        barra_base, control_move = barra_base.move(-barra_speed, 0), 2

    #Creating de bola space
    pos_barra_base = [list(range(x_barra, x_barra+201)), list(range(379, 400))]
    pos_ball_x = list(range(x, x+21))
    pos_ball_y = list(range(y, y+21))

    #Testing if ball had kick on each block
    contador_matriz = 0
    for k in pos_barras:
        contador_barra = 0
        for i in k:
            list_x = list(range(i[0], i[0]+81))
            for j in list_x:
                if j in pos_ball_x and (i[1]+20 in pos_ball_y or i[1] in pos_ball_y): 
                    #getting the position of the touched bar
                    y_barra_tirar, x_barra_tirar = getting_pos(pos_barras)
                    #move putting our bar out of the screen
                    barras[y_barra_tirar][x_barra_tirar] = barras[y_barra_tirar][x_barra_tirar].move(-1000, -1000) 
                    #updating their position on control variable
                    pos_barras[y_barra_tirar][x_barra_tirar][0] -= 1000
                    pos_barras[y_barra_tirar][x_barra_tirar][1] -= 1000
                    #add the indexes of our colided bar in our list control 
                    barra_colidida.append([y_barra_tirar, x_barra_tirar])

                    #summing more one score for that
                    pontos += 1
                    #making the control colision variables True
                    ball_colisao = True
                    barra_colisao = True

                    ball_speed = 1.003*ball_speed
                    #Changing the ball moviment variation (direction)
                    move_random_y = [round(ball_speed)]
                    move_random_x = [-round(ball_speed), -round(ball_speed)+5, round(ball_speed), round(ball_speed)-5]
        
            contador_barra += 1
        contador_matriz += 1

    #Testing if the ball touch the base bar
    for i in pos_barra_base[0]:
        for j in pos_barra_base[1]:
            if i in pos_ball_x and (j-20 in pos_ball_y):
                ball_colisao = True
                barra_base_colisao = True
                move_random_y = [-round(ball_speed)]
                move_random_x = [-round(ball_speed), -round(ball_speed)+5, round(ball_speed), round(ball_speed)-5]


    if (x > 560 or x < 20) or (y < 20 or y > 379):
        if x > 560: #getting a new direction to front
            move_random_x = move_random_x = [-round(ball_speed), -round(ball_speed)+5]
        elif x < 20: #getting a new direction to front
            move_random_x = [round(ball_speed), round(ball_speed)-5]
        if y < 20: #getting a new direction to down 
            move_random_y = [round(ball_speed)]
        elif y > 379: #Rebooting our game

            #Putting our base bar in its start position 
            x_barra, y_barra, move_random_x = 200, 370, [0]  
            barra_base = pygame.Rect(x_barra, y_barra, 200, 20)
            
            #Putting our ball in its start speed 
            ball_speed = 10
            x, y, x_move, y_move = 290, 150, 0, 0
            bola = pygame.Rect(x, y, 20, 20)
            
            #Updating our highscore
            if pontos > highscore:
                highscore = pontos
            
            #updating our label values
            season = 1
            pontos = 0
            tentativas += 1
            
            #putting our upside bars in their start position
            for e in barra_colidida:
                barras[e[0]][e[1]] = barras[e[0]][e[1]].move(1000, 1000)
                pos_barras[e[0]][e[1]][0] += 1000
                pos_barras[e[0]][e[1]][1] += 1000
            barra_colidida = []

        if not (y > 379):   
            x_move = choice(move_random_x)
            y_move = choice(move_random_y)


    #Putting the upside bars on their places
    if pontos/season == 24 and pontos != 0:
        if season%4 == 0:
            #save the weights to the Neural Network tested
            save_weights(a, season)
        
        #Putting the bars on their places
        for e in range(len(barras)):
            for i in range(len(barras[e])):
                barras[e][i] = barras[e][i].move(1000, 1000)
                pos_barras[e][i][0] += 1000
                pos_barras[e][i][1] += 1000

        season += 1
        barra_colidida = []

    
    #verifying if ball had touch on upside bars
    if ball_colisao and barra_colisao:
        controle = True
        while controle:
            x_move = choice(move_random_x)
            y_move = choice(move_random_y)
            if x_move != 0 and y_move != 0:
                controle = False
        ball_colisao = False
        barra_base_colisao = False

    #verifying if the ball had touch on base bar
    elif ball_colisao and barra_base_colisao:
        controle = True
        while controle:
            x_move = choice(move_random_x)
            y_move = choice(move_random_y)
            if x_move != 0 and y_move != 0:
                controle = False
        ball_colisao = False
        barra_base_colisao = False        
            
    

    #Looking for output and take the NN to train or use
    data = output_right((x, y), (x_move, y_move), (x_barra, y_barra))

    #data[0] = 2 Turnin' unable our NN
    #Training if the game had update less of 1000 times
    if not(player_control):
        if data[0] != 2 and train < 22000:
            if train%20 == 0:
                data_base_test(data)
            a.training_loop(data[:-1], data[-1])
            control_move = round(a.output)
            if train%100 == 0:
                print(train)
                print(a.w)
            

            train += 1
        #use our NN trained 1000 times
        elif train >= 22000 and data[1] != 2:
            train += 1
            a.use(data[:-1])
            control_move = round(a.output)

    #setting our screen  
    RELOGIO.tick(30)
    tela.fill(fundo_tela)
    sup_base.fill(fundo_tela)



    #Getting the upside bars
    for e in range(0, len(barras)):
        for i in range(0, len(barras[e])):
            pygame.draw.rect(tela, choice(choice(CORES)), barras[e][i])
            
    #Getting the upside info        
    text = font.render("Score: {0} | Attempt: {1} | High Score: {2} | Season: {3}".format(pontos, tentativas, highscore, season), True, (0, 0, 0))
    tela.blit(text, [50, 0])
    

    #Drawing our ball and the base bar
    pygame.draw.ellipse(tela, (0, 0, 0), bola)
    pygame.draw.rect(tela, BLACK, barra_base)
    

    pygame.display.update()
pygame.quit()
    
