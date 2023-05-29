from utilities import *


def plot_3d_function(function, a, b):
    f_xy = sp.lambdify((x_list[0], x_list[1]), sp.sympify(function))
    domain_x = get_vector(range_of_start_point, range_of_end_point)
    domain_y = get_vector(range_of_start_point, range_of_end_point)
    domain_x, domain_y = np.meshgrid(domain_x, domain_y)
    image = f_xy(domain_x, domain_y)
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection='3d')
    ax.plot_surface(domain_x, domain_y, image, rstride=1, cstride=1, cmap='viridis')
    plt.show()


def build_graph(function, coordinate_x0_to_build_graphic, coordinate_x1_to_build_graphic,
                coordinate_f_to_build_graphic):
    f_xy = sp.lambdify((x_list[0], x_list[1]), sp.sympify(function))
    print(min(coordinate_x0_to_build_graphic), max(coordinate_x0_to_build_graphic))
    domain_x = get_vector(int(min(coordinate_x0_to_build_graphic)) - 1, int(max(coordinate_x0_to_build_graphic)) + 1)
    domain_y = get_vector(int(min(coordinate_x1_to_build_graphic)) - 1, int(max(coordinate_x1_to_build_graphic)) + 1)
    domain_x, domain_y = np.meshgrid(domain_x, domain_y)
    image = f_xy(domain_x, domain_y)
    fig = plt.figure(figsize=(7, 7))
    ax = plt.axes(projection='3d')
    ax.plot_surface(domain_x, domain_y, image, alpha=0.5, cmap='Blues')
    ax.set_xlabel('x0', fontsize=12)
    ax.set_ylabel('x1', fontsize=12)
    ax.set_zlabel('f(x0, x1)', fontsize=12)
    ax.plot(coordinate_x0_to_build_graphic, coordinate_x1_to_build_graphic, coordinate_f_to_build_graphic, '.-',
            c='red')
    plt.show()


def function_profile(function, list_of_coordinares_build_function_profile, list_of_gradients_build_function_profile,
                     range_of_values, itetations_where_build_function_profile):
    for dict_of_coordinates, gradient, iteration in zip(list_of_coordinares_build_function_profile,
                                                        list_of_gradients_build_function_profile,
                                                        itetations_where_build_function_profile):
        gradient_norm = sqrt(sum(value ** 2 for value in gradient.values()))
        gradient = {key: value / gradient_norm for key, value in gradient.items()}
        t = np.linspace(-range_of_values, range_of_values, 100)
        new_coordinates_0 = dict_of_coordinates[x_list[0]] - t * gradient[x_list[0]]
        new_coordinates_1 = dict_of_coordinates[x_list[1]] - t * gradient[x_list[1]]
        coord = dict()
        func_value = list()
        f = function(2)
        for first_coord, second_coord in zip(new_coordinates_0, new_coordinates_1):
            coord[x_list[0]] = first_coord
            coord[x_list[1]] = second_coord
            func_value.append(f.subs(coord))
        print(func_value)
        fig, ax = plt.subplots()
        ax.set_xlabel('x0', fontsize=10)
        ax.set_ylabel('x1', fontsize=10)
        ax.set_title('Номер итерации, при которой берется профиль: ' + str(iteration))
        ax.plot(t, func_value, '.-', c='red')
        plt.show()
