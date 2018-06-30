# -*- coding: UTF-8 -*-
#Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade. 

idade = int(input("Digite sua idade: "))

if idade >= 18:
	print("maior de idade")
elif idade > 0 and idade < 18:
	print("menor de idade")
else:
	print("idade inválida")