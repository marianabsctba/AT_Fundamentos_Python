#1) Usando o Thonny, escreva um programa em Python que leia uma tupla contendo 3 números inteiros, (n1, n2, n3) e os imprima em ordem crescente.
# Versão 01

def order(t):
    return sorted(t)

  
t = (10, 15, 1)

print(f"Essa é a sua tupla: {t}")

print(f"Essa é a sua tupla ordenada: {tuple(order(t))}")
