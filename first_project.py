# -*- coding: utf-8 -*-

# This program is for my school for the class of AI
import random

from functions import most_common, less_common

'''
Rules
1. CI AND CO > 1
2. R_MAX > R_N
3. NA* < CO
'''
# We take all the data and assing them to a varibles
colors = ['Azul', 'Verde', 'Rojo', 'Negro', 'Morado', 'Amarillo', 'Blanco', 'Cafe', 'Gris', 'Naranja', 'Rosa', 'Dorado', 'Plateado']
# colors_2 = []
# colors_3 = []
# colors_4 = []
# colors_5 = []
# colors_6 = []
# colors_7 = []
# colors_8 = []
# colors_9 = []

cities_number = int(input('Cuantas ciudades se ubican en el mapa? \n'))
color_number = int(input('Cuantos colores se van a utilizar? \n'))

# We assert tha this varibles aprove the first rule
while cities_number < 2 or color_number < 2:
    print('Deben existir por lo menos dos ciudades y dos colores \n')
    cities_number = int(input('Cuantas ciudades se ubican en el mapa? \n'))
    color_number = int(input('Cuantos colores se van a utilizar? \n'))

relationships_number = int(input('Cuantas relaciones existen entre las ciudades? \n'))

while True:
    r_max = 0
    for r in range(cities_number):
        r_max = r_max + r
    if relationships_number > r_max:
        print('\nEl numero de relaciones seleccionadas supera el numero de las posibles relaciones, es decir coloca un numero menor de relaciones para continuar o incrementa el numero de ciudades. \n')
        cities_number = int(input('Cuantas ciudades se ubican en el mapa? \n'))
        relationships_number = int(input('Cuantas relaciones existen entre las ciudades? \n'))
    else:
        print(r_max)
        break

relations_incomplete = []
relations_complete = []
nodes = []
nodes_4 = []

for relation in range(relationships_number):
    the_relation = input('Dame los nodos que se relacionan, separados por una coma: \n')
    relations_incomplete.append(the_relation)

for relation in relations_incomplete:
    relations_complete.append({})
    for node in relation:
        nodes.append(node)
        nodes_4.append(node)
        for dic in relations_complete:
            if len(dic) < 2:
                dic[node] = 'default'

colors_t_ch = random.sample(colors, color_number)

a_test = []
for color in colors_t_ch:
    a_test.append(color)

for i in range(color_number):

    colors_t_ch_2 = colors_t_ch
    colors_t_ch_3 = colors_t_ch

    # Here we select the main color and the main node
    mn = int(most_common(nodes))
    print mn
    if len(colors_t_ch_2) >= 1:
        mc = random.choice(colors_t_ch_2)
    print mc

    second_color = []
    for color in colors_t_ch_3:
        if color != mc:
            second_color.append(color)
            print second_color

    # Here we assing the main color to the main node
    for dic in relations_complete:
        if dic.has_key(mn):
            dic[mn] = mc
        print dic

        for node, colors in dic.items():
            if dic.has_key(mn) and colors == 'default':
                if len(second_color) >= 1:
                    dic[node] = second_color[0]

    for node in nodes:
        if node == mn:
            nodes.remove(mn)

    if len(colors_t_ch_2) >= 1:
        colors_t_ch_2.remove(mc)

for i in range(color_number):
    colors_t_ch_2 = a_test
    colors_t_ch_3 = a_test

    minor_n = int(less_common(nodes_4))
    print minor_n
    mn = int(most_common(nodes_4))
    print mn
    if len(colors_t_ch_2) > 1:
        minor_c = random.choice(colors_t_ch_2)
        for dic in relations_complete:
            if dic.has_key(mn):
                while True:
                    if dic[mn] != minor_c:
                        break
                    else:
                        minor_c = random.choice(colors_t_ch_2)

    print minor_c

    second_color = []
    for color in colors_t_ch_3:
        if color != minor_c:
            second_color.append(color)
            print second_color

    for dic in relations_complete:
        if dic.has_key(minor_n):
            dic[minor_n] = minor_c
        print dic

        for node, colors in dic.items():
            if dic.has_key(minor_n) and colors == 'default':
                if len(second_color) >= 1:
                    dic[node] = second_color[0]

    for node in nodes:
        if node == minor_n:
            nodes_4.remove(minor_n)
            print nodes_4
        elif node == mn:
            nodes_4.remove(mn)
            print nodes_4

    if len(colors_t_ch_2) > 1:
        colors_t_ch_2.remove(minor_c)


# print a_test

# a_color_list = []
#
# for dic in relations_complete:
#     for this_color in a_test:
#         for node, colors in dic.items():
#             a_color_list.append(colors)
#             # for color in a_color_list:
#             #     if color != this_color:
#             #         color = this_color
#             print dic

print relations_complete


# print relations_complete

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
            print(node, ':', dic[node])

            if nodes_3 != 0:
                nodes_3.remove(node)
# print (relations_incomplete)
# print (relations_complete)
# print nodes
#print(cities_number, type(color_number))
