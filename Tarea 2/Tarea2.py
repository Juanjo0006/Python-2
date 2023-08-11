import requests
import matplotlib.pyplot as plt
from tabulate import tabulate
from datetime import datetime, timedelta
import pandas as pd

# URL base de la API del USGS Earthquake Catalog
base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

# ... (Código para obtener los datos de los terremotos y contar por continente) ...

# Parámetros de la consulta para el año 2023
params = {
    "format": "geojson",
    "starttime": "2023-01-01T00:00:00",
    "endtime": "2023-12-31T23:59:59",
    "minmagnitude": 5
}

# Hacer la solicitud a la API del USGS Earthquake Catalog
response = requests.get(base_url, params=params)
data = response.json()

# Crear un diccionario para contabilizar los eventos por continente
continent_counts = {
    "Africa": 0,
    "Asia": 0,
    "Europe": 0,
    "North America": 0,
    "Oceania": 0,
    "South America": 0
}

# Definir las coordenadas aproximadas de los continentes
continent_boundaries = {
    "Africa": [20, -20, 60, -40],
    "Asia": [90, 10, 180, -10],
    "Europe": [40, 70, 60, 35],
    "North America": [-40, 90, 85, -170],
    "Oceania": [-10, 160, -40, 100],
    "South America": [-40, -90, 10, -70]
}

# Ciclo para contar los eventos por continente
for quake in data['features']:
    event_location = quake['geometry']['coordinates']

    for continent, boundary in continent_boundaries.items():
        if boundary[0] >= event_location[1] >= boundary[1] and boundary[2] >= event_location[0] >= boundary[3]:
            continent_counts[continent] += 1
            break

# Función para imprimir la tabla y gráfico de eventos por continente
def imprimir_tabla_y_grafico_continente():
    # Crear la tabla con el número de eventos por continente
    table = []
    for continent, count in continent_counts.items():
        table.append([continent, count])

    # Imprimir la tabla con el número de eventos por continente
    print("Tabla de Eventos por Continente:")
    print(tabulate(table, headers=["Continente", "Número de Eventos"], tablefmt="grid"))

    # Crear el gráfico de barras
    continents = list(continent_counts.keys())
    event_counts = list(continent_counts.values())

    plt.bar(continents, event_counts)
    plt.xlabel("Continente")
    plt.ylabel("Número de Eventos")
    plt.title("Número de Eventos de Terremotos por Continente en 2023")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Mostrar la tabla y el gráfico
    plt.show()

# Función para imprimir gráfico de los cinco terremotos más fuertes
def imprimir_grafico_terremotos_fuertes():
    # Obtener los detalles de los últimos cinco terremotos más fuertes
    strongest_quakes = []
    for quake in data['features'][-5:]:
        event_id = quake['id']
        event_magnitude = quake['properties']['mag']
        strongest_quakes.append((event_id, event_magnitude))

    # Crear el gráfico de barras
    quake_ids = [quake[0] for quake in strongest_quakes]
    quake_magnitudes = [quake[1] for quake in strongest_quakes]

    plt.barh(quake_ids, quake_magnitudes)  # Utilizamos barh para un gráfico horizontal
    plt.xlabel("Magnitud")
    plt.ylabel("ID del Terremoto")
    plt.title("Últimos Cinco Terremotos Más Fuertes en 2023")
    plt.tight_layout()

    # Mostrar el gráfico de los últimos cinco terremotos más fuertes
    plt.show()


# Obtener eventos por mes para el año actual (enero a julio)
def imprimir_grafico_lineas_enero_a_julio():
    current_year = datetime.now().year
    current_month = datetime.now().month
    months = list(range(1, 13))  # Cambiamos el rango a todos los meses (enero a diciembre)
    event_counts_by_month = [0] * 12  # Creamos una lista para todos los meses

    for quake in data['features']:
        event_date = datetime.fromtimestamp(quake['properties']['time'] / 1000)
        if event_date.year == current_year and 1 <= event_date.month <= 12:  # Comprobamos para todos los meses
            event_counts_by_month[event_date.month - 1] += 1

    month_names = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]  # Agregamos los nombres de los meses restantes

    plt.plot(months, event_counts_by_month, marker='o')
    plt.xlabel("Mes")
    plt.ylabel("Número de Eventos")
    plt.title("Eventos de Terremotos por Mes en " + str(current_year))
    plt.xticks(months, month_names)
    plt.tight_layout()
    plt.show()

# Función para salir del programa
def salir():
    print("Saliendo del programa.")
    exit()

# Menú de opciones
menu = {
    1: ("Impresión de tabla y gráfico de continentes", imprimir_tabla_y_grafico_continente),
    2: ("Imprimir gráfico de 5 terremotos más fuertes", imprimir_grafico_terremotos_fuertes),
    3: ("Imprimir gráfico eventos 2023", imprimir_grafico_lineas_enero_a_julio),
    4: ("Salir", salir)
}

while True:
    print("Menú:")
    for option, (description, _) in menu.items():
        print(f"{option}. {description}")

    choice = int(input("Seleccione una opción: "))

    if choice in menu:
        _, function = menu[choice]
        function()
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")
