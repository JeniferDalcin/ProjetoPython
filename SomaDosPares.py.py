from random import randint


números = list()
def sorteia(lista):
   for c in range(0, 5):
       números.append(randint(1, 10))
   print(f'Sorteei os números {números}.')


def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'A soma dos valores pares da lista é {soma}.')

# Programa Principal:
sorteia(números)
somapar(números)
