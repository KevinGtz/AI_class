

def process_the_info(c_i, c_o, r_n, t_r):
    cities = c_i
    colors = c_o
    relations_number = r_n
    relations = str(t_r).split()
    relations_cleaned = []

    for relation in relations:
        for element in relation:
            if element not in ['-', ',']:
                relations_cleaned.append(int(element))

    return relations_cleaned
