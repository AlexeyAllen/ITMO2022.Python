import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt
from threading import Thread

# MAX_THREAD_1 = 1
# MAX_THREAD_2 = 2
MAX_THREAD_4 = 4
# MAX_THREAD_16 = 16


def create_matrix_int(max_val, matrix_size_l, matrix_size_m):
    return np.random.randint(max_val, size=(matrix_size_l, matrix_size_m))


def create_matrix_float(max_val, matrix_size_l, matrix_size_m):
    return np.random.uniform(max_val, size=(matrix_size_l, matrix_size_m))


def save_matrix_to_csv(matrix, path_to_file):
    dataframe = pd.DataFrame(matrix)
    dataframe.to_csv(path_to_file, index=False, header=False)


def save_data_to_csv(data, path_to_file):
    dataframe = pd.DataFrame(data)
    dataframe.to_csv(path_to_file, index=False, header=False)


def load_matrix(path_to_file):
    file_name = open(path_to_file)
    matrix = np.loadtxt(file_name, delimiter=",")
    file_name.close()
    return matrix


def matrices_multiply(matrix_a, matrix_b):
    result = [[0 for col in range(len(matrix_b[0]))] for row in range(len(matrix_a))]
    for row in range(len(matrix_a)):
        for col in range(len(matrix_b[0])):
            for i in range(len(matrix_b)):
                result[row][col] += matrix_a[row][i] * matrix_b[i][col]
    return result


def multiply_matrix_by_scalar(matrix_a, scalar):
    for row in range(len(matrix_a)):
        for col in range(len(matrix_a[0])):
            matrix_a[row][col] *= scalar
    return matrix_a


def matrices_sum(matrix_a, matrix_b):
    result = [[matrix_a[row][column] + matrix_b[row][column] for column in range
    (len(matrix_a[0]))] for row in range(len(matrix_a))]
    return result


# dgemm - perform matrix operation C = alpha*op( A )*op( B ) + beta*C

def dgemm_calcs(matrix_a, matrix_b, matrix_c, alpha, betta):
    matrix_a_b = matrices_multiply(matrix_a, matrix_b)
    matrix_a_b_alpha = multiply_matrix_by_scalar(matrix_a_b, alpha)
    matrix_c_betta = multiply_matrix_by_scalar(matrix_c, betta)
    matrix_a_b_alpha_added_matrix_c_betta = matrices_sum(matrix_a_b_alpha, matrix_c_betta)
    return matrix_a_b_alpha_added_matrix_c_betta


def threaded_calc(matrix_a, matrix_b, matrix_c, alpha, betta):
    thread = list(range(MAX_THREAD_4))
    for i in range(MAX_THREAD_4):
        thread[i] = Thread(target=dgemm_calcs, args=(matrix_a, matrix_b, matrix_c, alpha, betta))
        thread[i].start()
    for i in range(MAX_THREAD_4):
        thread[i].join()


def get_statistics(time_lst, path_to_file):
    time_range = []
    for idx in range(1, len(time_lst)):
        time_range.append(time_lst[idx] - time_lst[idx - 1])
    time_min_value = min(time_range)
    time_max_value = max(time_range)
    time_mean_value = statistics.mean(time_range)
    time_median_value = statistics.median(time_range)
    time_std_dev_value = statistics.pstdev(time_range)
    statistics_list_python = ["time_min_value: " + str(time_min_value), "time_max_value: " + str(time_max_value),
                              "time_mean_value: " + str(time_mean_value),
                              "median_value: " + str(time_median_value), "std_dev_value: " + str(time_std_dev_value)]
    save_data_to_csv(statistics_list_python, path_to_file)
    return time_median_value


def graphics_create(time_median_value):
    final_stat = [time_median_value, 300, 400]

    # money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]

    def axis_format(x, pos):
        return '{:1.1f}'.format(x)

    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(axis_format)
    ax.bar(['Python', 'C#', 'Java'], final_stat)
    fig.savefig('stat_graph.png')
    plt.show()
