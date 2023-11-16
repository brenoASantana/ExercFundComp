vetpos = [0] * 10
vetneg = [0] * 10

for i in range(10):
    n = int(input("Informe um valor:\n"))

    if n > 0:
        vetpos[i] = n
    if n < 0:
        vetneg[i] = n

print(f"Vetor Positivo: {vetpos}")
print(f"Vetor Negativo: {vetneg}")
