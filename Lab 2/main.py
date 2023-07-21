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
import concurrent.futures
import aiohttp
import asyncio

async def get_username_async(): 
    async with aiohttp.ClientSession() as session:
        task = [api.get_username_async(session, item) for item in ids]
        await asyncio.gather(*task, return_exceptions=True)

def get_username(id):
    user = api.getOneUser(id)
    username = user["username"]
    return username

def get_username_threading():
    with concurrent.futures.ThreadPoolExecutor(max_workers= 5) as executor:
        usernames = list(executor.map(get_username,ids))
    return usernames
    

if __name__ == "__main__":
    start_time = time.time()
   
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_username_async())
    
    # usernames = get_username_threading()
    
    # Función para cuantificar e imprimir el tiempo
    end_time = time.time()
    execution_time = end_time - start_time
    print("Tiempo de ejecución:", execution_time, "segundos")