# CALCULADORA DE IMC COM CATEGORIZAÇÃO
# ENTREGA ATÉ 04/09/2025
# FAZER UM FORK E UM PULL REQUEST PARA ENTREGAR
# Nome: Isabella Rocha Da Silvas
def calcular_imc(peso, altura):
    return peso / altura**2

print('Olá, bem vindo (a)! ')
peso = float(input("Insira seu peso em kg: "))
altura = float(input('Insira sua altura: '))


imc = calcular_imc(peso, altura)
print("Seu IMC equivale a: ", imc)
if imc <= 18.5:
    print("Você está abaixo do peso.")
elif imc <= 24.9:
    print("Parabéns! Seu está com o peso normal.")
elif imc <= 29.9:
    print("Você está com sobrepeso.")
elif imc <= 34.9:
    print("Você está com Obesidade Grau I.")
elif imc <= 39.9:
    print("Você está com Obesidade Grau II.")
else:
    print("Você está com Obesidade Grau III. ")