#6) Escreva uma função em Python que:
#leia uma tupla contendo números inteiros,
#retorne uma lista contendo somente os números ímpares
#e uma nova tupla contendo somente os elementos nas posições pares.
 
 
 # alteração do exercício para trabalhar com listas e tuplas
 
def read_t(tupl):
    return tuple(tupl)

def show_i(tupl):
    return [n for n in tupl if n % 2 != 0]

def show_p(tupl):
    return tuple(n for n in tupl if n % 2 == 0)


t = []
n = int(input("Digite o número de elementos na tupla: "))
for e in range(1, n+1):
    user_t = int(input(f"Digite o {e}° número inteiro: "))
    t.append(user_t)


l_i = show_i(t)
tup_p = show_p(t)

print(f"Tupla digitada: {read_t(t)}")
print(f"Lista de ímpares: {l_i}")
print(f"Tupla de pares: {tup_p}")
