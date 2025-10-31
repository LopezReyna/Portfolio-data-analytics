# Mi primer script de Python
# Autor: Reyna Lopez
# Fecha: 31 de Octubre 2025

def saludar(nombre):
    """
    Función que saluda a una persona
    """
    mensaje = "¡Hola! Bienvenido a mi portfolio de análisis de datos."
    return mensaje

# Programa principal
if __name__ == "__main__":
    print("=== Mi Primer Programa en Python ===")
    
    mi_nombre = "Reyna"
    saludo = saludar(mi_nombre)
    print(saludo)
    
    # Pequeño ejercicio con listas
    tecnologias = ["Python", "SQL", "Power BI", "Git"]
    print("\nTecnologías que estoy aprendiendo:")
    for i, tech in enumerate(tecnologias, 1):
        print(f"{i}. {tech}")
    
    print("\n¡Vamos por más! 🚀")

print("¡Seguimos aprendiendo! 📊")

