a = int(input("Digite o valor de A:\n"))
b = int(input("Digite o valor de B:\n"))

print(f'Valores Iniciais:\nA={a} B={b}')

## variável intermediaria para armazenar temporariamente um valor
temp = a
a = b
b = temp

print(f'Valores Finais:\nA={a} B={b}')
