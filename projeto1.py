#!/usr/bin/env python
# -*- coding: utf-8 -*-

#tic tac toe - project1 study python

import os

SQUARE_SPACE_V=5
SQUARE_SPACE_H=9
TABLE_SPACE=30

def draw_x():
    matrix_x=[[0]*SQUARE_SPACE_H]*SQUARE_SPACE_V
    
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

    return x

def draw_o():
    pass

def draw_vertical_line():
    return '|'

def draw_horizontal_line():
    return '_'*TABLE_SPACE

def draw_blank():
    return ' '*SQUARE_SPACE_H

def draw_table(game_table):
    table=''
    count=0
    
    for j in range(0,2):
        for i in range(0,2):
            # if game_table[j] == 1:
            print(count)
            count += 1
            # table += draw_blank()+draw_vertical_line()
        # draw_blank()+'\n'
        print(count)
        count+=1
        # table += draw_horizontal_line()+'\n'
        print(draw_horizontal_line())
        
    for i in range(0,2):
        print(count)
        count += 1
            # table += draw_blank()+draw_vertical_line()
    # draw_blank()+'\n'
    print(count)
    count+=1    
        
    return table

def gretting_display():
    print('_____________________________________')
    print('___________ tic tac toe _____________')
    print('_____________________________________')
    print('')

game_table=[0]*9
game_table[0]=1

if __name__ == "__main__":
    # # pega o tamanho do terminal
    # rows, columns = os.popen('stty size', 'r').read().split()
    # print(rows,columns)

    # FACTOR=0.7
    # TABLE_SPACE = int(int(rows)*FACTOR*2.3)
    # SQUARE_SPACE_V=int((int(rows)*FACTOR)/3.0)
    # SQUARE_SPACE_H=int((int(rows)*FACTOR)/1.3)    
    
    gretting_display()
    print(game_table)
    print(draw_table(game_table))
    print(draw_x())
    