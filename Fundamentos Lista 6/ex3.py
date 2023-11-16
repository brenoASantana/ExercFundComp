numPar = [0] * 10
i = 0

while len(numPar) < 10:
    n = int(input("Informe um valor:\n"))

    if n % 2 != 0:
        numPar[i] = n

    i += 1

print(numPar)
