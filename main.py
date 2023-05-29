from testing import *
from constants import *

number_of_iterations = 300
modes = ["along_the_axes", "along_the_random_vector", 'perpendicular_to_the_previous_step']
print(dict_of_coordinates)
print('const_search')
search_with_selection_of_the_best_parameters_by_const_step()
for MODE in modes:
    print(MODE)
    print(dict_of_coordinates)
    search_with_selection_of_the_best_parameters_by_direction()
print('adaptive_step')
search_with_selection_of_the_best_parameters_adaptive_step()
print('step_division')
search_with_selection_of_the_best_parameters_step_division()
print('golden_search')
search_with_selection_of_the_best_parameters_by_golden_search()
