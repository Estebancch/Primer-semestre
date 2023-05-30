# Inicializar variables para contar la cantidad de personas mayores de edad y la suma de sus edades
cantidad_mayores_edad = 0
suma_edades_mayores_edad = 0

# Ciclo que pregunta la edad de 5 personas
for i in range(5):
    edad = int(input("Ingrese la edad de la persona #" + str(i+1) + ": "))
    if edad >= 18:  # Comprobar si la edad es mayor o igual a 18
        cantidad_mayores_edad += 1
        suma_edades_mayores_edad += edad

# Calcular el promedio de edad de las personas mayores de edad
if cantidad_mayores_edad > 0:
    promedio_edad_mayores_edad = suma_edades_mayores_edad / cantidad_mayores_edad
else:
    promedio_edad_mayores_edad = 0

# Imprimir los resultados
print("Cantidad de personas mayores de edad:", cantidad_mayores_edad)
print("Promedio de edad de personas mayores de edad:", promedio_edad_mayores_edad)
