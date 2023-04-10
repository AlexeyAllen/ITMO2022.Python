from Practice02.Ex04.matrixFunctions import create_matrix_int, save_to_csv, load_matrix, create_matrix_float
from time import time
import numpy as np
import scipy as scipy


file_path_matrix_A_int = "dataFolder/matrix_A_int.csv"
file_path_matrix_B_int = "dataFolder/matrix_B_int.csv"
file_path_matrix_C_int = "dataFolder/matrix_C_int.csv"

file_path_matrix_A_float = "dataFolder/matrix_A_float.csv"
file_path_matrix_B_float = "dataFolder/matrix_B_float.csv"
file_path_matrix_C_float = "dataFolder/matrix_C_float.csv"

file_path_matrix_C_dgemm_int = "dataFolder/matrix_C_dgemm_int.csv"
file_path_matrix_C_dgemm_float = "dataFolder/matrix_C_dgemm_float.csv"


max_val = int(input("Введите максимальное значение диапазона значений матрицы => "))
matrix_size_l = int(input("Введите размер матрицы l => "))
matrix_size_m = int(input("Введите размер матрицы m => "))

matrix_A_int = create_matrix_float(max_val, matrix_size_l, matrix_size_m)
matrix_B_int = create_matrix_float(max_val, matrix_size_l, matrix_size_m)
matrix_C_int = create_matrix_float(max_val, matrix_size_l, matrix_size_m)

matrix_A_float = create_matrix_float(max_val, matrix_size_l, matrix_size_m)
matrix_B_float = create_matrix_float(max_val, matrix_size_l, matrix_size_m)
matrix_C_float = create_matrix_float(max_val, matrix_size_l, matrix_size_m)
matrix_C_dgemm = create_matrix_float(max_val, matrix_size_l, matrix_size_m)

save_to_csv(matrix_A_int, file_path_matrix_A_int)
save_to_csv(matrix_B_int, file_path_matrix_B_int)
save_to_csv(matrix_A_float, file_path_matrix_A_float)
save_to_csv(matrix_B_float, file_path_matrix_B_float)

start_time = time()
result = np.dot(load_matrix(file_path_matrix_A_int), load_matrix(file_path_matrix_B_int))
finish_time = time() - start_time
print('Время перемножения матриц c int значениями: {:.2f} сек.'.format(finish_time))
save_to_csv(result, file_path_matrix_C_int)

start_time = time()
result = np.dot(load_matrix(file_path_matrix_A_float), load_matrix(file_path_matrix_B_float))
finish_time = time() - start_time
print('Время перемножения матриц c float значениями: {:.2f} сек.'.format(finish_time))
save_to_csv(result, file_path_matrix_C_float)

alpha = 5
start_time = time()
result = scipy.linalg.blas.dgemm(alpha, load_matrix(file_path_matrix_A_float), load_matrix(file_path_matrix_B_float))
finish_time = time() - start_time
print('Время перемножения матриц dgemm: {:.2f} сек.'.format(finish_time))
save_to_csv(result, file_path_matrix_C_dgemm_float)

start_time = time()
result = scipy.linalg.blas.sgemm(alpha, load_matrix(file_path_matrix_A_int), load_matrix(file_path_matrix_B_int))
finish_time = time() - start_time
print('Время перемножения матриц dgemm: {:.2f} сек.'.format(finish_time))
save_to_csv(result, file_path_matrix_C_dgemm_int)