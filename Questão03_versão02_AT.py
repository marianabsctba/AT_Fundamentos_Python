#Questão 03, versão 02. 

#Isso porque "n vezes n" e "n elevado à potência n" são iguais e, portanto, também responderia ao exercício com um operador comum e com multiplicação.

def exp_AB(A, B):
    return A**B

A = int(input("Digite a base: "))
B = int(input("Digite o expoente: "))

print(f"Base: {A}\nExpoente: {B}")
print(f"Resultado: {exp_AB(A, B)}")
