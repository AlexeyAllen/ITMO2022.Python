# from Practice02.Ex04.functions import create_matrix_int, save_matrix_to_csv, load_matrix, dgemm_calcs, \
#     create_matrix_float

import sys
sys.path.append(r'..\Ex04')
import functions
from functions import create_matrix_int, save_matrix_to_csv, load_matrix, dgemm_calcs,create_matrix_float

file_path_matrix_a_int = "dataFolder/matrix_a_int.csv"
file_path_matrix_b_int = "dataFolder/matrix_b_int.csv"
file_path_matrix_c_int = "dataFolder/matrix_c_int.csv"
file_path_matrix_d_int = "dataFolder/matrix_d_int.csv"

file_path_matrix_a_float = "dataFolder/matrix_a_float.csv"
file_path_matrix_b_float = "dataFolder/matrix_b_float.csv"
file_path_matrix_c_float = "dataFolder/matrix_c_float.csv"
file_path_matrix_d_float = "dataFolder/matrix_d_float.csv"

max_val = int(input("Введите максимальное значение диапазона значений матрицы => "))
matrix_size_l = int(input("Введите размер квадратной матрицы => "))
# matrix_size_m = int(input("Введите размер матрицы m => "))

matrix_a_int = create_matrix_int(max_val, matrix_size_l, matrix_size_l)
matrix_b_int = create_matrix_int(max_val, matrix_size_l, matrix_size_l)
matrix_c_int = create_matrix_int(max_val, matrix_size_l, matrix_size_l)

matrix_a_float = create_matrix_float(max_val, matrix_size_l, matrix_size_l)
matrix_b_float = create_matrix_float(max_val, matrix_size_l, matrix_size_l)
matrix_c_float = create_matrix_float(max_val, matrix_size_l, matrix_size_l)

save_matrix_to_csv(matrix_a_int, file_path_matrix_a_int)
save_matrix_to_csv(matrix_b_int, file_path_matrix_b_int)
save_matrix_to_csv(matrix_c_int, file_path_matrix_c_int)

save_matrix_to_csv(matrix_a_float, file_path_matrix_a_float)
save_matrix_to_csv(matrix_b_float, file_path_matrix_b_float)
save_matrix_to_csv(matrix_c_float, file_path_matrix_c_float)
