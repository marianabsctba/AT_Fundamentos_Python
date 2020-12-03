#1) Usando o Thonny, escreva um programa em Python que leia uma tupla contendo 3 números inteiros,
#(n1, n2, n3) e os imprima em ordem crescente.

#Versão 02, usando input do usuário (que poderia ser maior do que 3 e trabalhando com tuplas e listas)

def order(t):
    return tuple(t), tuple(sorted(t))


t = []
n = int(input("Digite o número de elementos na tupla: "))
for e in range(1, n+1):
    user_l = int(input(f"Digite o {e}° número inteiro: "))
    t.append(user_l)


print(f"Essa é a sua tupla digitada: {order(t)[0]}")
print(f"Essa é a sua tupla ordenada: {order(t)[1]}")
