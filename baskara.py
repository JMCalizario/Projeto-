import math

print('*' * 30)
print('BHASKARA')
print('x  = - b ± raiz b² - 4 * a * c')
print('     -------------------------')
print('             2 * a')
print('*' * 30)
a = int(input('Informe o valor de a :_'))
b = int(input('Informe o valor de b :_'))
c = int(input('Informe o valor de c :_'))
print('*' * 30)

aux0 = - 4
aux1 = 2 * a
aux2 = b ** 2
aux3 = a * c
aux4 = aux0 * aux3
subtra = aux2 - - aux4
raiz = math.sqrt(subtra)
auxDex1 = - b + raiz
x1 = - (b // raiz)
auxDex2 = - (b + raiz)
x2 = auxDex2 / aux1
print('x  = - b ± raiz b² - 4 * a * c')
print('    ---------------------------')
print('             2 . a      \n')
print('x = - {} ± raiz de {}² {} . {} . {}'.format(b, b, aux0, a, c))
print('    ----------------------------')
print('             2 . {} \n'.format(a))
print('x = - {} ± raiz de {} {} . {} . {}'.format(b, aux2, aux0, a, c))
print('    -----------------------------')
print('               {}\n'.format(aux1))
print('x= - {} ±  raiz de {} {} . {}'.format(b, aux2, aux0, aux3))
print('     ---------------------------')
print('               {}\n'.format(aux1))
print('x = - {} ± raiz de {} {} '.format(b, aux2, aux4))
print('     ---------------------------')
print('               {}\n'.format(aux1))
print('x = - {} ± raiz de {}'.format(b, subtra))
print('    -----------------------------')
print('               {}\n'.format(aux1))
print('x = - {} ± raiz de  {:.0f}'.format(b, raiz))
print('   ------------------------------')
print('               {}\n'.format(aux1))
print('X1= - {} ± {}  '.format(b, subtra))
print(' -------------')
print('    {}\n '.format(aux1))
print(' X1 = {:.0f}'.format(auxDex1))
print('---------------')
print('    {}\n '.format(aux1))
print(' X1 = {:.0f}\n'.format(x1))
print('*' * 30)
print('X2 = {:.0f}'.format(auxDex2))
print('---------------')
print('    {}\n'.format(aux1))
print('X2 ={}'.format(x2))
