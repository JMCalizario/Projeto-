print('=============  Teoria da Igualdade dos Conjutos   =============')
print('----------------------------------------------------------')
print('Dizemos que um conjunto de A é Igual B, Escrevendo A = B se os elementos são iguais ')
print('Sendo B = {1,2,3,4}')
print('----------------------------------------------------------')
n1a = int(input('Informe o 1ª  numero  para o A'))
n2a = int(input('Informe o 2ª  numero para A'))
n3a = int(input('Informe o 3º  numero para A '))
n4a = int(input('Informe o 4º  numero para A'))
print('-----------------------------------------------------------')

n1b = 1
n2b = 2
n3b = 3
n4b = 4

a = [n1a, n2a, n3a, n4a]
b = [n1b, n2b, n3b, n4b]

if a == b:
    print('Os numeros {},{},{},{}'.format(n1a, n2a, n3a, n4a))
    print('A {} Pertencem ao conjunto de  B {} '.format(a, b))



else:
    print('Os numeros não pertecem ao conjuto de  B')
