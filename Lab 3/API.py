import requests as req
import random

#GET1
#Se crea una función que importe un chiste aleatorio de la URL del API. 
def get1request(): 
    url = "https://api.chucknorris.io/jokes/random"
    getresponse = req.get(url)

    if getresponse.status_code == 200:
        joke = getresponse.json()
        print("La respuesta del servidor es:")
        print(joke)
    else:
        print("Error al realizar la solicitud.")

#GET2
#Se crea una función que imprima las categorías disponibles en la URL del API. 
def get2request(): 
    url = "https://api.chucknorris.io/jokes/categories"
    getresponse = req.get(url)
    
    if getresponse.status_code == 200:
        categories = getresponse.json()
        print("La respuesta del servidor es:")
        print(categories)
        
    else:
        print("Error al realizar la solicitud.")


#GET3
#Se crea una función que seleccione una categoría
def get3request(): 
    def get_random_category():
        url = "https://api.chucknorris.io/jokes/categories"
        response = req.get(url)
    
        if response.status_code == 200:
            categories = response.json()
            return random.choice(categories)
        else:
            print("Error al obtener las categorías.")
            return None


#Se crea una función que obtenga un chiste de una categoría cualquiera.
    def get_random_joke(category):
        url = f"https://api.chucknorris.io/jokes/random?category={category}"
        response = req.get(url)
    
        if response.status_code == 200:
            joke_data = response.json()
            return joke_data["value"]
        else:
            print("Error al obtener el chiste.")
            return None

    category = get_random_category()

    if category:
        joke = get_random_joke(category)
        
        if joke:
            print("Categoría:")
            print(category)
            
            print("\nChiste:")
            print(joke)
        
#Se crea el menú para que el usuario seleccione la opción que requiera
def main_menu():
    while True:
        print("\n-- MENÚ DE OPCIONES --")
        print("1. Obtener un chiste aleatorio")
        print("2. Obtener categorías de chistes")
        print("3. Obtener chiste de categoría aleatoria")
        print("4. Salir")

        choice = input("Ingrese el número de la opción deseada: ")

        if choice == "1":
            get1request()
        elif choice == "2":
            get2request()
        elif choice == "3":
            get3request()
        elif choice == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido de opción.")


if __name__ == "__main__":
    main_menu()
    
    
