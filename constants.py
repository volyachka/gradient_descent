from sympy import symbols, diff
import sympy as sp
from sympy import sin, cos, exp, sqrt
import random
from sympy import exp, I

# min_number of variables in function
n = 1
# max_number of variables in function
N = 100
# diffrence between two steps when program will stopf
EPS = 1e-8
b = 0.2
a = 1.5
x = symbols(f"x_0:{N}")
x_dict = {f"x_{i}": x[i] for i in range(N)}
x_list = [x[i] for i in range(N)]
locals().update(x_dict)
print(x_list)
l_rate = symbols("l_rate")
l_rate_dict = {'l_rate': l_rate}
locals().update(l_rate_dict)

itetations_where_build_function_profile = [300, 600, 900]


def function(number_of_variables):
  sum_1 = 0
  sum_2 = 0
  for i in range(1, 6):
    sum_1 += i * cos((i + 1)*x_list[0]+1)
    sum_2 += i * cos((i + 1)*x_list[1]+1)
  return -sum_1*sum_2

STEP = 1
EPSILON = 1
MODE = "along_the_axes"
function_value = function(2)

print(function_value)
f_xy = sp.lambdify((x_list[0], x_list[1]), sp.sympify(function_value))

number_of_iterations = 100
range_of_start_point = -5
range_of_end_point = 5
list_of_variables = [2]
number_of_variables = 2
dict_of_coordinates = dict()
dict_of_minimum = dict()
for i in range(list_of_variables[-1]):
    dict_of_coordinates[x_list[i]] = random.uniform(range_of_start_point, range_of_end_point)
    dict_of_minimum[x_list[i]] = 0
print(dict_of_coordinates)
