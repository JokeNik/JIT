import math
import os

PI = 3.14159265359


def torad(x):
    return x * PI / 180

alpha = int(input()) #Угол наклона дрона относительно вертикальной линии против часовой стрелки
twobeta = int(input());#Градусный диапазон по горизонтали который видит дрон
twogama = int(input());#Градусный дипазон по вертикали который видит дрон
h = int(input());#высота надо объектом
phi = int(input());#угол поворота дрона относительно прямоугольный координат
x = int(input());#х координата дрона
y = int(input());#у координата дрона
beta = twobeta / 2#узнаем половинные углы
gama = twogama / 2#узнаем половинные углы

#Переводим в радианы
alpha = torad(alpha)
beta =  torad(beta)
gama = torad(gama)
phi = torad(phi)

#Считаеаем координаты трапеции
x1 = (x + math.tan(alpha - gama) * h) * math.cos(-phi) - (y - h / (math.cos(alpha - gama)) * math.tan(beta)) * math.sin(-phi)
y1 = (x + math.tan(alpha - gama) * h) * math.sin(-phi) + (y - h / (math.cos(alpha - gama)) * math.tan(beta)) * math.cos(-phi)
x2 = (x + math.tan(alpha - gama) * h) * math.cos(-phi) - (y + h / (math.cos(alpha - gama)) * math.tan(beta)) * math.sin(-phi)
y2 = (x + math.tan(alpha - gama) * h) * math.sin(-phi) + (y + h / (math.cos(alpha - gama)) * math.tan(beta)) * math.cos(-phi)

x3 = (x + math.tan(alpha + gama) * h) * math.cos(-phi) - (y - h / (math.cos(alpha + gama)) * math.tan(beta)) * math.sin(-phi)
y3 = (x + math.tan(alpha + gama) * h) * math.sin(-phi) + (y - h / (math.cos(alpha + gama)) * math.tan(beta)) * math.cos(-phi)
x4 = (x + math.tan(alpha + gama) * h) * math.cos(-phi) - (y + h / (math.cos(alpha + gama)) * math.tan(beta)) * math.sin(-phi)
y4 = (x + math.tan(alpha + gama) * h) * math.sin(-phi) + (y + h / (math.cos(alpha + gama)) * math.tan(beta)) * math.cos(-phi)

#print(alpha, beta, gama, phi, sep = " ")
#Вывод вершин трапеции в порядке обхода
print(x1, y1, sep = " ")
print(x2, y2, sep = " ")
print(x4, y4, sep = " ")
print(x3, y3, sep = " ")

