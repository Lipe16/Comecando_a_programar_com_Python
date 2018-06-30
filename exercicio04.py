# -*- coding: UTF-8 -*-
# Escreva um programa que ordene uma lista numérica com três elementos. 

lista = [5,2,6]

#Select Sort

for i in range(len(lista)): 
	menor = i
	for j in range(i+1 , len(lista)):
		if lista[j] < lista[menor]:
			menor = j
	
	if lista[menor] != lista[i]:
		aux = lista[menor]
		lista[menor] = lista[i]
		lista[i] = aux

print(lista)
	