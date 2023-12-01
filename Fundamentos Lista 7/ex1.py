vetpos = []
vetneg = []

for i in range(10):
    n = int(input("Informe um valor:\n"))

    if n > 0:
        vetpos += [n]
    if n < 0:
        vetneg += [n]

print(f"Vetor Positivo: {vetpos}")
print(f"Vetor Negativo: {vetneg}")
