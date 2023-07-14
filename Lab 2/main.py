# #Se importan los módulos necesarios. 
# import api
# from ids import ids
# import time

# #Se inicia el conteo de tiempo
# start_time = time.time()

# #Se crea la función que imprima los nombres de usuario 
# for id in ids:
#     user = api.getOneUser(id)
#     username = user["username"]
#     print(username)

# #Función para cuantificar e imprimir el tiempo
# end_time = time.time()
# execution_time = end_time - start_time
# print("Tiempo de ejecución:", execution_time, "segundos")



#Código modificado para implementar multiprocess
import api
from ids import ids
import time
import multiprocessing

def get_username(id):
    user = api.getOneUser(id)
    username = user["username"]
    return username

if __name__ == "__main__":
    # Se inicia el conteo de tiempo.
    start_time = time.time()

    # Se crea un Pool y se utiliza map para obtener los nombres
    pool = multiprocessing.Pool()
    usernames = pool.map(get_username, ids)

    # Se cierra el Pool
    pool.close()
    pool.join()

    # Se imprimen los nombres de usuario
    for username in usernames:
        print(username)

    # Función para cuantificar e imprimir el tiempo
    end_time = time.time()
    execution_time = end_time - start_time
    print("Tiempo de ejecución:", execution_time, "segundos")