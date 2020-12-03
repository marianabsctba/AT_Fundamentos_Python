#6) Escreva uma função em Python que:
#leia uma tupla contendo números inteiros,
#retorne uma lista contendo somente os números ímpares
#e uma nova tupla contendo somente os elementos nas posições pares.
 
 
def read_t(tupl):
    return tupl

def show_i(tupl):
    return [n for n in tupl if n % 2 != 0]

def show_p(tupl):
    return tuple(n for n in tupl if n % 2 == 0)


t = (1, 2, 44, 67, 89, -1, 99, 118, 125, 149, 3, 7)

l_i = show_i(t)
tup_p = show_p(t)

print(f"Tupla: {read_t(t)}")
print(f"Lista de ímpares: {l_i}")
print(f"Tupla de pares: {tup_p}")
