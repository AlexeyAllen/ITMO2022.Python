import math


# def params_input():
#     d1_var_yards = float(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) => "))
#     print("{:.0f}".format(d1_var_yards))
#     d2_var_feet = float(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы) => "))
#     print("{:.0f}".format(d2_var_feet))
#     h_var_yard = float(input("Введите боковое смещение между спасателем и утопающим, h (ярды) => "))
#     print("{:.0f}".format(h_var_yard))
#     v_sand = float(input("Введите скорость движения спасателя по песку, v_sand (мили в час) => "))
#     print("{:.0f}".format(v_sand))
#     n_var_slowdown = float(input("Введите коэффициент замедления спасателя при движении в воде, n => "))
#     print("{:.2f}".format(n_var_slowdown))
#     # theta1 = float(input("Введите направление движения спасателя по песку, theta1 (градусы) => "))
#     # print("{:.3f}".format(theta1))


def calcs(d1_var_yards, d2_var_feet, h_var_yard, v_sand, n_var_slowdown):
    theta_idx = 0
    time_minimum = 1000000
    theta1_optimum = 0
    true = False
    while theta_idx < 90:
        theta_idx += 0.001
        x = d1_var_yards * 3 * math.tan(math.radians(theta_idx))
        l1 = math.sqrt(x ** 2 + (d1_var_yards * 3) ** 2)
        l2 = math.sqrt((h_var_yard * 3 - x) ** 2 + d2_var_feet ** 2)
        time_flag = (l1 + n_var_slowdown * l2) / (v_sand * 5280 / 3600)
        theta2_flag = math.atan2((h_var_yard * 3 - x), d2_var_feet)
        if time_minimum <= time_flag:
            continue
        time_minimum = time_flag
        theta1_optimum = theta_idx
        theta2 = math.degrees(theta2_flag)
        value1 = round(math.sin(math.radians(theta1_optimum)), 3)
        value2 = round(n_var_slowdown * math.sin(math.radians(theta2)), 3)
        true = value1 == value2

    print(
        f"Если спасатель начнёт движение под углом theta1, равным {theta1_optimum:.0f} градусам, он достигнет утопащего"
        f" через минимальное время равное {time_minimum:.1f} секунды")

    if true:
        print('Формула определеляющая оптимальный угол движения спасателя: "Theta1 = n * Theta 2" выполняется')


calcs(8, 10, 50, 5, 2)
