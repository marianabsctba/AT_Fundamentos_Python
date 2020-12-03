#6) Escreva uma função em Python que:
#leia uma tupla contendo números inteiros,
#retorne uma lista contendo somente os números ímpares
#e uma nova tupla contendo somente os elementos nas posições pares.

#acrescentei tupla com os números pares também, além do index

def read_t(tupl):
    return tupl

def show_int(tupl):
    return [n for n in tupl if n % 2 != 0]

def show_p(tupl):
    return tuple(n for n in tupl if n % 2 == 0)

def show_index(tupl):
    return tuple(n for i, n in enumerate(tupl) if i % 2 == 0)


t = (1, 2, 44, 67, 89, -1, 99, 118, 125, 149, 3, 7)

l_i = show_int(t)
tup_p = show_p(t)
s_index = show_index(t)

print(f"Tupla: {read_t(t)}")
print(f"Lista de ímpares: {l_i}")
print(f"Tupla de pares: {tup_p}")
print(f"Tupla com elementos em posições pares: {s_index}")
