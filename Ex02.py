#Escrever um programa que lê o número de um funcionário, o número de horas por ele trabalhadas, 
# o valor que recebe por hora, o número de filhos com idade inferior a 14 anos, a idade, o tempo de serviço do funcionário e o valor do salário família por filho. 
# Calcular o salário bruto, o desconto do INSS (8,5% do salário bruto) e o salário família. Calcular o IR (Imposto de Renda) como segue: 
#Se SB > 1.500,00 então IR = 15% do SB
#Escrever o número do funcionário, salário bruto, total dos descontos, e salário líquido:
funcionario = float(input('Digite o seu número de funcionário:'))
horas = float(input('Digite as horas trabalhadas mensais:'))
valor = float(input('Digite o valor que você recebe por hora trabalhada:'))
filhos = int(input('Caso você tenha filhos menores de 14 anos, digite o número de filhos:'))
idade = int(input('Digite a sua idade:'))
tempo_servico = float(input('Digite o tempo de serviço que você tem registrado:'))
salario_familia = float(input('Informe o valor do salário família por filho:'))
salario_familia_total = salario_familia * filhos
bruto = (horas * valor) + salario_familia_total
inss = bruto * 0.085
if bruto > 1500:
    ir = bruto  * 0.15
if (bruto > 500 ) and (bruto <= 1500):
    ir = bruto * 0.08
else:
    ir = 0
total_desconto = inss + ir
salario_liquido = bruto - total_desconto
print (f' Funcionário: {funcionario} você recebe de salário bruto o valor : R$ {bruto} e tem descontos de R$: {total_desconto} sendo seu salário líquido de R$: {salario_liquido}')
