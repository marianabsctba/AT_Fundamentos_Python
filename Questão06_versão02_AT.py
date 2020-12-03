#6) Escreva uma função em Python que:
#leia uma tupla contendo números inteiros,
#retorne uma lista contendo somente os números ímpares
#e uma nova tupla contendo somente os elementos nas posições pares.

#acrescentei tupla com os números pares também, além do index. Nessa versão, ainda, incluí input do usuário e uso de listas

def read_t(tupl):
    return tuple(tupl)

def show_int(tupl):
    return [n for n in tupl if n % 2 != 0]

def show_p(tupl):
    return tuple(n for n in tupl if n % 2 == 0)

def show_index(tupl):
    return tuple(n for i, n in enumerate(tupl) if i % 2 == 0)

t = []
n = int(input("Digite o número de elementos na tupla: "))
for e in range(1, n+1):
    user_t = int(input(f"Digite o {e}° número inteiro: "))
    t.append(user_t)

l_i = show_int(t)
tup_p = show_p(t)
s_index = show_index(t)

print(f"Tupla: {read_t(t)}")
print(f"Lista de ímpares: {l_i}")
print(f"Tupla de pares: {tup_p}")
print(f"Tupla com elementos em posições pares: {s_index}")
