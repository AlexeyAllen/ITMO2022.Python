# from Practice02.Ex04.functions import load_matrix, dgemm_calcs, save_matrix_to_csv, get_statistics, threaded_calc
from time import time
# from Practice02.Ex04.functions import graphics_create

import sys
sys.path.append(r'..\Ex04')
import functions
from functions import load_matrix, dgemm_calcs, save_matrix_to_csv, get_statistics, threaded_calc, graphics_create

file_path_matrix_a_int = "dataFolder/matrix_a_int.csv"
file_path_matrix_b_int = "dataFolder/matrix_b_int.csv"
file_path_matrix_c_int = "dataFolder/matrix_c_int.csv"
file_path_matrix_d_int = "dataFolder/matrix_d_int.csv"

file_path_matrix_a_float = "dataFolder/matrix_a_float.csv"
file_path_matrix_b_float = "dataFolder/matrix_b_float.csv"
file_path_matrix_c_float = "dataFolder/matrix_c_float.csv"
file_path_matrix_d_float = "dataFolder/matrix_d_float.csv"

statistics_path_int = "dataFolder/resulted_statistics_int.csv"
statistics_path_float = "dataFolder/resulted_statistics_float.csv"

matrix_a_int_loaded = load_matrix(file_path_matrix_a_int)
matrix_b_int_loaded = load_matrix(file_path_matrix_b_int)
matrix_c_int_loaded = load_matrix(file_path_matrix_c_int)

matrix_a_float_loaded = load_matrix(file_path_matrix_a_float)
matrix_b_float_loaded = load_matrix(file_path_matrix_b_float)
matrix_c_float_loaded = load_matrix(file_path_matrix_c_float)

alpha = float(input("Введите коэффициент alpha => "))
betta = float(input("Введите коэффициент betta => "))

# Matrices multiplication with a single thread

time_lst = [time() * 1000]
matrix_d_int = dgemm_calcs(matrix_a_int_loaded, matrix_b_int_loaded, matrix_c_int_loaded, alpha, betta)
time_lst.append(time() * 1000)
time_median_value_python = get_statistics(time_lst, statistics_path_int)
save_matrix_to_csv(matrix_d_int, file_path_matrix_d_int)
graphics_create(time_median_value_python)

time_lst = [time() * 1000]
matrix_d_float = dgemm_calcs(matrix_a_float_loaded, matrix_b_float_loaded, matrix_c_float_loaded, alpha, betta)
time_lst.append(time() * 1000)
time_median_value_python = get_statistics(time_lst, statistics_path_float)
save_matrix_to_csv(matrix_d_float, file_path_matrix_d_float)
graphics_create(time_median_value_python)

# Matrices multiplication with a multithreading

time_lst = [time() * 1000]
matrix_d_int = threaded_calc(matrix_a_float_loaded, matrix_b_float_loaded, matrix_c_float_loaded, alpha, betta)
time_lst.append(time() * 1000)
time_median_value_python = get_statistics(time_lst, statistics_path_int)
save_matrix_to_csv(matrix_d_int, file_path_matrix_d_int)
graphics_create(time_median_value_python)

time_lst = [time() * 1000]
matrix_d_float = threaded_calc(matrix_a_float_loaded, matrix_b_float_loaded, matrix_c_float_loaded, alpha, betta)
time_lst.append(time() * 1000)
time_median_value_python = get_statistics(time_lst, statistics_path_float)
save_matrix_to_csv(matrix_d_float, file_path_matrix_d_float)
graphics_create(time_median_value_python)
