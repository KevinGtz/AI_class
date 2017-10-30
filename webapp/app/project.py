# -*- coding: utf-8 -*-

import random

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
    while cities_number < 2 or color_number < 2:
        print('Deben existir por lo menos dos ciudades y dos colores \n')
        cities_number = int(c_i)
        color_number = int(c_o)

    relationships_number = int(r_n)

    while True:
        r_max = 0
        for r in range(cities_number):
            r_max = r_max + r
        if relationships_number > r_max:
            print('\nEl numero de relaciones seleccionadas supera el numero de las posibles relaciones, es decir coloca un numero menor de relaciones para continuar o incrementa el numero de ciudades. \n')
            cities_number = int(c_i)
            relationships_number = int(c_o)
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
    print 'the nodes are %s' % nodes

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
        colors_t_ch_4 = colors_3
        print colors_t_ch_4

        # Here we select the main color and the main node
        mn = int(most_common(nodes))
        minor_n = int(less_common(nodes))
        print (mn, 'nodo principal')
        print (minor_n, 'nodo menor')

        mc = random.choice(colors_t_ch_2)
        minor_c = random.choice(colors_t_ch_3)

        while mc == minor_c:
                mc = random.choice(colors_t_ch_2)
                minor_c = random.choice(colors_t_ch_3)

        print (mc, 'color principal')
        print (minor_c, 'color menor')

        if color_number > 2:
            second_color_a = random.choice(colors_t_ch_4)
            while second_color_a == mc:
                second_color_a = random.choice(colors_t_ch_4)
            if color_number > 3:
                second_color_b = random.choice(colors_t_ch_4)
                while second_color_b == minor_n:
                    second_color_b = random.choice(colors_t_ch_4)

            print (second_color_a, 'segundo color diferente del color principal y el color menor')



        # Here we assing the main color to the main node
        for dic in relations_complete:
            if dic.has_key(mn):
                dic[mn] = mc
            elif dic.has_key(minor_n):
                dic[minor_n] = minor_c

            print (dic, 'diccionario con los valores')

            for node, colors in dic.items():
                if dic.has_key(mn) and colors == 'default':
                    if node != mn:
                        dic[node] = second_color_a
                        print 'in mn'
                elif dic.has_key(minor_n) and colors == 'default':
                    if color_number > 3:
                        if node != minor_n:
                            dic[node] = second_color_b
                            print 'in minor_nc'
                    else:
                        if node != minor_n:
                            dic[node] = mc
                            print 'in minor_nc'

        for node in nodes:
            if node == mn:
                nodes.remove(mn)
            elif node == minor_n:
                nodes.remove(minor_n)

        if len(colors_t_ch_2) >= 1:
            colors_t_ch_2.remove(mc)
        if len(colors_t_ch_3) >= 1:
            colors_t_ch_3.remove(minor_c)

    print relations_complete

    nodes_2 = []
    nodes_3 = []

    for relation in relations_incomplete:
        for node in relation:
            nodes_2.append(node)

    for node in nodes_2:
        if node not in nodes_3:
            nodes_3.append(node)

    for dic in relations_complete:
        for node in dic:
            if node in nodes_3:
                result = (node, ':', dic[node])
                print result

                if nodes_3 != 0:
                    nodes_3.remove(node)
