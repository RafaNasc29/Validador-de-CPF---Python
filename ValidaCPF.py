"""
    Validador de CPF
"""

CPF = input('Porfavor Digite um CPF (com os pontos "." e o traço "-"entre os números): ')

novoCPF = CPF[:-2]
Nprim = ''
contP = 10
contS = 11
somaP = 0
somaS = 0
primeiro = 0
segundo = 0

# Para o Primeiro Digito
for n in CPF[0:11]:
    if not n == '.':
        Nprim += n

for x in Nprim:
    if x.isnumeric():
        x = int(x)

    multP = x * contP
    somaP = somaP + multP
    contP -= 1

resultadoP = 11 - (somaP % 11)

if resultadoP > 9:
    primeiro = 0
else:
    primeiro = resultadoP

Nprim += str(primeiro)

# Para o Segundo Digito
for n in Nprim:
    if n.isnumeric():
        n = int(n)

    multS = n * contS
    somaS = somaS + multS
    contS -= 1

resultadoS = 11 - (somaS % 11)

if resultadoS > 9:
    segundo = 0
else:
    segundo = resultadoS

Nprim += str(segundo)

novoCPF += Nprim[9:11]

if novoCPF == CPF:
    print('Esse CPF é Válido!')
else:
    print('Esse CPF não é Válido!')
