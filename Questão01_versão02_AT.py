#1) Usando o Thonny, escreva um programa em Python que leia uma tupla contendo 3 números inteiros,
#(n1, n2, n3) e os imprima em ordem crescente.
#Versão 02

def order(l):
    return sorted(l)    


l = []
n = int(input("Digite o número de elementos na tupla: "))
for e in range(1, n+1):
    user_l = int(input(f"Digite o {e}° número inteiro: "))
    l.append(user_l)


print(f"Essa é a sua tupla digitada: {tuple(l)}")
print(f"Essa é a sua tupla ordenada: {tuple(order(l))}")
