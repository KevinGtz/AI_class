# -*- coding: utf-8 -*-

import random

def most_common(lst):
    return max(set(lst), key=lst.count)

def less_common(lst):
    return min(set(lst), key=lst.count)

# Making the code for the first rules stuff

# First Rule Here : The number od CI and CO needs to be more than one
def first_rule(c_i, c_o):
    c_i = int(c_i)
    c_o = int(c_o)
    while c_i < 2 :
        print ('Debe de haber mas de una ciudad')
        print ('Se incremento el numero de ciudades')
        c_i += 1
        while c_o < 2:
            print  ('Debe de haber mas de un color de ciudad')
            print ('Se incremento el numero de colores +1 para continuar')
            c_o += 1
        print 'El numero de ciudades ahora es %s' % c_i
        print 'El numero de colores ahora es %s' % c_o

        return c_i, c_o
    return c_i, c_o


# Second Rule Here: We obtain the max posible number of relationships that we can have and assert that it is over the relations number
def second_rule(n_r, c_i):
    c_i = int(c_i)
    r_max = 0
    for r in range(c_i):
        r_max = r_max + r
    while n_r > r_max:
        print ('\n El numero de ralaciones seleccionadas supera el numero de las posibles relacions.')
        print ('Se decrementara el numero de relaciones')
        n_r -= 1
        print 'El numero de relaciones ahora es %s' % n_r

    return n_r


# This function put the relations in python dictionaries, and also clean the data
def cleaning_data(t_r, c_i):
    relations_incomplete = str(t_r).split()
    relations_complete = []
    nodes = []
    nodes_2 = []

    for relation in relations_incomplete:
        relations_complete.append({})
        for node in relation:
            try:
                nodes.append(int(node))
                nodes_2.append(int(node))
                for dic in relations_complete:
                    if len(dic) < 2:
                        dic[node] = 'default'
                        return (dic)
            except: node

    return relations_complete, relations_incomplete, nodes, nodes_2


# Here we gonna put the color ceaning
def color_clearning(c_o):
    c_o = int(c_o)
    colors = ['Azul', 'Verde', 'Rojo', 'Negro', 'Morado', 'Amarillo', 'Blanco', 'Cafe', 'Gris', 'Naranja', 'Rosa', 'Dorado', 'Plateado']

    colors_t_ch = random.sample(colors, c_o)
    colors_t_ch_2 = []
    for color in colors_t_ch:
        colors_t_ch_2.append(color)

    return colors_t_ch, colors_t_ch_2

#Here we gonna put the main fuction, this function put a color within a python dictionary and asserts that the colors in one dictionary dont repeat itself.

def the_good_one(colors_t_ch, nodes,*args, **kwargs):
    colors_t_ch_2 = colors_t_ch
    colors_t_ch_3 = colors_t_ch

    def nodes_selection(nodes):
        mn = int(most_common(nodes))
        minor_n = int(less_common(nodes))
        return mn, minor_n

    def color_selection(colors_t_ch_2):
        mc = random.choice(colors_t_ch_2)
        minor_c = random.choice(colors_t_ch_2)
        while mc == minor_c:
            mc = random.choice(colors_t_ch_2)
            minor_c = random.choice(colors_t_ch_2)

        if len(colors_t_ch_2) > 2:
            second_color = random.choice(colors_t_ch_2)
            while second_color == mc:
                while second_color == minor_c:
                    second_color = random.choice(colors_t_ch_2)
        return mc, minor_c, second_color

    def color_assignation(relations_complete, mn, minor_n, mc, minor_c, second_color):
        for dic in relations_complete:
            if dic.has_key(mn):
                dic[mn] = mc
            elif dic.has_key(minor_n):
                dic[minor_n] = minor_c

            for  node, colors in dic.items():
                if dic.has_key(mn)and colors == 'default':
                    dic[node] = second_color
                elif dic.has_key(minor_n) and colors == 'default':
                    dic[node] = second_color
        return relations_complete

    def drop_nodes(nodes, mn, minor_n):
        for node in nodes:
            if node == mn or node == minor_n:
                nodes.remove(node)
                return nodes

    return relations_complete

def showing_results(relations_incomplete, relations_complete):
    nodes_3 = []
    nodes_4 = []

    for relation in relations_incomplete:
        for node in relation:
            nodes_3.append(node)

    for node in nodes_3:
        if node not in nodes_4:
            nodes_4.append(node)

    for dic in relations_complete:
        for node in dic:
            if node in nodes_4:
                results = (node, ':', dic[node])

                return results
