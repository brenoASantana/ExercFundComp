vetor=[12,25,33,37,48,57,86,92]

inf= 0
sup= len(vetor)-1
busca = int(input('Qual o valor da busca: '))
while inf <=sup : 
    med=int((inf+sup)/2)
    if vetor [med] == busca:
        print(f'O valor {busca} se encontra no posição {med} ')
        break
    elif busca < vetor[med]:
        sup = med-1
    else:
        inf = med+1
        
    

