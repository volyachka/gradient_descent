from utilities import *
from constants import *
import numpy as np

phi = (1 + sqrt(5)) / 2
resphi = 2 - phi


def gradient_descent(update_coordinates, dict_of_initial_coordinates, dict_of_minimum, function_value, function,
                     itetations_where_build_function_profile, STEP=1, a=1, b=1, EPSILON=1, build_graphic=False,
                     debug=False, all_iterations=True, print_table=True):
    global iteration, difference_between_functions, value_of_function, step, dict_of_coordinates, dict_of_value_derivation
    coordinate_x0_to_build_graphic = list()
    coordinate_x1_to_build_graphic = list()
    coordinate_f_to_build_graphic = list()
    list_of_coordinares_build_function_profile = list()
    list_of_gradients_build_function_profile = list()
    # print(dict_of_initial_coordinates)
    for number_of_variables in list_of_variables:
        f = function(number_of_variables)
        dict_of_coordinates = dict_of_initial_coordinates
        # write random start coordinates
        # our function has only one global minimum, when all coordinates == 0. So, let's fill array_of_minimum
        step = STEP
        for iteration in range(number_of_iterations):
            coordinate_x0_to_build_graphic.append(dict_of_coordinates[x_list[0]])
            coordinate_x1_to_build_graphic.append(dict_of_coordinates[x_list[1]])
            coordinate_f_to_build_graphic.append(f.subs(dict_of_coordinates))
            dict_of_new_coordinates, new_step = update_coordinates(f, number_of_variables, dict_of_coordinates, step)
            distance = distance_between_min_and_current_coordinates(dict_of_minimum, dict_of_coordinates,
                                                                    number_of_variables)
            distance_between_steps = f.subs(dict_of_new_coordinates) - f.subs(dict_of_coordinates)
            if debug == True:
                print('dict_of_new_coordinates ', dict_of_new_coordinates)
            if iteration in itetations_where_build_function_profile:
                dict_of_value_derivation = dict()
                for i in range(number_of_variables):
                    dict_of_value_derivation[x_list[i]] = (f.diff(x_list[i]).subs(dict_of_coordinates))
                list_of_coordinares_build_function_profile.append(dict_of_new_coordinates)
                list_of_gradients_build_function_profile.append(dict_of_value_derivation)
            if all_iterations == False and abs(distance_between_steps) < EPS:
                accuracy = distance_between_min_and_current_coordinates(dict_of_minimum, dict_of_new_coordinates,
                                                                        number_of_variables)
                break
            else:
                dict_of_coordinates = dict_of_new_coordinates
                step = new_step

        if distance > 1e8:
            print('inf')
            dict_of_value_derivation = dict()
            for i in range(number_of_variables):
                dict_of_value_derivation[x_list[i]] = (f.diff(x_list[i]).subs(dict_of_coordinates))
            return 10000000
        value_of_function = f.subs(dict_of_coordinates)
        difference_between_functions = f.subs(dict_of_coordinates) - f.subs(dict_of_minimum)
        dict_of_value_derivation = dict()
        for i in range(number_of_variables):
            dict_of_value_derivation[x_list[i]] = (f.diff(x_list[i]).subs(dict_of_coordinates))
    if print_table == True:
        table_1 = [['distance_between_min_and_current_coordinates', 'number of iteration', 'step',
                    'distance_between_min_and_current_function_value', 'value_of_function'],
                   [toFixed(distance), toFixed(iteration), toFixed(step), toFixed(difference_between_functions),
                    toFixed(value_of_function)]]
        print(tabulate(table_1, headers="firstrow", tablefmt="psql"))
        table_2 = [['coordinates', 'value of derivations'], [dict_of_coordinates, dict_of_value_derivation]]
        print(tabulate(table_2, headers="firstrow", tablefmt="psql"))
        print(
            f'dict of coordinates = {round_dict_values(dict_of_coordinates, 3)}, distance_between_min_and_current_function_value = {toFixed(difference_between_functions)}, value_of_function = {toFixed(value_of_function)}, value_derivation = {round_dict_values(dict_of_value_derivation, 3)}')
    return value_of_function


def goldenSectionSearch(f, a, c, b, absolutePrecision):
    if abs(a - b) < absolutePrecision:
        return (a + b) / 2
    # Create a new possible center, in the area between c and b, pushed against c
    d = c + resphi * (b - c)
    if f.subs({l_rate: d}) < f.subs({l_rate: c}):
        return goldenSectionSearch(f, c, d, b, absolutePrecision)
    else:
        return goldenSectionSearch(f, d, c, a, absolutePrecision)


def ternarySearchMin(f, left, right, eps):
    while right - left > eps:
        a = (left * 2 + right) / 3
        b = (left + right * 2) / 3
        if f.subs({l_rate: a}) < f.subs({l_rate: b}):
            right = b
        else:
            left = a
    return (left + right) / 2


def update_coordinates_const_step(f, number_of_variables, dict_of_coordinates, step):
    new_dict_of_coordinates = dict()
    for i in range(number_of_variables):
        derivation = f.diff(x_list[i])
        value_of_derivation = derivation.subs(dict_of_coordinates)
        # print(f.diff(x_list[i]), value_of_derivation * step)
        # print(value_of_derivation)
        new_dict_of_coordinates[x_list[i]] = dict_of_coordinates[x_list[i]] - value_of_derivation * step
    return new_dict_of_coordinates, step


def update_coordinates_step_division(f, number_of_variables, dict_of_coordinates, step):
    dict_of_new_coordinates = dict()
    dict_of_value_derivation = dict()
    for i in range(number_of_variables):
        dict_of_value_derivation[x_list[i]] = f.diff(x_list[i]).subs(dict_of_coordinates)
        dict_of_new_coordinates[x_list[i]] = dict_of_coordinates[x_list[i]] - dict_of_value_derivation[x_list[i]] * step
    # print(dict_of_value_derivation)
    left_part = f.subs(dict_of_new_coordinates)
    right_part = f.subs(dict_of_coordinates) - EPSILON * step * vector_measure(dict_of_value_derivation,
                                                                               number_of_variables)
    # print(left_part, right_part)
    if left_part <= right_part:
        return dict_of_new_coordinates, step
    else:
        return dict_of_new_coordinates, step * EPSILON


b = 0.9
a = 1.5


def update_coordinates_adaptive_step(f, number_of_variables, dict_of_coordinates, step):
    # print(dict_of_coordinates, f.subs(dict_of_coordinates))
    dict_of_new_coordinates = dict()
    dict_of_derivation = dict()
    dict_of_coordinates_to_search_new_step = dict()
    # here l_rate is special variable to define optimal step, so it is depricated to use it as function variable
    for i in range(number_of_variables):
        dict_of_derivation[x_list[i]] = f.diff(x_list[i])
        value_of_derivation = dict_of_derivation[x_list[i]].subs(dict_of_coordinates)
        # print(value_of_derivation)
        dict_of_new_coordinates[x_list[i]] = dict_of_coordinates[x_list[i]] - value_of_derivation * step
    function_before_step = f.subs(dict_of_coordinates)
    function_after_step = f.subs(dict_of_new_coordinates)
    # print(dict_of_new_coordinates)
    if function_after_step <= function_before_step:
        return dict_of_new_coordinates, a * step
    else:
        return dict_of_new_coordinates, b * step


def update_coordinates_fastest_descent_golden_search(f, number_of_variables, dict_of_coordinates, step):
    dict_of_new_coordinates = dict()
    dict_of_derivation = dict()
    dict_of_coordinates_to_search_new_step = dict()
    # here l_rate is special variable to define optimal step, so it is depricated to use it as function variable
    for i in range(number_of_variables):
        dict_of_derivation[x_list[i]] = f.diff(x_list[i])
        value_of_derivation = dict_of_derivation[x_list[i]].subs(dict_of_coordinates)
        dict_of_coordinates_to_search_new_step[x_list[i]] = dict_of_coordinates[
                                                                x_list[i]] - value_of_derivation * l_rate
    function_to_optimize = f.subs(dict_of_coordinates_to_search_new_step)
    step = goldenSectionSearch(function_to_optimize, -1, (-1 + resphi * 2), 1, 1e-8)
    for i in range(number_of_variables):
        dict_of_derivation[x_list[i]] = f.diff(x_list[i])
        value_of_derivation = dict_of_derivation[x_list[i]].subs(dict_of_coordinates)
        dict_of_new_coordinates[x_list[i]] = dict_of_coordinates[x_list[i]] - value_of_derivation * step
    return dict_of_new_coordinates, step


def update_coordinates_fastest_descent_ternarySearchMin(f, number_of_variables, dict_of_coordinates, step):
    dict_of_new_coordinates = dict()
    dict_of_derivation = dict()
    dict_of_coordinates_to_search_new_step = dict()
    # here l_rate is special variable to define optimal step, so it is depricated to use it as function variable
    for i in range(number_of_variables):
        dict_of_derivation[x_list[i]] = f.diff(x_list[i])
        value_of_derivation = dict_of_derivation[x_list[i]].subs(dict_of_coordinates)
        dict_of_new_coordinates[x_list[i]] = dict_of_coordinates[x_list[i]] - value_of_derivation * step
        dict_of_coordinates_to_search_new_step[x_list[i]] = dict_of_coordinates[
                                                                x_list[i]] - value_of_derivation * l_rate

    function_to_optimize = f.subs(dict_of_coordinates_to_search_new_step)
    step = ternarySearchMin(function_to_optimize, -1, 1, 1e-8)

    for i in range(number_of_variables):
        value_of_derivation = dict_of_derivation[x_list[i]].subs(dict_of_coordinates)
        dict_of_new_coordinates[x_list[i]] = dict_of_coordinates[x_list[i]] - value_of_derivation * step

    return dict_of_new_coordinates, step


def update_coordinates_by_direction(f, number_of_variables, dict_of_coordinates, step):
    f = function(number_of_variables)
    dict_of_new_coordinates, new_step = update_coordinates_adaptive_step(f, number_of_variables, dict_of_coordinates,
                                                                         step)
    if distance_between_coordinates(dict_of_coordinates, dict_of_new_coordinates, number_of_variables) > 1e-3:
        return dict_of_new_coordinates, new_step
    else:
        # можно вдоль координатных осей (самый понятный способ)
        new_func_value = f.subs(dict_of_coordinates)
        # можно вдоль направления, перпендикулярного предыдущему шагу.
        if MODE == "perpendicular_to_the_previous_step":
            # считаем градиент на предыдущем шаге
            derivation = dict()
            for i in range(number_of_variables):
                derivation[x_list[i]] = (f.diff(x_list[i]).subs(dict_of_coordinates))
            length = sqrt(sum(value ** 2 for value in derivation.values()))
            derivation = {key: value / length for key, value in derivation.items()}
            j = 1
            v = list()
            counter = 0
            for i in range(number_of_variables):
                if abs(derivation[x_list[i]]) >= 1e-3:
                    v.append(j / derivation[x_list[i]])
                    j *= -1
                    counter += 1
                else:
                    v.append(0)
            if counter % 2 != 0:
                v[0] = 0
            if counter == 0:
                return
            # answer = 0
            # for i in range(number_of_variables):
            #   answer += v[i] * derivation[x_list[i]]
            # print(answer)
            point = dict_of_coordinates.copy()  # стартовая точка
            flag = 0
            while (True):
                for i in range(number_of_variables):
                    point[x_list[i]] = point[x_list[i]] + v[i]
                    if (point[x_list[i]] >= range_of_end_point or point[x_list[i]] <= range_of_start_point):
                        flag = 1
                        break
                if flag == 1:
                    break
                func_value_search_by_random_vector = f.subs(point)
                if func_value_search_by_random_vector < new_func_value:
                    new_func_value = func_value_search_by_random_vector
                    dict_of_new_coordinates = point.copy()
            point = dict_of_coordinates.copy()  # стартовая точка
            # теперь идем в отрицательную сторону с шагом 0.1, делая не больше 1000 итераций
            flag = 0
            while (True):
                for i in range(number_of_variables):
                    point[x_list[i]] -= v[i]
                    if point[x_list[i]] >= range_of_end_point or point[x_list[i]] <= range_of_start_point:
                        flag = 1
                        break
                if flag == 1:
                    break
                # print(point)
                func_value_search_by_random_vector = f.subs(point)
                if func_value_search_by_random_vector < new_func_value:
                    new_func_value = func_value_search_by_random_vector
                    dict_of_new_coordinates = point.copy()
            return dict_of_new_coordinates, step

        if MODE == "along_the_axes":
            for i in range(number_of_variables):
                dict_of_coordinates_search_by_direction = dict_of_coordinates.copy()
                new_coord = np.linspace(range_of_start_point, range_of_end_point, 25)
                for coord in new_coord:
                    dict_of_coordinates_search_by_direction[x_list[i]] = coord
                    func_value_search_by_direction = f.subs(dict_of_coordinates_search_by_direction)
                    # print(dict_of_coordinates_search_by_direction, func_value_search_by_direction, new_func_value)
                    if func_value_search_by_direction < new_func_value:
                        # print(func_value_search_by_direction, new_func_value)
                        new_func_value = func_value_search_by_direction
                        dict_of_new_coordinates = dict_of_coordinates_search_by_direction.copy()
            return dict_of_new_coordinates, step

        if MODE == "along_the_random_vector":
            # можно взять рандоомный вектор, который задаст направление (вообще непонятно, как генерировать этот вектор)
            v = np.random.rand(number_of_variables)
            length = np.linalg.norm(v)
            v = v / length
            point = dict_of_coordinates.copy()  # стартовая точка
            # сначала идем в положительную сторону с шагом 0.1, делая не больше 1000 итераций
            flag = 0
            while (True):
                for i in range(number_of_variables):
                    point[x_list[i]] = point[x_list[i]] + v[i]
                    if (point[x_list[i]] >= range_of_end_point or point[x_list[i]] <= range_of_start_point):
                        flag = 1
                        break
                if flag == 1:
                    break
                # print(point)
                func_value_search_by_random_vector = f.subs(point)
                if func_value_search_by_random_vector < new_func_value:
                    new_func_value = func_value_search_by_random_vector
                    dict_of_new_coordinates = point.copy()
            point = dict_of_coordinates.copy()  # стартовая точка
            # теперь идем в отрицательную сторону с шагом 0.1, делая не больше 1000 итераций
            flag = 0
            while (True):
                for i in range(number_of_variables):
                    point[x_list[i]] -= v[i]
                    if (point[x_list[i]] >= range_of_end_point or point[x_list[i]] <= range_of_start_point):
                        flag = 1
                        break
                if flag == 1:
                    break
                # print(point)
                func_value_search_by_random_vector = f.subs(point)
                if func_value_search_by_random_vector < new_func_value:
                    new_func_value = func_value_search_by_random_vector
                    dict_of_new_coordinates = point.copy()
            return dict_of_new_coordinates, step
