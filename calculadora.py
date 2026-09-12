# Calculadora

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return a ** 0.5

print('Mensaje para probar el git stash')