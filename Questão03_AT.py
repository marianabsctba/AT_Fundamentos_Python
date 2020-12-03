#Usando o Thonny, escreva uma função em Python chamada potencia. Esta função deve obter como argumentos dois números inteiros, A e B,
#e calcular AB usando multiplicações sucessivas (não use a função de python math.pow) e retornar o resultado da operação.
#Depois, crie um programa em Python que obtenha dois números inteiros do usuário e indique o resultado de AB usando a função.

def mult_a_b(a, b):
    sums = sum(b for _ in range(abs(a)))
    return sums 

def power(a, b):
    sums = 1
    for _ in range(b):
        sums = mult_a_b(sums, a)
    return sums

a = int(input("Digite a base: "))
b = int(input("Digite o expoente: "))

print(f"Base: {a}  - Expoente: {b}")
print(f"Resultado: {pot(a, b)}")
