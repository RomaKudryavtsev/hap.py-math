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


def multiply(matrix_a, matrix_b, sym_res: bool | None = False):
    if not isinstance(matrix_a, (list, numpy.ndarray)) or not isinstance(
        matrix_b, (list, numpy.ndarray)
    ):
        raise ValueError("Both inputs must be lists or numpy arrays.")
    matrix_a = numpy.array(matrix_a)
    matrix_b = numpy.array(matrix_b)
    if matrix_a.shape[1] != matrix_b.shape[0]:
        raise ValueError(
            "Number of columns in the first matrix must equal number of rows in the second matrix."
        )
    if sym_res:
        sympy_matrix_a = sympy.Matrix(matrix_a)
        sympy_matrix_b = sympy.Matrix(matrix_b)
        return sympy_matrix_a * sympy_matrix_b
    else:
        numpy_matrix_a = numpy.array(matrix_a)
        numpy_matrix_b = numpy.array(matrix_b)
        return numpy.dot(numpy_matrix_a, numpy_matrix_b)
