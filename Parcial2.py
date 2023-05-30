import random
import matplotlib.pyplot as plt

# Lista de los equipos

equipos = ["Aguilas Doradas", "Millonarios", "America", "Boyaca chico", "Alianza petrolera", "Atletico nacional", "Junior", "Santa Fe", "Pasto", "Medellin", "La equidad", "Envigado", "Tolima", "Jaguares", "Deportivo pereira", "Atletico huila", "Deportivo Cali",  "Union Magdalena", "Bucaramanga", "Once caldas"]

equipos_local = []
equipos_visitante = []
goles_local = []
goles_visitante = []

for equipo in equipos:
    for j in range(2):
        equipos_local.append(equipo)
        equipos_visitante.append(random.choice(equipos))
        goles_local.append(random.randint(0, 5))
        goles_visitante.append(random.randint(0, 5))

# Cálculo de estadísticas

partidos = {}
partidos_ganados = {}
partidos_perdidos = {}
partidos_empatados = {}
goles_locales = {}
goles_visitantes = {}

for equipo in equipos:
    partidos[equipo] = 0
    partidos_ganados[equipo] = 0
    partidos_perdidos[equipo] = 0
    partidos_empatados[equipo] = 0
    goles_locales[equipo] = 0
    goles_visitantes[equipo] = 0

for i in range(len(equipos_local)):
    equipo_local = equipos_local[i]
    equipo_visitante = equipos_visitante[i]
    goles_local_equipo = goles_local[i]
    goles_visitante_equipo = goles_visitante[i]

    partidos[equipo_local] += 1
    partidos[equipo_visitante] += 1

    goles_locales[equipo_local] += goles_local_equipo
    goles_visitantes[equipo_visitante] += goles_visitante_equipo

    if goles_local_equipo > goles_visitante_equipo:
        partidos_ganados[equipo_local] += 1
        partidos_perdidos[equipo_visitante] += 1
    elif goles_local_equipo < goles_visitante_equipo:
        partidos_perdidos[equipo_local] += 1
        partidos_ganados[equipo_visitante] += 1
    else:
        partidos_empatados[equipo_local] += 1
        partidos_empatados[equipo_visitante] += 1

total_goles = sum(goles_local) + sum(goles_visitante)

# Graficar todas las variables con las listas

plt.bar(range(len(goles_locales)), list(goles_locales.values()), align='center')
plt.xticks(range(len(goles_locales)), list(goles_locales.keys()), rotation=90)
plt.ylabel('Goles')
plt.title('Cantidad de goles de equipos locales')
plt.show()

plt.bar(range(len(goles_visitantes)), list(goles_visitantes.values()), align='center')
plt.xticks(range(len(goles_visitantes)), list(goles_visitantes.keys()), rotation=90)
plt.ylabel('Goles')
plt.title('Cantidad de goles de equipos visitantes')
plt.show()

plt.bar(range(len(partidos_ganados)), list(partidos_ganados.values()), align='center')
plt.xticks(range(len(partidos_ganados)), list(partidos_ganados.keys()), rotation=90)
plt.ylabel('Partidos ganados')
plt.title('Cantidad de partidos ganados')
plt.show()

plt.bar(range(len(partidos_perdidos)), list(partidos_perdidos.values()), align='center')
plt.xticks(range(len(partidos_perdidos)), list(partidos_perdidos.keys()), rotation=90)
plt.ylabel('Partidos perdidos')
plt.title('Cantidad de partidos perdidos')
plt.show()

plt.bar(range(len(partidos_empatados)), list(partidos_empatados.values()), align='center')
plt.xticks(range(len(partidos_empatados)), list(partidos_empatados.keys()), rotation=90)
plt.ylabel('Partidos empatados')
plt.title('Cantidad de partidos empatados')
plt.show()

plt.bar(range(len(partidos)), list(partidos.values()), align='center')
plt.xticks(range(len(partidos)), list(partidos.keys()), rotation=90)
plt.ylabel('Partidos jugados')
plt.title('Cantidad de partidos jugados')
plt.show()