import requests as req

url = "https://jsonplaceholder.typicode.com/users/"

def getOneUser(id):
    response = req.get(url)
    return response.json()[id]


async def get_username_async(sesion, id):
    async with sesion.get(url) as response:
        jsonRes = await response.json()
        print(jsonRes[id]["name"])