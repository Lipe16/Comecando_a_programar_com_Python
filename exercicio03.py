# -*- coding: UTF-8 -*-
# Escreva um programa que resolva uma equação de segundo grau. 

# a2 -4 .a.c
#delta = - b [+-] raiz(delta)/2.a

from math import sqrt

a = float(input("Digite valor de a: "))
b = float(input("Digite valor de b: "))
c = float(input("Digite valor de c: "))


delta = b**2 - 4*a*c

x1 = (-b + sqrt(delta))/(2*a)
x2 = (-b - sqrt(delta))/(2*a)

print("x1 = %f \n" %(x1))
print("x2 = %f \n" %(x2))


