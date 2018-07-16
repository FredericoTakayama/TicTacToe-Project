#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#tic tac toe - project1 study python

import os

SQUARE_SPACE_V=5
SQUARE_SPACE_H=9
TABLE_SPACE=29

def draw_x(pos_x,pos_y,table_matrix):
    # matrix_x=[[0]*SQUARE_SPACE_H]*SQUARE_SPACE_V    
    # x=''    
    # for i in len(matrix_x):
    #     if i < (SQUARE_SPACE_H/2):
    #         x+='\\'
    #     elif i > (SQUARE_SPACE_H/2):
    #         x+='/'
    #     else:
    #         x+='X'

    x=[]
    x += [r'  \   /  ']
    x += [r'   \ /   ']
    x += [r'    X    ']
    x += [r'   / \   ']
    x += [r'  /   \  ']

    for i in range(0,SQUARE_SPACE_V):
        for j in range(0,SQUARE_SPACE_H):
            table_matrix[(pos_x*SQUARE_SPACE_V)+(1*pos_x)+i][(pos_y*SQUARE_SPACE_H)+(1*pos_y)+j]=x[i][j]

def draw_o(pos_x,pos_y,table_matrix):
    o=[]
    o += [r'   ---   ']
    o += [r' /     \ ']
    o += [r'|       |']
    o += [r' \     / ']
    o += [r'   ---   ']

    for i in range(0,SQUARE_SPACE_V):
        for j in range(0,SQUARE_SPACE_H):
            table_matrix[(pos_x*SQUARE_SPACE_V)+(1*pos_x)+i][(pos_y*SQUARE_SPACE_H)+(1*pos_y)+j]=o[i][j]

def draw_vertical_lines(table_matrix):
    for i in range(0,2):
        for j in range(0,SQUARE_SPACE_V*3+2):
            table_matrix[j][(SQUARE_SPACE_H)*(i+1)+(1*i)] = '|'

def draw_horizontal_lines(table_matrix):
    for i in range(0,2):
        for j in range(0,TABLE_SPACE):
            table_matrix[((SQUARE_SPACE_V)*(i+1)+(1*i))][j] = '-'

def draw_number_positions(table_matrix):
    count=1
    for i in range(0,3): # row
        for j in range(0,3): # column
            table_matrix[SQUARE_SPACE_V*i+i][SQUARE_SPACE_H*j+j] = str(count)
            count+=1

def draw_table(game_table):
    # nao serve! ele copia como referencia e depois nao permite mexer um elemento sem mexer
    # table_matrix = [['0']*TABLE_SPACE]*(SQUARE_SPACE_V*3+2) 
    table_matrix = [[' ' for j in range(0,TABLE_SPACE)] for i in range(0, SQUARE_SPACE_V*3+2)]
    # print(len(table_matrix)) # rows
    # print(len(table_matrix[0])) # columns
    # matrix[5*3+2)][30]
       
    draw_vertical_lines(table_matrix)
    draw_horizontal_lines(table_matrix)

    for i in range(0,3):
        for j in range(0,3):
            if game_table[i*3+j] == 1:
                draw_x(i,j,table_matrix)
                
            elif game_table[i*3+j] == 2:
                draw_o(i,j,table_matrix)

    # add number positions
    draw_number_positions(table_matrix)

    drew_table = ''    
    for row in table_matrix:
        for column in row:
            drew_table += column
        drew_table += '\n'

    return drew_table

def gretting_display():
    print('_____________________________________')
    print('___________ tic tac toe _____________')
    print('_____________________________________')
    print('')

game_table=[0]*9
# game_table=[[0]*3]*3

def check_position(position):
    try:        
        return game_table[(int(position)-1)] == 0
    except:
        return False

def check_end_game(game_table):
    '''check if there is a winner or its a tie'''
    for i in range(0,3):
        # check rows:
        if(game_table[i] == game_table[i+1] == game_table[i+2] and game_table[i] != 0):
            return game_table[i] # player wins
        # check columns:
        elif(game_table[i] == game_table[3+i] == game_table[6+i] and game_table[i] != 0):
            return game_table[i] # player wins
    
    if(game_table[0] == game_table[4] == game_table[8] and game_table[4] != 0) or\
        (game_table[2] == game_table[4] == game_table[6] and game_table[4] != 0):
            return game_table[4] # player wins

    for i in range(0,9):
        if(game_table[i] == 0):
            return 0 # didn't finished

    return -1 # tie

if __name__ == "__main__":
    # pega o tamanho do terminal
    # rows, columns = os.popen('stty size', 'r').read().split()
    # print(rows,columns)

    # FACTOR=0.7
    # TABLE_SPACE = int(int(rows)*FACTOR*2.3)
    # SQUARE_SPACE_V=int((int(rows)*FACTOR)/3.0)
    # SQUARE_SPACE_H=int((int(rows)*FACTOR)/1.3)    
    
    player = 0
    # print(game_table) # debug
    gretting_display()
    print(draw_table(game_table))
            
    while(True):        
        text = 'Player %s, please choose a position:' % str(player+1)
        position = input(text)
        os.system('clear')
        # printar o tabuleiro com lugares disponíveis
        try:
            if int(position) > 0 and int(position) <= 9 and check_position(position):
                # valid position
                game_table[int(position)-1] = player+1
                #exchange between players
                player = (player+1)%2
                # print(game_table) # debug        
                gretting_display()
                print(draw_table(game_table))
            else:
                gretting_display()
                print(draw_table(game_table))
                print('Invalid position. Please try again.')    
        except:
            gretting_display()
            print(draw_table(game_table))
            print('Invalid position. Please try again.')
        
        # check if game finished:
        res = check_end_game(game_table)        
        if res == 0:
            continue
        else:
            if res == -1:
                print('Game end: Tie!')
            else:                
                print('Game end: Player %s wins!' % res)
            break
