# Calculadora simple
# Práctica de funciones y operaciones básicas

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"

# Pruebas
print("=== Calculadora Simple ===")
print(f"10 + 5 = {sumar(10, 5)}")
print(f"10 - 5 = {restar(10, 5)}")
print(f"10 * 5 = {multiplicar(10, 5)}")
print(f"10 / 5 = {dividir(10, 5)}")