#3)Usando o Thonny, escreva uma função em Python chamada potencia. Esta função deve obter como argumentos dois números inteiros, A e B,
#e calcular AB usando multiplicações sucessivas (não use a função de python math.pow) e retornar o resultado da operação.
#Depois, crie um programa em Python que obtenha dois números inteiros do usuário e indique o resultado de AB usando a função.

def potencia(A, B):
    sums = 1
    while B > 0:
        sums *= A
        B -= 1
    return sums
   
A = int(input("Base: "))
B = int(input("Expoente: "))
    
print(potencia(A, B))
