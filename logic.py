# -*- coding: utf-8 -*-

from functions import first_rule, second_rule, cleaning_data, color_clearning, the_good_one, showing_results


def process_the_info(c_i, c_o, n_r, t_r):

    first_rule(c_i, c_o) # Takes Cities number and Color number; return the same

    second_rule(n_r, c_i) # Takes Relations number and Cities number; Return Relations number

    cleaning_data(t_r, c_i) # Takes  The relation of every single relationship and also needs the Cities Number; Return relations_complete, relations_incomplete, nodes, nodes_2

    color_clearning(c_o) # Takes color number; Return colors_t_ch and colors_t_ch_2

    the_good_one(colors_t_ch, nodes, relations_complete) # Returns relations complete

    showing_results(relations_incomplete, relations_complete) # Returns the results

    return results
