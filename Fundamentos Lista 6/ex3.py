numImpar = [0] * 10
quant = 0

## Como que vou declarar um vetor e inserir nele depois???

while quant < 10:
    n = int(input("Informe um valor: "))

    if n % 2 != 0:
        numImpar.insert(quant,n)
        quant += 1

print(numImpar)
