import sympy
import numpy


def _validate_sq_matrix(matrix):
    if not isinstance(matrix, (list, numpy.ndarray)):
        raise ValueError("Input must be a list or numpy array.")
    if isinstance(matrix, list):
        matrix = numpy.array(matrix)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input must be a square matrix.")
    return matrix


def determinant(matrix, sym_res: bool | None = False):
    matrix = _validate_sq_matrix(matrix)
    if sym_res:
        sympy_matrix = sympy.Matrix(matrix)
        return sympy_matrix.det()
    else:
        numpy_matrix = numpy.array(matrix)
        return numpy.linalg.det(numpy_matrix)
