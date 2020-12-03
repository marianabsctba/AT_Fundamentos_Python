#Questão 03, versão 02. 

def potencia(A, B):
    sums = 1
    t = 0
    for n in range(B):
        sums *= A
        t += 1
    return sums

A = int(input("Base: "))
B = int(input("Expoente: "))

print(f"Resultado: {potencia(A, B)}")


