#2) Usando o Thonny, escreva um programa em Python que some todos os números pares de 1 até um dado n, inclusive.
#O dado n deve ser obtido do usuário. No final, escreva o valor do resultado desta soma.

def line():
    print("=" * 50)
    

def hello():
    return f"==  PROGRAMA QUE SOMA NÚMEROS PARES EM INTERVALO PROPOSTO =="

def sum_n():
    line()
    num = int(input("Digite um número inteiro: "))
    s = 0
    for a in range(2, num+1, 2):
        if a % 2 == 0:
            s += a
    line()
    return f"A soma dos números pares entre 1 e {num} é {s}."
    
def end():
    line()
    return f"FIM!"
    
print(hello())
print(sum_n())
print(end())
