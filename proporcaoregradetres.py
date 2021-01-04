print('-=-' * 20)
print('Proporção  Diretamente ou Iversamente proporcional')
print('--' * 30)
print('A proporção é uma relação de igualdade entre razões ')
print('e, assim, apresenta a comparação de duas grandezas')
print('em diferentes situações.')
print('--' * 30)
print('a   c')
print('- = -')
print('b   d')

print('Le desta forma  a esta  para b assim com  c esta para d ')

a = int(input('Digite um numero para   a:_'))
b = int(input('Digite um numero para   b:_'))
c = int(input('Digite um numero para   c:_'))
d = int(input('Digite um numero para   d:_'))
print('--'*20)
numerador_a = a / b
denominador_b = c / d
razao_n = numerador_a
razao_d = denominador_b

print(' {}       {}'.format(a,c))
print('_____ = ______')
print(' {}       {}'.format(b,d))

print('')
print('{:.2f} = {:.2f}'.format(numerador_a, denominador_b))
if razao_n == razao_d:
    print('(k) Constante ')
    print('')
    print('A razao é diretamente proporcional ')
else:
    if razao_n != razao_d:
        print('')
        print('A razao é inversamente proporcional')
