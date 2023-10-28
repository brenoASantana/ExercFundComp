import math

n = int(input("Informe um número: "))

if n <= 0:
    print("Informe um número maior que zero.")

for cont in range(1, n+1):
    sqrt = math.sqrt(n)