#Faça um programa que leia a altura e o sexo de uma pessoa, calcule seu peso ideal, utilizando as seguintes fórmulas:
altura = float(input('Digite a sua altura:'))
peso = float(input('Digite o seu peso:'))
sexo = input('Qual é o seu sexo?(F/M) ')
if sexo == 'M':
    soma = (62.1 * altura) - 44.7
    print (f'Seu peso ideal é: {soma}')
else:
    soma = (72.7 * altura) - 58
    print (f' Seu peso ideal é: {soma}')