
# ============================================
# BLOQUE 1: MÉTODOS DE CADENAS (STRINGS)
# ============================================

print("=" * 50)
print("EJERCICIO 1: Métodos básicos de strings")
print("=" * 50)
# Creá una variable con tu nombre completo en minúsculas
# Usá métodos para:
# - Convertirlo a mayúsculas
# - Convertirlo a título (primera letra de cada palabra en mayúscula)
# - Contar cuántas letras 'a' tiene

nombre_completo = "lopez reyna gabriela elizabeth"
print(f"Nombre en mayúsculas: {nombre_completo.upper()}")
print(f"Nombre con primera letra en mayúscula: {nombre_completo.title()}")
print(f"Cantidad de letras 'A': {nombre_completo.count('a')}")



print("\n" + "=" * 50)
print("EJERCICIO 2: Método strip() y replace()")
print("=" * 50)
# Tenés este string con espacios extras:
texto = "   Hola Mundo   "
# Eliminá espacios al inicio y final
# Replazá para cambiar "Mundo" por "Python"

print(f"Texto sin espacios extras: {texto.strip()}")
print(f"Texto reemplazado: {texto.replace('Mundo','Python')}")
print(f"Texto reemplazado y sin espacios extras: {(texto.strip().replace('Mundo','Python'))}")



print("\n" + "=" * 50)
print("EJERCICIO 3: Método split() y join()")
print("=" * 50)
# Tenés esta oración:
oracion = "Python es un lenguaje poderoso"
# Dividila en palabras usando split()
# Luego uní las palabras con guiones usando join()


print(f"Oración dividida: {oracion.split(' ')}")
print(type(oracion))
separador = "-"
print(f"Oración dividida: {(separador.join(oracion.split(' ')))}")



print("\n" + "=" * 50)
print("EJERCICIO 4: Métodos find() y endswith()")
print("=" * 50)
# Creá un email: email = "usuario@gmail.com"
# Encontrá la posición del @ 
# Verificá si el email termina con ".com" 

email = "lopezreynagabriela@gmail.com"

print(f"Posisión del @: {email.find('@')}")
print(f"Termina con .com: {email.endswith('.com')}")



print("\n" + "=" * 50)
print("EJERCICIO 5: Validación de string")
print("=" * 50)
# Creá una contraseña y verificá:
# - Si contiene solo letras y números 
# - Si tiene al menos 8 caracteres
# - Imprimí "Contraseña válida" o "Contraseña inválida"

clave = "clave455"

print(f"La clave contiene solo nros y letras: {clave.isalnum()}")

if len(clave) >= 8:
    print(f"La clave tiene al menos 8 caracteres?: Si la clave tiene {len(clave)} caracteres")
else:
    print(f"La clave tiene al menos 8 caracteres?: No la clave tiene {len(clave)} caracteres")

if clave == 'clave455':
    print(f"Contraseña válida")
else:
    print(f"Contraseña inválida")


# ============================================
# BLOQUE 2: MÉTODOS DE LISTAS
# ============================================

print("\n" + "=" * 50)
print("EJERCICIO 6: Métodos append() y extend()")
print("=" * 50)
# Creá una lista de frutas: ["manzana", "banana"]
# Agregá "naranja" 
# Agregá ["uva", "pera"] 
# Imprimí la lista final

frutas = ["manzana", "banana"]

frutas.append("naranja")
frutas.extend(["uva", "pera"])

print(f"Lista de frutas: {frutas}")


print("\n" + "=" * 50)
print("EJERCICIO 7: Métodos insert() y remove()")
print("=" * 50)
# Creá una lista de números: [1, 2, 4, 5]
# Insertá el 3 en la posición correcta 
# Remové el número 5 

numeros = [1, 2, 4, 5]
print(f"Lista de números inicial: {numeros}")

numeros.insert(2,3)
print(f"Lista de números agregado el 3: {numeros}")

numeros.remove(5)
print(f"Lista de números removiendo el 5: {numeros}")


print("\n" + "=" * 50)
print("EJERCICIO 8: Métodos sort() y reverse()")
print("=" * 50)
# Creá una lista desordenada: [5, 2, 8, 1, 9]
# Ordená la lista de menor a mayor 
# Invertila
# Imprimí el resultado

lista = [5, 2, 8, 1, 9]
print(f"Lista de números inicial: {lista}")

lista.sort()
print(f"Lista de números ordenada: {lista}")

lista.reverse()
print(f"Lista de números con orden invertido: {lista}")



print("\n" + "=" * 50)
print("EJERCICIO 9: Método pop() y clear()")
print("=" * 50)
# Creá una lista: ["primero", "segundo", "tercero"]
# Eliminá y guardá el último elemento 
# Limpiá toda la lista 

orden = ["primero", "segundo", "tercero"]
print(f"Lista de orden inicial: {orden}")

orden.pop(-1)
print(f"Lista de orden eliminando el último: {orden}")

orden.clear()
print(f"Lista de orden eliminando todos los elementos: {orden}")


print("\n" + "=" * 50)
print("EJERCICIO 10: Método count() e index()")
print("=" * 50)
# Creá una lista: [1, 2, 3, 2, 4, 2, 5]
# Contá cuántas veces aparece el 2 
# Encontrá la posición del primer 3 

lista_numeros = [1, 2, 3, 2, 4, 2, 5]
print(f"Lista de Números: {lista_numeros}")
print(f"Cuántas veces aparece el 2: {lista_numeros.count(2)}")
print(f"Posision del primer 3: {lista_numeros.index(3)}")


# ============================================
# BLOQUE 3: MÉTODOS DE DICCIONARIOS
# ============================================

print("\n" + "=" * 50)
print("EJERCICIO 11: Métodos keys(), values() e items()")
print("=" * 50)
# Creá un diccionario de un estudiante:
# nombre, edad, carrera
# Imprimí todas las claves 
# Imprimí todos los valores 
# Imprimí pares clave-valor

diccionario = { 
               "nombre": "Reyna Lopez",
               "edad": "32",
               "carrera": "Analista en Sistemas de Computación"
               }

print(f"Todas las keys: {diccionario.keys()}")
print(f"Todas los valores: {diccionario.values()}")
print(f"Todas las keys: {diccionario.items()}")



print("\n" + "=" * 50)
print("EJERCICIO 12: Método get() y setdefault()")
print("=" * 50)
# Creá un diccionario: {"producto": "laptop", "precio": 1000}
# Intentá obtener "stock" con get() 
# Agregá "stock" con valor 5 usando setdefault()

diccionario1 = {
                "producto": "laptop", 
                "precio": 1000
            }

print(f"Stock: {diccionario1.get('stock')}")

diccionario1.setdefault("stock", 5)
print(f"Stock agregado: {diccionario1.get('stock')}")
print(f"Diccionario: {diccionario1}")


print("\n" + "=" * 50)
print("EJERCICIO 13: Método update() y pop()")
print("=" * 50)
# Creá un diccionario de un producto
# Actualizá múltiples valores con update()
# Eliminá una clave con pop() y guardá su valor

diccionario2 = {
                "producto": "Jabón Facial", 
                "precio": 3000
            }

print(f"Diccionario inicial: {diccionario2}")

diccionario2.update({"producto": "Jabón Corporal"})
diccionario2.update({"precio": 3500})
print(f"Diccionario modificado: {diccionario2}")

diccionario2.pop("precio")
print(f"Diccionario eliminando el precio: {diccionario2}")



# ============================================
# BLOQUE 4: ENTRADA DE DATOS (INPUTS)
# ============================================

print("\n" + "=" * 50)
print("EJERCICIO 14: Input básico")
print("=" * 50)
# Pedí el nombre del usuario con input()
# Pedí su edad (convertila a entero)
# Imprimí: "Hola [nombre], tenés [edad] años"

nombre_usuario = input("Ingrese su nombre de usuario: ")
edad = input("Ingrese su edad: ")

print(f"Hola {nombre_usuario} tienes {int(edad)} años")


print("\n" + "=" * 50)
print("EJERCICIO 15: Calculadora simple con inputs")
print("=" * 50)
# Pedí dos números al usuario
# Pedí qué operación quiere hacer (+, -, *, /)
# Mostrá el resultado

num1 = input("Ingrese numero 1: ")
num2 = input("Ingrese numero 2: ")

operacion = input("Ingrese qué operación quiere hacer (+, -, *, /): ")

if operacion == "+":
    print(f"Resultado: {float(num1) + float(num2)}")
elif operacion == "-":
    print(f"Resultado: {float(num1) - float(num2)}")
elif operacion == "*":
    print(f"Resultado: {float(num1) * float(num2)}")
elif operacion == "/":
    if float(num1) >= 1 and float(num2) >= 1:
        print(f"Resultado: {float(num1) / float(num2)}")
    elif float(num1) == 0 or float(num2) == 0:
        print("No se puede dividir por 0")
    

print("\n" + "=" * 50)
print("EJERCICIO 16: Validación de input")
print("=" * 50)
# Pedí un número del 1 al 10
# Si no está en ese rango, mostrá un mensaje de error
# Si está en el rango, mostrá "Número válido"

num3 = input("Ingrese un número del 1 al 10: ")

if int(num3) in range(1,11):
    print("Número válido.")
else:
    print("El número ingresado esta fuera del rango. ")
    

# ============================================
# BLOQUE 5: BUCLE FOR
# ============================================

print("\n" + "=" * 50)
print("EJERCICIO 17: For con listas")
print("=" * 50)
# Creá una lista de colores
# Recorrela con for e imprimí: "Me gusta el color [color]"

colores = ["azul", "verde", "rojo", "blanco", "negro"]

for color in colores:
    if color == "rojo":
        print(f"Me gusta el color {color}")
    


print("\n" + "=" * 50)
print("EJERCICIO 18: For con range()")
print("=" * 50)
# Imprimí los números del 1 al 10 usando for y range()
# Después imprimí solo los números pares del 0 al 20

print(f"Numeros del 1 al 10:")
for num in range(1, 11):
    print(f"Nro: {num}")
    
    
print(f"-" * 50)

print(f"Numeros Pares:")
for num in range(1, 21):
    if num % 2 == 0:
        print(num)


print("\n" + "=" * 50)
print("EJERCICIO 19: For con enumerate()")
print("=" * 50)
# Creá una lista de tareas: ["estudiar", "ejercicio", "cocinar"]
# Recorrela con enumerate() mostrando:
# "Tarea 1: estudiar"
# "Tarea 2: ejercicio"
# etc.

tareas = ["estudiar", "ejercicio", "cocinar"]
key = 1

for tarea in enumerate(tareas):
    value = tarea[1]
    print(f"Tarea {key}: {value}")
    key +=1



print("\n" + "=" * 50)
print("EJERCICIO 20: For con diccionarios")
print("=" * 50)
# Creá un diccionario de precios: {"manzana": 50, "banana": 30}
# Recorrelo mostrando: "La manzana cuesta $50"

dicc_precios = {
        "manzana": 50, 
        "banana": 30
        }

for fruta, precio in dicc_precios.items():
    if fruta == "manzana":
        print(f"La {fruta} cuesta ${precio}")
    


print("\n" + "=" * 50)
print("EJERCICIO 21: For anidado (nested)")
print("=" * 50)
# Imprimí una tabla de multiplicar del 1 al 5
# Formato: 1 x 1 = 1, 1 x 2 = 2, etc.

num1 = 1

for multi in range(1,11):
    print(f"\n")
    print(f"Tabla del {multi}:")
    print(f"------------------") 
    for num1 in range(1,6) :
        print(f"{multi} x {num1} = {multi * num1}")
        


# ============================================
# BLOQUE 6: BUCLE WHILE
# ============================================

print("\n" + "=" * 50)
print("EJERCICIO 22: While básico")
print("=" * 50)
# Contá del 1 al 10 usando while
# Imprimí cada número

numero = 1
print("Numeros del 1 al 10:")
while numero <= 10:
    print(numero)
    numero += 1




print("\n" + "=" * 50)
print("EJERCICIO 23: While con condición")
print("=" * 50)
# Empezá con un número (ej: 100)
# Dividilo por 2 en cada iteración mientras sea mayor a 1
# Imprimí cada resultado

numero = 100 

while numero > 1:
    print(f"{numero} / 2 = {numero / 2}")
    numero = numero / 2


print("\n" + "=" * 50)
print("EJERCICIO 24: While con break")
print("=" * 50)
# Pedí números al usuario en un bucle infinito
# Si ingresa 0, salí del bucle con break
# Calculá y mostrá la suma de todos los números ingresados


numero_in = input("Ingrese un nro: ")
suma = 0

while int(numero_in) != "0":
    suma = suma + int(numero_in)
    numero_in = input("Ingrese un nro: ")
    if int(numero_in) == 0:
        print(f"La suma de todos los nros es: {suma}")
        break



print("\n" + "=" * 50)
print("EJERCICIO 25: Juego de adivinanza")
print("=" * 50)
# Creá un número secreto (ej: 7)
# Pedí al usuario que adivine
# Usá while para seguir pidiendo hasta que acierte
# Dale pistas: "muy alto" o "muy bajo"

num_sec = 5

numero_ent = input("Ingresa un numero: ")

while int(numero_ent) != num_sec:
    if int(numero_ent) < num_sec:
        print("Muy bajo")
        numero_ent = input("Ingresa otro numero: ")
    if int(numero_ent) > num_sec:
        print("Muy alto")
        numero_ent = input("Ingresa otro numero: ")
    if int(numero_ent) == num_sec:
        print("Felicidades es el numero correcto !")