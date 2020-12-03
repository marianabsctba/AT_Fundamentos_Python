#Questão 03, versão 02 c/ recursiva

def potencia(a, b):
    if b == 0:
        return 1
    else:
        return a*potencia(a, b-1)

A = int(input("Base: "))
B = int(input("Expoente: "))

p = potencia(A, B)

print(f"Resultado: {p}")


