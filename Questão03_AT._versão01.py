#Usando o Thonny, escreva uma função em Python chamada potencia. Esta função deve obter como argumentos dois números inteiros, A e B,
#e calcular AB usando multiplicações sucessivas (não use a função de python math.pow) e retornar o resultado da operação.
#Depois, crie um programa em Python que obtenha dois números inteiros do usuário e indique o resultado de AB usando a função.

def mult_AB(A, B):
    sums = sum(B for _ in range(abs(A)))
    return sums 

def exp_AB(A, B):
    sums = 1
    for _ in range(B):
        sums = mult_AB(sums, A)
    return sums

A = int(input("Digite a base: "))
B = int(input("Digite o expoente: "))

print(f"Base: {A}\nExpoente: {B}")
print(f"Resultado: {exp_AB(A, B)}")
