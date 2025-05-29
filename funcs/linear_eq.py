import numpy as np
from sympy import Matrix, symbols


def solve_linear_system(equations, sym_res=False):
    coefficients = [row[:-1] for row in equations]
    constants = [row[-1] for row in equations]
    if sym_res:
        variables_num = len(coefficients[0])
        variables = symbols(f"x1:{variables_num+1}")
        coeff_matrix = Matrix(coefficients)
        const_matrix = Matrix(constants)
        solution = coeff_matrix.LUsolve(const_matrix)
        return {str(variables[i]): solution[i] for i in range(len(variables))}
    else:
        coeff_matrix = np.array(coefficients)
        const_matrix = np.array(constants)
        solution = np.linalg.solve(coeff_matrix, const_matrix)
        return solution.tolist()
