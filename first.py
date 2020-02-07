
# Exercício 4 - usando modulo


import math 

def mathFactorial(x):
    
    x = math.factorial(n)
    return x
    
n = int(input())
print(mathFactorial(n))


# Exercício 4 - forma alternativa


n = int(input('n:'))
anterior = []
x = 0
# enquanto n for maior que zero, subtrai um do valor original 
# e coloca em uma posição do vetor de números anteriores
while n > 0:
    x = n 
    anterior.append(x)
    n = n - 1 
x = 1
for i in anterior:
    x = x * i
print(x)



# Exercício 4 - Correção 

def factorial(n):
    fat = 1 
    for i in range(1, n+1):
        fat = fat * i
    return fat

n = int(input('Informe o numero :'))
print(factorial(n))