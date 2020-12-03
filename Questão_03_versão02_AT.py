def exp_AB(A, B):
    return A**B

A = int(input("Digite a base: "))
B = int(input("Digite o expoente: "))

print(f"Base: {A}\nExpoente: {B}")
print(f"Resultado: {exp_AB(A, B)}")
