#Usando o Thonny, escreva uma função em Python chamada potencia. Esta função deve obter como argumentos dois números inteiros, A e B,
#e calcular AB usando multiplicações sucessivas (não use a função de python math.pow) e retornar o resultado da operação.
#Depois, crie um programa em Python que obtenha dois números inteiros do usuário e indique o resultado de AB usando a função.

def potency(A, B):
    pot = A ** B
    return pot


A = int(input("Digite um número (base): "))
B = int(input("Digite um número (potência): "))

print(f"Base: {A} -- Expoente: {B} -- Resultado: {potency(A, B)}")
