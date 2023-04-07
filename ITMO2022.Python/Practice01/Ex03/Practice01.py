import math

d1var = float(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) => "))
print("{:.0f}".format(d1var))
d2var = float(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы) => "))
print("{:.0f}".format(d2var))
hvar = float(input("Введите боковое смещение между спасателем и утопающим, h (ярды) => "))
print("{:.0f}".format(hvar))
vsand = float(input("Введите скорость движения спасателя по песку, v_sand (мили в час) => "))
print("{:.0f}".format(vsand))
nvar = float(input("Введите коэффициент замедления спасателя при движении в воде, n => "))
print("{:.2f}".format(nvar))
theta1 = float(input("Введите направление движения спасателя по песку, theta1 (градусы) => "))
print("{:.3f}".format(theta1))
x = d1var * 3 * math.tan(math.radians(theta1))
l1 = math.sqrt(x ** 2 + (d1var * 3) ** 2)
l2 = math.sqrt((hvar - x) ** 2 + d2var ** 2)
t = 1 / (vsand * 5280 / 3600) * (l1 + nvar * l2)

print(
    f"Если спасатель начнёт движение под углом theta1, равным {theta1:.0f} градусам, он достигнет утопащего через {t:.1f} секунды")
