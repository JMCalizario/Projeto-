from typing import List

print( '\033[0;30;41m-Subconjuntos Matemáticos ' )
print( '\033[0;37;40m' )
print( '-1 Dados 2 conjuntos A e B chama-se união de A e B o conjunto formado pelos elementos que ' )
print( 'pertencem a A ou B.' )
a = {1, 2, 3}
b = {2, 4}
print( 'a={} e b={}'.format( a, b ) )
print('A U B {} '.format(a.union(b)))
