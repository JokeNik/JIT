import math
import os

PI = 3.14159265359


def torad(x):
    return x * PI / 180

alpha = int(input())
twobeta = int(input());
twogama = int(input());
h = int(input());
phi = int(input());
x = int(input());
y = int(input());
beta = twobeta / 2
gama = twogama / 2

alpha = torad(alpha)
beta =  torad(beta)
gama = torad(gama)
phi = torad(phi)


x1 = (x + math.tan(alpha - gama) * h) * math.cos(-phi) - (y - h // (math.cos(alpha - gama) * math.tan(beta))) * math.sin(-phi)
y1 = (x + math.tan(alpha - gama) * h) * math.sin(-phi) + (y - h // (math.cos(alpha - gama) * math.tan(beta))) * math.cos(-phi)
x2 = (x + math.tan(alpha - gama) * h) * math.cos(-phi) - (y + h // (math.cos(alpha - gama) * math.tan(beta))) * math.sin(-phi)
y2 = (x + math.tan(alpha - gama) * h) * math.sin(-phi) + (y + h // (math.cos(alpha - gama) * math.tan(beta))) * math.cos(-phi)

x3 = (x + math.tan(alpha + gama) * h) * math.cos(-phi) - (y - h // (math.cos(alpha + gama) * math.tan(beta))) * math.sin(-phi)
y3 = (x + math.tan(alpha + gama) * h) * math.sin(-phi) + (y - h // (math.cos(alpha + gama) * math.tan(beta))) * math.cos(-phi)
x4 = (x + math.tan(alpha + gama) * h) * math.cos(-phi) - (y + h // (math.cos(alpha + gama) * math.tan(beta))) * math.sin(-phi)
y4 = (x + math.tan(alpha + gama) * h) * math.sin(-phi) + (y + h // (math.cos(alpha + gama) * math.tan(beta))) * math.cos(-phi)

#print(alpha, beta, gama, phi, sep = " ")
print(x1, y1, sep = " ")
print(x2, y2, sep = " ")
print(x4, y4, sep = " ")
print(x3, y3, sep = " ")
