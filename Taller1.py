import random
 
# 1. Definición del alfabeto
alfabeto = set()
alfabeto.update(input("Símbolos del alfabeto (ejemplo: ab o mas): "))
print("Alfabeto (Σ) =", alfabeto)   
 
# 2. Generación de cadenas
n = int(input("¿Cuántas cadenas deseas generar?: "))
for i in range(n):
    cadena = "".join(random.choice(list(alfabeto)) for _ in range(random.randint(1, 5)))
    print(f"Cadena aleatoria: {cadena}")
    print(f"Longitud: {len(cadena)}")
 
# 3. Definición del lenguaje
entrada = input("Cadenas del lenguaje separadas por coma (ej: a,ab,bb,aba): ")
lenguaje = set(c.strip() for c in entrada.split(","))
print("Definición del lenguaje =", lenguaje)
 
# 4. Verificación de pertenencia
while True:
    cadena = input("Cadena que deseas verificar o escribe ('salir') para terminar: ")
    if cadena == "salir":
        break
    print(f"¿'{cadena}' pertenece al lenguaje? -> {cadena in lenguaje}")