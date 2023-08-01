# Link principal: https://eonet.gsfc.nasa.gov/docs/v2.1  o https://api.nasa.gov/?ref=apispublicas.com


#link events: https://eonet.gsfc.nasa.gov/api/v2.1/events
#link categories: https://eonet.gsfc.nasa.gov/api/v2.1/categories
#link layers: https://eonet.gsfc.nasa.gov/api/v2.1/layers

#En el siguiente código se imprime un menú para escoger una de tres funiones relacionadas a una API remota de la NASA. 

import requests as req
import random

##Imprimir en pantalla todas las categorías disponibles de la API

def get_all_categories():
    url = "https://eonet.gsfc.nasa.gov/api/v2.1/categories"
    response = req.get(url)

    if response.status_code == 200:
        categories = response.json()['categories']
        return categories
    else:
        print("Error al obtener las categorías.")
        return []

 
##Imprimir un evento random de la lista junto con su categoría 

def get_all_categories():
    url = "https://eonet.gsfc.nasa.gov/api/v2.1/categories"
    response = req.get(url)

    if response.status_code == 200:
        categories = response.json()['categories']
        return categories
    else:
        print("Error al obtener las categorías.")
        return []

def get_all_events():
    url = "https://eonet.gsfc.nasa.gov/api/v2.1/events"
    response = req.get(url)

    if response.status_code == 200:
        events = response.json()['events']
        return events
    else:
        print("Error al obtener los eventos.")
        return []

def print_random_event_with_category():
    all_events = get_all_events()
    all_categories = get_all_categories()

    if all_events and all_categories:
        if len(all_events) > 0:
            random_event = random.choice(all_events)
            event_title = random_event['title']
            event_categories = random_event['categories']
            event_category_titles = []

            for category_id in event_categories:
                for category in all_categories:
                    if category['id'] == category_id:
                        event_category_titles.append(category['title'])
                        break

            print("Evento de la NASA:")
            print("Título: ", event_title)
            print("Categorías: ", ", ".join(event_category_titles))
        else:
            print("No se encontraron eventos en la API.")
    else:
        print("No se pudieron obtener los eventos o las categorías.")


##Imprime el número de eventos de una categoría en el año 2023

def get_categories_with_event_count(year):
    url = f"https://eonet.gsfc.nasa.gov/api/v2.1/events?year={year}"
    response = req.get(url)

    if response.status_code == 200:
        events = response.json()['events']
        categories_with_count = {}

        for event in events:
            event_categories = event['categories']
            for category in event_categories:
                category_id = category['id']
                if category_id not in categories_with_count:
                    categories_with_count[category_id] = 1
                else:
                    categories_with_count[category_id] += 1

        return categories_with_count
    else:
        print("Error al obtener los eventos.")
        return {}

def get_all_categories():
    url = "https://eonet.gsfc.nasa.gov/api/v2.1/categories"
    response = req.get(url)

    if response.status_code == 200:
        categories = response.json()['categories']
        return categories
    else:
        print("Error al obtener las categorías.")
        return []

def print_categories_with_event_count(year):
    all_categories = get_all_categories()
    categories_with_count = get_categories_with_event_count(year)

    if all_categories and categories_with_count:
        print(f"Eventos ocurridos en el año {year} por categoría:")
        for category in all_categories:
            category_id = category['id']
            category_name = category['title']
            event_count = categories_with_count.get(category_id, 0)
            print(f"{category_name}: {event_count}")
    else:
        print(f"No se encontraron eventos en el año {year}.")


def main_menu():
    while True:
        print("\n-- MENÚ DE OPCIONES --")
        print("1. Obtener todas las categorías disponibles en la API")
        print("2. Imprimir un evento Random y su categoría")
        print("3. Imprimir en pantalla todos los eventos y sus categrías ocurridos en el año 2023")
        print("4. Salir")

        choice = input("Ingrese el número de la opción deseada: ")

        if choice == "1":
            all_categories = get_all_categories()
            if all_categories:
                print("Categorías presentes en la API de la NASA:")
                for category in all_categories:
                    print(category['title'])
                
        elif choice == "2":
            print_random_event_with_category()
            
        elif choice == "3":
            year = 2023
            print_categories_with_event_count(year)
        
        elif choice == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido de opción.")


if __name__ == "__main__":
    main_menu()
    