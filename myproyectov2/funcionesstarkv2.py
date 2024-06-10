from stark_heroes import lista_personajes

# Convertir alturas y pesos a floats
for personaje in lista_personajes:
    personaje['altura'] = float(personaje['altura'])
    personaje['peso'] = float(personaje['peso'])

# Funciones que emulan el comportamiento de min, max y sum
def mi_min(lista, clave):
    minimo = lista[0]
    for item in lista:
        if item[clave] < minimo[clave]:
            minimo = item
    return minimo

def mi_max(lista, clave):
    maximo = lista[0]
    for item in lista:
        if item[clave] > maximo[clave]:
            maximo = item
    return maximo

def mi_sum(lista):
    total = 0
    for item in lista:
        total += item
    return total

def imprimir_nombres_genero(genero):
    for personaje in lista_personajes:
        if personaje["genero"] == genero:
            print(personaje["nombre"])

def obtener_superheroe_mas_alto(genero):
    return mi_max([p for p in lista_personajes if p["genero"] == genero], "altura")

def obtener_superheroe_mas_bajo(genero):
    return mi_min([p for p in lista_personajes if p["genero"] == genero], "altura")

def calcular_altura_promedio(genero):
    alturas = [p["altura"] for p in lista_personajes if p["genero"] == genero]
    return mi_sum(alturas) / len(alturas)

def contar_atributo(atributo):
    conteo = {}
    for personaje in lista_personajes:
        valor = personaje[atributo] if personaje[atributo] else "No Tiene"
        if valor not in conteo:
            conteo[valor] = 0
        conteo[valor] += 1
    return conteo

def listar_superheroes_por_atributo(atributo):
    agrupados = {}
    for personaje in lista_personajes:
        valor = personaje[atributo] if personaje[atributo] else "No Tiene"
        if valor not in agrupados:
            agrupados[valor] = []
        agrupados[valor].append(personaje["nombre"])
    return agrupados

def menu():
    while True:
        print("\nMenú de Opciones:")
        print("A. Imprimir nombres de superhéroes de género M")
        print("B. Imprimir nombres de superhéroes de género F")
        print("C. Superhéroe más alto de género M")
        print("D. Superhéroe más alto de género F")
        print("E. Superhéroe más bajo de género M")
        print("F. Superhéroe más bajo de género F")
        print("G. Altura promedio de superhéroes de género M")
        print("H. Altura promedio de superhéroes de género F")
        print("I. Informar nombres de superhéroes asociados a los indicadores anteriores (C a F)")
        print("J. Contar superhéroes por color de ojos")
        print("K. Contar superhéroes por color de pelo")
        print("L. Contar superhéroes por tipo de inteligencia")
        print("M. Listar superhéroes agrupados por color de ojos")
        print("N. Listar superhéroes agrupados por color de pelo")
        print("O. Listar superhéroes agrupados por tipo de inteligencia")
        print("Q. Salir")
        
        opcion = input("Seleccione una opción: ").upper()

        if opcion == "A":
            imprimir_nombres_genero("M")
        elif opcion == "B":
            imprimir_nombres_genero("F")
        elif opcion == "C":
            heroe_mas_alto_m = obtener_superheroe_mas_alto("M")
            print(f"Superhéroe más alto de género M: {heroe_mas_alto_m['nombre']} ({heroe_mas_alto_m['altura']} cm)")
        elif opcion == "D":
            heroe_mas_alto_f = obtener_superheroe_mas_alto("F")
            print(f"Superhéroe más alto de género F: {heroe_mas_alto_f['nombre']} ({heroe_mas_alto_f['altura']} cm)")
        elif opcion == "E":
            heroe_mas_bajo_m = obtener_superheroe_mas_bajo("M")
            print(f"Superhéroe más bajo de género M: {heroe_mas_bajo_m['nombre']} ({heroe_mas_bajo_m['altura']} cm)")
        elif opcion == "F":
            heroe_mas_bajo_f = obtener_superheroe_mas_bajo("F")
            print(f"Superhéroe más bajo de género F: {heroe_mas_bajo_f['nombre']} ({heroe_mas_bajo_f['altura']} cm)")
        elif opcion == "G":
            altura_promedio_m = calcular_altura_promedio("M")
            print(f"Altura promedio de superhéroes de género M: {altura_promedio_m} cm")
        elif opcion == "H":
            altura_promedio_f = calcular_altura_promedio("F")
            print(f"Altura promedio de superhéroes de género F: {altura_promedio_f} cm")
        elif opcion == "I":
            heroe_mas_alto_m = obtener_superheroe_mas_alto("M")
            heroe_mas_alto_f = obtener_superheroe_mas_alto("F")
            heroe_mas_bajo_m = obtener_superheroe_mas_bajo("M")
            heroe_mas_bajo_f = obtener_superheroe_mas_bajo("F")
            print(f"Superhéroe más alto de género M: {heroe_mas_alto_m['nombre']}")
            print(f"Superhéroe más alto de género F: {heroe_mas_alto_f['nombre']}")
            print(f"Superhéroe más bajo de género M: {heroe_mas_bajo_m['nombre']}")
            print(f"Superhéroe más bajo de género F: {heroe_mas_bajo_f['nombre']}")
        elif opcion == "J":
            conteo_ojos = contar_atributo("color_ojos")
            print("Superhéroes por color de ojos:", conteo_ojos)
        elif opcion == "K":
            conteo_pelo = contar_atributo("color_pelo")
            print("Superhéroes por color de pelo:", conteo_pelo)
        elif opcion == "L":
            conteo_inteligencia = contar_atributo("inteligencia")
            print("Superhéroes por tipo de inteligencia:", conteo_inteligencia)
        elif opcion == "M":
            agrupados_ojos = listar_superheroes_por_atributo("color_ojos")
            print("Superhéroes agrupados por color de ojos:", agrupados_ojos)
        elif opcion == "N":
            agrupados_pelo = listar_superheroes_por_atributo("color_pelo")
            print("Superhéroes agrupados por color de pelo:", agrupados_pelo)
        elif opcion == "O":
            agrupados_inteligencia = listar_superheroes_por_atributo("inteligencia")
            print("Superhéroes agrupados por tipo de inteligencia:", agrupados_inteligencia)
        elif opcion == "Q":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    menu()
