#Desenvolver um programa em python que solicite a digitação de um numero inteiro e mostrar os numeros primos entre 1 e esse numero lido
lista = []
num = int(input("Digite um numero: "))
for i in range(2, num):
    if i == 2:
        lista.append(i)
    if i == 3:
        lista.append(i)
    if i == 5:
        lista.append(i)   
    elif i % 2 != 0:
        if i % 3 != 0:
            if i % 5 != 0:
                lista.append(i)
    else:
        continue
    
print(lista)