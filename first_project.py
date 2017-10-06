# -*- coding: utf-8 -*-

# This program is for my school for the class of AI

'''
Rules
1. CI AND CO > 1
2. R_MAX > R_N
3. NA* < CO
'''
# We take all the data and assing them to a varibles
# cities_number = int(input('Cuantas ciudades se ubican en el mapa? \n'))
# color_number = int(input('Cuantos colores se van a utilizar? \n'))
#
# # We assert tha this varibles aprove the first rule
# while cities_number < 2 or color_number < 2:
#     print('Deben existir por lo menos dos ciudades y dos colores \n')
#     cities_number = int(input('Cuantas ciudades se ubican en el mapa? \n'))
#     color_number = int(input('Cuantos colores se van a utilizar? \n'))

relationships_number = int(input('Cuantas relaciones existen entre las ciudades? \n'))

# while True:
#     r_max = 0
#     for r in range(cities_number):
#         r_max = r_max + r
#     if relationships_number > r_max:
#         print('\nEl numero de relaciones seleccionadas supera el numero de las posibles relaciones, es decir coloca un numero menor de relaciones para continuar o incrementa el numero de ciudades. \n')
#         cities_number = int(input('Cuantas ciudades se ubican en el mapa? \n'))
#         relationships_number = int(input('Cuantas relaciones existen entre las ciudades? \n'))
#     else:
#         print(r_max)
#         break

relations = [{}]

for relation in range(relationships_number):
    the_relation = input('Dame los nodos que se relacionan, separados por una coma: \n')
    relations.append(the_relation)

print (relations)

#print(cities_number, type(color_number))
