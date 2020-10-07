# Minimos Cuadrados
import matplotlib.pyplot as plt
import numpy as np
import math
from os import system, name

# ---Variables a usar ---

n = 0  # Tamaño del dataset
x_axis = []  # Datos del eje x
y_axis = []  # Datos del eje y
xTy = []  # Lista con el resultado de x * y
x_square = []  # lista con el resultado de x^2
y_axis_plot = []  # Lista con y despues del metodo de minimos cuadrados
x_less_xprom = []  # Lista con x menos el promedio de x
y_less_yprom = []  # lista con y menos el promedio de y
x_less_xprom_sqrt = []  # Lista con x menos el promedio de x, todo al cuadrado
y_less_yprom_sqrt = []  # Lista con y menos el promedio de y, todo al cuadrado
# Lista con x menos el promedio de x multiplicado por y menos el promedio de y
xlp_times_ylp = []
table = []  # Lista de apoyo para hacer la tabla
colLabels = ["x", "y", "x*y", "x^2", "y=mx+b"]


# Funcion para limpiar consola


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


clear()
print("Programa de minimos Cuadrados")
print("Titulo de dataset: ", end="")
tittle = input()

print("Cual es el tamaño del dataset?")
n = int(input())
rowLabels = ["{:X}".format(i+1) for i in range(n)]
clear()

print("Que valor representa 'X'?")
xTittle = input()

print("Se procedera a introducir datos del eje x")

for i in range(n):
    print(f"Favor de introducir el dato #{i+1} de 'x'")
    x = int(input())
    x_axis.append(x)
    clear()

print("Que valor representa 'Y'")
yTittle = input()

print("Se procedera a introducir datos del eje y")

for i in range(n):
    print(f"Favor de introducir el dato #{i+1} de 'y'")
    y = int(input())
    y_axis.append(y)
    clear()

for x in x_axis:
    x_square.append(x*x)

for i in range(n):
    value = x_axis[i] * y_axis[i]
    xTy.append(value)

m = (n * sum(xTy) - sum(x_axis) * sum(y_axis)) / \
    (n * sum(x_square) - sum(x_axis) * sum(x_axis))
b = (sum(y_axis) * sum(x_square) - sum(x_axis) * sum(xTy)) / \
    (n * sum(x_square) - sum(x_axis) * sum(x_axis))

for value in x_axis:
    y_value = m * value + b
    y_value = float("{:.2f}".format(y_value))
    y_axis_plot.append(y_value)


promx = sum(x_axis) / n
promy = sum(y_axis) / n

for x in x_axis:
    x_less_xprom.append(x-promx)

for x in x_less_xprom:
    x_less_xprom_sqrt.append(x*x)

for y in y_axis:
    y_less_yprom.append(y-promy)

for y in y_less_yprom:
    y_less_yprom_sqrt.append(y*y)

for i in range(n):
    xlp_times_ylp.append(x_less_xprom[i]*y_less_yprom[i])

r = sum(xlp_times_ylp) / (math.sqrt(sum(x_less_xprom_sqrt))
                          * math.sqrt(sum(y_less_yprom_sqrt)))


# Tabla
table.append(x_axis)
table.append(y_axis)
table.append(xTy)
table.append(x_square)
table.append(y_axis_plot)

tTable = np.transpose(table)

fig, (gra, tab) = plt.subplots(2, 1)

gra.plot(x_axis, y_axis, 'ks', x_axis, y_axis_plot)
gra.set_title(tittle)
gra.set(xlabel=xTittle, ylabel=yTittle)
trans = gra.get_xaxis_transform()
gra.annotate(f"m = {m}\nb = {b}\nr = {r}", xy=(x_axis[-1], y_axis_plot[-1]),
             xycoords='data', textcoords="offset points", xytext=(30, 0))

gtab = tab.table(cellText=tTable, colLabels=colLabels,
                 rowLabels=rowLabels, cellLoc="center", loc="upper left")
gtab.auto_set_font_size(False)
gtab.set_fontsize(24)
#gtab.scale(2, 2)
tab.set_axis_off()

#plt.subplots_adjust(bottom=0, left=0.)
plt.grid()
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.show()
