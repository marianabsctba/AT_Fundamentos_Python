#2) Usando o Thonny, escreva um programa em Python que some todos os números pares de 1 até um dado n, inclusive.
#O dado n deve ser obtido do usuário. No final, escreva o valor do resultado desta soma.


def line():
    print("=" * 50)    

def hello():
    return f"==  PROGRAMA QUE SOMA NÚMEROS PARES EM INTERVALO PROPOSTO  =="

def sum_n(n):
    line()
    s = 0
    for a in range(2, n+1, 2):
        if a % 2 == 0:
            s += a
    return s       

def end():
    line()
    return "FIM!"


num = int(input("Digite um número inteiro: "))

sum_even = sum_n(num)

print(hello())
print(f"A soma até o número {num}) é: {sum_even}")
print(end())

