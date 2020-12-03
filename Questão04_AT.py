#4) Escreva um programa em Python que leia um vetor de 5 números inteiros e o apresente na ordem inversa.
# Imprima o vetor no final. Use listas.  


#acrescentei itens a mais no exercício
    
def showVector(l):
    return l

def reverseVector(l):
    l.reverse()
    return l

def sortVector(l):
    l.sort()
    return l

l = []
while len(l)<5:
    n = int(input("Digite 5 elementos para o vetor: "))
    l.append(n)
        
print(f"Vetor digitado: {showVector(l)}")
print(f"Vetor invertido: {reverseVector(l)}")
print(f"Vetor ordenado: {sortVector(l)}")
