#Se importa el módulo 
from trig import Trig
#Se importa la hora y fecha
import datetime

#Se crea una instancia de la clase

trig_instance = Trig()

#Mostrar un menú 
print("Seleccione la operación que desea realizar")
print("1.Valor de pi")
print("2.Valor sin de pi")
print("3.Valor cos de pi")
print("4.Valor tan de pi")
print ("5. Salir")

#El usuario selecciona una opción
opcion = input("Ingrese el número de la operación que desea realizar")

#Se realiza la operación solicitada por el usuario
if opcion == "1":
    operation = "Valor de Pi"
    result = Trig.pi

elif opcion == "2":
    operation = "Valor sin de pi"
    result = Trig.sin_pi

elif opcion == "3":
    operation = "Valor cos de pi"
    result = Trig.cos_pi
    
elif opcion == "4":
    operation = "Valor tan de pi"
    result = Trig.tan_pi

elif opcion == "5":
    exit()

else: 
    print("Opción no válida")
    exit()

# Mostrar el resultado en la pantalla
print("El resultado de la operación es:", result)

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.datetime.now()

# Formatear la fecha y hora actual
fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")

# Se crea el documento de texto donde se registra la hora, fecha y operación realizada
text = "log.txt"

# Crear una cadena con la información a guardar en el archivo
data = f"Fecha y hora: {fecha_hora_formateada}\nOperación realizada: {operation}\nResultado: {result}\n"

# Abrir el archivo en modo de escritura

with open(text, "a") as archivo:
    
# Escribir la cadena en el archivo
    archivo.write(data + "\n")

print("Información guardada en el archivo.")