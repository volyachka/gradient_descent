from methods import *


def search_with_selection_of_the_best_parameters_adaptive_step():
    a_array = [0.2, 0.4, 0.8]
    b_array = [1.5, 1.5, 1.5]
    steps = [1, 1e-2, 1e-4]
    func_value_min = 1000000000
    best_step = 1
    best_a = 1
    best_b = 1
    for STEP in steps:
        for a, b in zip(a_array, b_array):
            func_value = gradient_descent(update_coordinates_adaptive_step, dict_of_coordinates, dict_of_minimum,
                                          function_value, function, itetations_where_build_function_profile, STEP=STEP,
                                          build_graphic=False, all_iterations=True, print_table=False)
            print(STEP, func_value)
            if func_value < func_value_min:
                best_step = STEP
                best_a = a
                best_b = b
                func_value_min = func_value
    STEP = best_step
    a = best_a
    b = best_b
    if number_of_variables == 2:
        func_value = gradient_descent(update_coordinates_adaptive_step, dict_of_coordinates, dict_of_minimum,
                                      function_value, function, itetations_where_build_function_profile, STEP=STEP,
                                      build_graphic=True, all_iterations=True, print_table=True)
    else:
        func_value = gradient_descent(update_coordinates_adaptive_step, dict_of_coordinates, dict_of_minimum,
                                      function_value, function, itetations_where_build_function_profile, STEP=STEP,
                                      build_graphic=False, all_iterations=True, print_table=True)
    return func_value


def search_with_selection_of_the_best_parameters_step_division():
    # steps = [1, 1e-2, 1e-4]
    global EPSILON
    steps = [1, 1e-2, 1e-4]
    epsilons = [0.2, 0.4, 0.8]
    func_value_min = 1000000000
    best_step = 1
    best_epsilon = 1
    for STEP in steps:
        for EPSILON in epsilons:
            func_value = gradient_descent(update_coordinates_step_division, dict_of_coordinates, dict_of_minimum,
                                          function_value, function, itetations_where_build_function_profile, STEP=STEP,
                                          build_graphic=False, all_iterations=True, print_table=False)
        if func_value < func_value_min:
            best_step = STEP
            func_value_min = func_value
            best_epsilon = EPSILON
    STEP = best_step
    EPSILON = best_epsilon
    if number_of_variables == 2:
        func_value = gradient_descent(update_coordinates_step_division, dict_of_coordinates, dict_of_minimum,
                                      function_value, function, itetations_where_build_function_profile, STEP=STEP,
                                      build_graphic=True, all_iterations=True, print_table=True)
    else:
        func_value = gradient_descent(update_coordinates_step_division, dict_of_coordinates, dict_of_minimum,
                                      function_value, function, itetations_where_build_function_profile, STEP=STEP,
                                      build_graphic=False, all_iterations=True, print_table=True)
    return func_value


def round_dict_values(d, k):
    return {key: float(f"{value:.{k}f}") for key, value in d.items()}


def search_with_selection_of_the_best_parameters_by_direction():
    # steps = [1, 1e-2, 1e-4, 1e-6, 1e-8]
    steps = [1]
    func_value_min = 1000000000
    best_step = 1
    for STEP in steps:
        func_value = gradient_descent(update_coordinates_by_direction, dict_of_coordinates, dict_of_minimum,
                                      function_value, function, itetations_where_build_function_profile, STEP=STEP,
                                      build_graphic=False, all_iterations=True, print_table=False)
        print(STEP, func_value)
        if func_value < func_value_min:
            best_step = STEP
            func_value_min = func_value
    STEP = best_step
    if number_of_variables == 2:
        func_value = gradient_descent(update_coordinates_by_direction, dict_of_coordinates, dict_of_minimum,
                                      function_value, function, itetations_where_build_function_profile, STEP=STEP,
                                      build_graphic=True, all_iterations=True, print_table=True)
    else:
        func_value = gradient_descent(update_coordinates_by_direction, dict_of_coordinates, dict_of_minimum,
                                      function_value, function, itetations_where_build_function_profile, STEP=STEP,
                                      build_graphic=False, all_iterations=True, print_table=True)


def search_with_selection_of_the_best_parameters_by_const_step():
    # steps = [1, 1e-2, 1e-4]
    steps = [1, 1e-2, 1e-4]
    func_value_min = 1000000000
    best_step = 1
    for STEP in steps:
        func_value = gradient_descent(update_coordinates_const_step, dict_of_coordinates, dict_of_minimum,
                                      function_value, function, itetations_where_build_function_profile, STEP=STEP,
                                      build_graphic=False, all_iterations=True, print_table=False)
        print(STEP, func_value)
        print(func_value, func_value_min)
        if func_value < func_value_min:
            best_step = STEP
            func_value_min = func_value
    STEP = best_step
    if number_of_variables == 2:
        func_value = gradient_descent(update_coordinates_const_step, dict_of_coordinates, dict_of_minimum,
                                      function_value, function, itetations_where_build_function_profile, STEP=STEP,
                                      build_graphic=True, all_iterations=True, print_table=True)
    else:
        func_value = gradient_descent(update_coordinates_const_step, dict_of_coordinates, dict_of_minimum,
                                      function_value, function, itetations_where_build_function_profile, STEP=STEP,
                                      build_graphic=False, all_iterations=True, print_table=True)
    return func_value


def search_with_selection_of_the_best_parameters_by_golden_search():
    # steps = [1e-2]
    steps = [1e-8]
    func_value_min = 1000000000
    best_step = 1
    for STEP in steps:
        func_value = gradient_descent(update_coordinates_fastest_descent_golden_search, dict_of_coordinates,
                                      dict_of_minimum, function_value, function,
                                      itetations_where_build_function_profile, STEP=STEP, build_graphic=False,
                                      all_iterations=True, print_table=False)
        print(STEP, func_value)
        if func_value < func_value_min:
            best_step = STEP
            func_value_min = func_value
    STEP = best_step
    if number_of_variables == 2:
        func_value = gradient_descent(update_coordinates_fastest_descent_golden_search, dict_of_coordinates,
                                      dict_of_minimum, function_value, function,
                                      itetations_where_build_function_profile, STEP=STEP, build_graphic=True,
                                      all_iterations=True, print_table=True)
    else:
        func_value = gradient_descent(update_coordinates_fastest_descent_golden_search, dict_of_coordinates,
                                      dict_of_minimum, function_value, function,
                                      itetations_where_build_function_profile, STEP=STEP, build_graphic=False,
                                      all_iterations=True, print_table=True)
    return func_value
