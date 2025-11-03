
# ============================================
# BLOQUE 1: TIPOS DE DATOS SIMPLES Y VARIABLES
# ============================================

print("=" * 50)
print("EJERCICIO 1: Tipos de datos")
print("=" * 50)
# Creá 4 variables con estos tipos de datos:
# - Un string con tu nombre
# - Un entero con tu edad
# - Un float con tu altura en metros
# - Un booleano que indique si te gusta programar

nomb = 'Reyna Lopez'
edad = 32
altura = 1.65
programar = True

#print(f"Nombre:, {nomb} \nEdad: {edad} \nAltura: {altura} \nLe gusta programar?: {programar}" )

print("\n" + "=" * 50)
print("EJERCICIO 2: Verificar tipos")
print("=" * 50)
# Usando las variables del ejercicio 1, imprimí el tipo de cada una
# usando la función type()

print(f"Tipo de variable Nombre: ", type(nomb))
print(f"Tipo de variable Edad: ", type(edad))
print(f"Tipo de variable Altura: ", type(altura))
print(f"Tipo de variable Programar: ", type(programar))


# ============================================
# BLOQUE 2: CONCATENACIÓN
# ============================================

print("\n" + "=" * 50)
print("EJERCICIO 3: Concatenación básica")
print("=" * 50)
# Creá dos variables: nombre y apellido
# Concatenalas para formar el nombre completo y mostralo

nombre = "Reyna Gabriela Elizabeth"
apellido = "Lopez"

nombre_completo = apellido + ', ' + nombre

print(nombre_completo)


print("\n" + "=" * 50)
print("EJERCICIO 4: Concatenación con números")
print("=" * 50)
# Creá una variable con tu edad (número)
# Imprimí: "Tengo X años" usando concatenación
# Convertí el número a string con str()

edad = 32
print("Tengo " + str(edad) + " años")


print("\n" + "=" * 50)
print("EJERCICIO 5: F-strings")
print("=" * 50)
# Creá variables: producto, precio, cantidad
# Imprimí: "El producto X cuesta $Y y tenemos Z unidades"
# Usá f-strings (formato moderno)

producto = "Blend Dulce Campo"
precio = 8000
cantidad = 10

print(f"El producto {producto} cuesta ${precio} y tenemos {cantidad} unidades.")


# ============================================
# BLOQUE 3: OPERADORES DE PERTENENCIA
# ============================================

print("\n" + "=" * 50)
print("EJERCICIO 6: Operador 'in' con strings")
print("=" * 50)
# Creá una variable con una frase larga
# Verificá si la palabra "Python" está en la frase

frase = "Estoy aprendiendo a programar en Python"

print("Python" in frase)


print("\n" + "=" * 50)
print("EJERCICIO 7: Operador 'not in'")
print("=" * 50)
# Creá una lista de frutas: ["manzana", "banana", "naranja"]
# Verificá si "uva" NO está en la lista

frutas = ["manzana", "banana", "naranja", "pera"]

print("uva" not in frutas)


# ============================================
# BLOQUE 4: TIPOS DE DATOS COMPUESTOS
# ============================================

print("\n" + "=" * 50)
print("EJERCICIO 8: Trabajar con listas")
print("=" * 50)
# Creá una lista con 4 tecnologías que estás aprendiendo
# Imprimí la primera y la última tecnología
# Agregá una nueva tecnología al final

tecnologia = ["Python", "SQL Server", "Power BI", "GitHub"]

print(f"Primera: {tecnologia[0]}")
print(f"Ultima: {tecnologia[-1]}")

tecnologia.append("Excel")

print(tecnologia)


print("\n" + "=" * 50)
print("EJERCICIO 9: Trabajar con tuplas")
print("=" * 50)
# Creá una tupla con coordenadas (latitud, longitud) de tu ciudad
# Intentá acceder a cada valor por separado

coordenadas = (-31.429201954555616, -64.19761491731043)

print(f"Altitud: {coordenadas[0]}")
print(f"Longitud: {coordenadas[1]}")


print("\n" + "=" * 50)
print("EJERCICIO 10: Trabajar con diccionarios")
print("=" * 50)
# Creá un diccionario con información de un producto:
# nombre, precio, stock, categoria
# Imprimí solo el precio del producto

producto = {
    'nombre': "Blend Dulce Campo",
    'precio': 8000,
    'stock': 10,
    'categoria': "Blends"
}

print(f"Precio: ${producto['precio']}")


# ============================================
# BLOQUE 5: OPERADORES ARITMÉTICOS
# ============================================

print("\n" + "=" * 50)
print("EJERCICIO 11: Calculadora básica")
print("=" * 50)
# Creá dos variables: num1 = 15, num2 = 4
# Realizá e imprimí: suma, resta, multiplicación, división, 
# división entera (//), módulo (%), potencia (**)

num1 = 15
num2 = 4

suma = num1 + num2

resta = num1 - num2

multi = num1 * num2

division = num1 / num2

division_entera = num1 // num2

modulo = num1 % num2

potencia = num1 ** num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multi}")
print(f"Division: {division}")
print(f"Division Entera: {division_entera}")
print(f"Modulo o Resto: {modulo}")
print(f"Potencia: {potencia}")



print("\n" + "=" * 50)
print("EJERCICIO 12: Cálculo de precio final")
print("=" * 50)
# Un producto cuesta $1000 y tiene 15% de descuento
# Calculá el precio final después del descuento

producto = 1000
descuento = producto * 0.15

precio_final = producto - descuento

print(f"Precio final del Producto: {precio_final}")


# ============================================
# BLOQUE 6: OPERADORES DE COMPARACIÓN
# ============================================

print("\n" + "=" * 50)
print("EJERCICIO 13: Comparaciones simples")
print("=" * 50)
# Creá dos variables: edad1 = 25, edad2 = 30
# Compará si edad1 es mayor, menor, igual, diferente que edad2
# Imprimí el resultado de cada comparación

edad1 = 25
edad2 = 30

print(f"Es Mayor edad1 que edad2?: {edad1 > edad2}")
print(f"Es Menor edad1 que edad2?: {edad1 < edad2}")
print(f"Es Igual edad1 que edad2?: {edad1 == edad2}") 
print(f"Es Distinto edad1 que edad2?: {edad1 != edad2}") 


print("\n" + "=" * 50)
print("EJERCICIO 14: Comparación de strings")
print("=" * 50)
# Compará si "python" == "Python" (case sensitive)
# Luego compará usando .lower() para ignorar mayúsculas

cadena1 = "python"
cadena2 = "Python"

print(f"Son iguales?: {cadena1 == cadena2}")
print(f"Son iguales con .lower()?: {cadena1 == cadena2.lower()}")


# ============================================
# BLOQUE 7: CONDICIONALES
# ============================================

print("\n" + "=" * 50)
print("EJERCICIO 15: If básico")
print("=" * 50)
# Creá una variable edad
# Si la edad es mayor o igual a 18, imprimí "Eres mayor de edad"
# Si no, imprimí "Eres menor de edad"

edad = 18 

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


print("\n" + "=" * 50)
print("EJERCICIO 16: If-elif-else")
print("=" * 50)
# Creá una variable nota (0-10)
# Si nota >= 9: "Excelente"
# Si nota >= 7: "Muy bien"
# Si nota >= 5: "Aprobado"
# Si no: "Reprobado"

nota = 8

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Muy bien")
elif nota >= 5:
    print("Aprobado")
else:
    print("Reprobado")
    

print("\n" + "=" * 50)
print("EJERCICIO 17: Condicional con operadores de pertenencia")
print("=" * 50)
# Creá una lista de usuarios permitidos
# Pedí un nombre de usuario (o creá una variable)
# Verificá si está en la lista y mostrá mensaje apropiado

usuarios_permitidos = ["Pepito", "Juan Pedro", "Jose"]
#usuario_ingresado = input("Usuario:")
usuario_ingresado = "Pepito"

if usuario_ingresado in usuarios_permitidos:
    print("Iniciando Sesion...")
else:
    print("El usuario ingresado no tiene permisos para iniciar sesion.")

# ============================================
# BLOQUE 8: OPERADORES LÓGICOS
# ============================================

print("\n" + "=" * 50)
print("EJERCICIO 18: Operador AND")
print("=" * 50)
# Creá variables: edad = 25, tiene_licencia = True
# Una persona puede conducir si tiene 18+ años Y tiene licencia
# Verificá e imprimí si puede conducir

edad = 15
tiene_licencia = False

if edad >= 18 and tiene_licencia == True:
    print("Tiene permitido conducir.")
elif edad >= 18 and tiene_licencia == False:
    print("No puede conducir, no tiene licencia.")
elif edad <= 17:
    print("No puede conducir, es menor de edad.")



print("\n" + "=" * 50)
print("EJERCICIO 19: Operador OR")
print("=" * 50)
# Un descuento se aplica si:
# - El cliente es miembro VIP O
# - La compra es mayor a $5000
# Creá las variables y verificá si aplica descuento

cliente_vip = True
ultima_compra = 5000.0 #float(input("Ingrese el monto de compra:"))
descuento = 0.15
precio_final = 0

#cliente['ultima_compra'] = input("Ingrese el monto de compra:")

if cliente_vip == True or ultima_compra >= 5000:
    precio_final = ultima_compra - (ultima_compra * descuento) 
    print(f"Por ser Cliente VIP o tener una compra mayor a $5000 se le realiza un descuento del 15%. \nPrecio Final: {precio_final}")
elif cliente_vip == False or ultima_compra <= 5000:
    precio_final = ultima_compra
    print(f"No se aplican descuentos. \nPrecio Final: {precio_final}")

                    
                    
print("\n" + "=" * 50)
print("EJERCICIO 20: Combinación de operadores lógicos")
print("=" * 50)
# Sistema de acceso a una app:
# Puede acceder si:
# (tiene_cuenta AND contraseña_correcta) OR es_admin
# Creá las variables y verificá el acceso

tiene_cuenta = False
contraseña_correcta = True
es_admin = True

if (tiene_cuenta and contraseña_correcta) or es_admin:
    print("Iniciando sesion...")
else:
    print("No puede iniciar sesion.")
