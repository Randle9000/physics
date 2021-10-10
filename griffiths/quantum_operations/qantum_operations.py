from sympy import *


def get_probability_of_density(func):
    func_conjugate = conjugate(func)
    function_probability_of_density = func_conjugate*func
    return function_probability_of_density


def put_operator_on_function(operator, function):
    function_conjugate = conjugate(function)
    return function_conjugate * operator * function
