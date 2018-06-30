# -*- coding: UTF-8 -*-
#Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.

numero1 = float(input("Digite o primeiro numero: "))
operador = input("Digite o operador: ")
numero2 = float(input("Digite o segundo numero: "))

#soma
if operador == "+":
	resultado = numero1+numero2
#subtracao
elif operador == "-":
	resultado = numero1-numero2
#multiplicacao
elif operador == "*":
	resultado = numero1*numero2
#divisao
elif operador == "/":
	resultado = numero1/numero2
	
print(resultado)
	
 