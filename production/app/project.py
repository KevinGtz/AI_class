# -*- coding: utf-8 -*-

import random
from time import clock
from flask import flash

from functions import most_common, less_common

'''
Rules
1. CI AND CO > 1
2. R_MAX > R_N
3. NA* < CO
'''


def process_the_info(c_i, c_o, r_n, t_r):
    # This program is for my school for the class of AI


    # We take all the data and assing them to a varibles
    colors = ['Azul', 'Verde', 'Rojo', 'Negro', 'Morado', 'Amarillo', 'Blanco', 'Cafe', 'Gris', 'Naranja', 'Rosa', 'Dorado', 'Plateado']

    cities_number = int(c_i)
    color_number = int(c_o)

    # We assert tha this varibles aprove the first rule
    if cities_number < 2 or color_number < 2:
        result = 'Deben existir por lo menos dos ciudades y dos colores'
        flash('Cambia los valores')
        return result

    relationships_number = int(r_n)

    while True:
        r_max = 0
        for r in range(cities_number):
            r_max = r_max + r
        if relationships_number > r_max:
            result = 'El numero de relaciones seleccionadas supera el numero de las posibles relaciones, es decir coloca un numero menor de relaciones para continuar o incrementa el numero de ciudades.'
            flash('Cambia los valores')
            return result
        else:
            print('numero maximo de relaciones:\t' ,r_max)
            break

    relations_incomplete = str(t_r).split()
    relations_complete = []
    nodes = []
    nodes_4 = []

    for relation in relations_incomplete:
        relations_complete.append({})
        for node in relation:
            try:
                nodes.append(int(node))
                nodes_4.append(int(node))
                for dic in relations_complete:
                    if len(dic) < 2:
                        dic[int(node)] = 'default'
            except: node

    print nodes

    # mn = int(most_common(nodes)) [WIP: Find a solution in the logic]
    # if int(nodes.count(mn)) > color_number:
    #
    #     flash('Cambia los valores')
    #     result = 'Uno de los nodos posee mas relaciones que los colores posibles a elegir. Tienes que cambiar las relaciones o incrementar el numero de colores.'
    #     return result

    colors_t_ch = random.sample(colors, color_number)

    colors_1 = []
    colors_2 = []
    colors_3 = []
    colors_4 = []
    for color in colors_t_ch:
        colors_1.append(color)
        colors_2.append(color)
        colors_3.append(color)

    for i in range(color_number):

        colors_t_ch_2 = colors_1
        print colors_t_ch_2
        colors_t_ch_3 = colors_2
        print colors_t_ch_3

        # Here we select the main color and the main node
        mn = int(most_common(nodes))
        minor_n = int(less_common(nodes_4))
        print (mn, 'nodo principal')
        print (minor_n, 'nodo menor')

        if len(colors_t_ch_2) > 1:
            mc = colors_t_ch_2[1]
        elif len(colors_t_ch_2) == 1:
            mc = colors_t_ch_2[0]

        minor_c = colors_t_ch_3[0]


        print (mc, 'color principal')
        print (minor_c, 'color menor')

        # Here we assing the main color to the main node
        for dic in relations_complete:
            for node, colors in dic.items():
                if node == mn and colors == 'default':
                    dic[mn] = mc
                elif node == minor_n and colors == 'default':
                    dic[minor_n] = minor_c

        for i in range(len(nodes)):
            if mn in nodes:
                nodes.remove(mn)
        for i in range(len(nodes_4)):
            if minor_n in nodes_4:
                nodes_4.remove(minor_n)

        if len(colors_t_ch_2) >= 1:
            colors_t_ch_2.remove(mc)
        if len(colors_t_ch_3) >= 1:
            colors_t_ch_3.remove(minor_c)

        print relations_complete

    print relations_complete

    nodes_2 = []
    nodes_3 = []
    result = []

    for relation in relations_incomplete:
        for node in relation:
            try:
                nodes_2.append(int(node))
            except: pass

    for node in nodes_2:
        if node not in nodes_3:
            nodes_3.append(int(node))
    print nodes_3

    for relation in relations_complete:
        for node in relation:
            if node in nodes_3:
                result.append({})
                for dic in result:
                    if len(dic) < 1:
                        dic[node] = relation[node]

                if nodes_3 != 0:
                    nodes_3.remove(node)
    return result
