m1, m2, mS = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

ordem = 1

for lin in range(len(m1)):
    for col in range(len(m1[lin])):
        m2[col] = int(
            input(f"Informe o valor da {ordem}º matriz na coordenada [{lin},{col}]: ")
        )

ordem += 1

for lin in range(len(m2)):
    for col in range(len(m2[lin])):
        m2[col] = int(
            input(f"Informe o valor da {ordem}º matriz na coordenada [{lin},{col}]: ")
        )

for lin in range(len(mS)):
    for col in range(len(ms[lin])):
        ms[lin][col] = m1[lin][col] + m2[lin][col]

print("Matriz 1: ", m1)
print("Matriz 2: ", m2)
print("Matriz Soma: ", mS)
