import math

d1_var_yards = float(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) => "))
print("{:.0f}".format(d1_var_yards))
d2_var_feet = float(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы) => "))
print("{:.0f}".format(d2_var_feet))
h_var_yard = float(input("Введите боковое смещение между спасателем и утопающим, h (ярды) => "))
print("{:.0f}".format(h_var_yard))
v_sand = float(input("Введите скорость движения спасателя по песку, v_sand (мили в час) => "))
print("{:.0f}".format(v_sand))
n_var_slowdown = float(input("Введите коэффициент замедления спасателя при движении в воде, n => "))
print("{:.2f}".format(n_var_slowdown))
theta1 = float(input("Введите направление движения спасателя по песку, theta1 (градусы) => "))
print("{:.3f}".format(theta1))
x = d1_var_yards * 3 * math.tan(math.radians(theta1))
l1 = math.sqrt(x ** 2 + (d1_var_yards * 3) ** 2)
l2 = math.sqrt((h_var_yard * 3 - x) ** 2 + d2_var_feet ** 2)
t = 1 / (v_sand * 5280 / 3600) * (l1 + n_var_slowdown * l2)

print(
    f"Если спасатель начнёт движение под углом theta1, равным {theta1:.0f} градусам, он достигнет утопащего через {t:.1f} секунды")
