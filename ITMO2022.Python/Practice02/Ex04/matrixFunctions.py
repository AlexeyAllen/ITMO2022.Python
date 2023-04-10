import numpy as np
import pandas as pd
import scipy as scipy


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
