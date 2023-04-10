import numpy as np
import pandas as pd


def create_matrix_int(max_val, matrix_size_l, matrix_size_m):
    return np.random.randint(max_val, size=(matrix_size_l, matrix_size_m))


def create_matrix_float(max_val, matrix_size_l, matrix_size_m):
    return np.random.uniform(max_val, size=(matrix_size_l, matrix_size_m))


def save_to_csv(matrix, path_to_file):
    dataframe = pd.DataFrame(matrix)
    dataframe.to_csv(path_to_file, index=False, header=False)


def load_matrix(path_to_file):
    file_name = open(path_to_file)
    matrix = np.loadtxt(file_name, delimiter=",")
    file_name.close()
    return matrix

# def python_dgemm_algo(n, a, b, c):
#     for idx_i in range(n):
#         for idx_j in range(n):
#             c[idx_i + idx_j * n] = 0
#             for idx_k in range(n):
#                 c[idx_i + idx_j * n] += a[idx_i + idx_k * n] * b[idx_k + idx_j * n]
