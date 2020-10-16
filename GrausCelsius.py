
print("Content-Type: text/html\n\n")
print('=======Transformação de graus Celsius para Fahrenheit=======')

print('-------------------------------------------------------------')
print('Formula C =  F - 32 ')
print('       ___   ______ ')
print('        5      9    ')

Celsius = int(input('Informe graus em C° :'))
C = 9 * Celsius
F = 5 * 32
CelsiusMaisFahrenheit = C + F
Fahrenheit = CelsiusMaisFahrenheit / 5
print('5 (F-32) = 9 x {}'.format(Celsius))
print('5F - {} = {}'.format(F, C))
print('5F = {} + {}'.format(C, F))
print('5F = {}'.format(CelsiusMaisFahrenheit))
print('F = {}'.format(CelsiusMaisFahrenheit))
print('   ----      ')
print('     5       ')
print('F = {}'.format(Fahrenheit))
