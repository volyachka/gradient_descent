from constants import *


def distance_between_coordinates(dict_of_coordinates, dict_of_new_coordinates, number_of_variables):
    distance = 0
    for i in range(number_of_variables):
        distance += (dict_of_coordinates[x_list[i]] - dict_of_new_coordinates[x_list[i]]) ** 2
    return sqrt(distance)


def distance_between_min_and_current_coordinates(dict_of_minimum, dict_of_coordinates, number_of_variables):
    distance = 0
    for i in range(number_of_variables):
        distance += (dict_of_coordinates[x_list[i]] - dict_of_minimum[x_list[i]]) ** 2
    return sqrt(distance)


def toFixed(numObj, digits=4):
    return f"{numObj:.{digits}f}"


x = symbols(f"x_0:{N}")
x_dict = {f"x_{i}": x[i] for i in range(N)}
x_list = [x[i] for i in range(N)]
locals().update(x_dict)
print(x_list)
l_rate = symbols("l_rate")
l_rate_dict = {'l_rate': l_rate}
locals().update(l_rate_dict)


def round_dict_values(d, k):
    return {key: float(f"{value:.{k}f}") for key, value in d.items()}


def vector_measure(dict_of_coordinates, number_of_variables):
    distance = 0
    for i in range(number_of_variables):
        distance += (dict_of_coordinates[x_list[i]]) ** 2
    return distance


def get_vector(a, b):
    return np.arange(a, b + 1, 0.1)
