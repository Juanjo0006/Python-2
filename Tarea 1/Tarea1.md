*Documentación*

API elegida: EONET (Earth Observatory Natural Event Tracker)
[URL] (https://eonet.gsfc.nasa.gov/docs/v2.1)

La página que pertenece a la NASA permite acceder a datos sobre fenómenos naturales ocurridos. 

*Endpoints*

GET: https://eonet.gsfc.nasa.gov/api/v2.1/events?year={year}
Parámetro: "Year"
GET: https://eonet.gsfc.nasa.gov/api/v2.1/categories

*Funciones*

1. get_categories_with_event_count(year): Esta función obtiene los eventos pobtenidos de la API recibiendo el parámentro "year". La información se filtra y la función cuenta la cantidad de eventos por categoría. Identifica las categorías y devuelve valores como la cantidad de eventos ocurridos. 
2. get_all_categories(): Esta fucnión solicita el nombre de todas las categorías y devuelve la lista con los nombres de todas las categorías presentes en la API. 
3. print_categories_with_event_count(year): En esta fucnión se imprimen la cantidad de eventos por categoría utilizando las dos funciones anteriores. 
