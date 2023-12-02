vet = []
maiorValor = menorValor = menorPosicao = maiorPosicao = 0.0

while len(vet) < 10:
    vet.append(float(input("Informe um valor: ")))

for i in range(len(vet)):
    if vet[i] > maiorValor:
        maiorValor = vet[i]

    if vet[i] < menorValor:
        menorValor = vet[i]

print(f"A posição do maior valor é: {maiorPosicao}")
print(f"A posição do menor valor é: {menorPosicao}")
print(f"A diferença desses valores é: {maiorValor-menorValor}")
