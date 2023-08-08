import pandas as pd
import matplotlib.pyplot as plt

#Se coloca la ruta del archivo
ventas = r"C:\Users\wjuan\OneDrive\Documentos\UCR- Tecn\Python 2\Python-2\Lab 4\ventas.csv"

# Se lee el archivo csv y crea el DataFrame
df = pd.read_csv(ventas)

# Se realiza una nueva columna llamada ganancias donde resta los valores de las columnas ventas menos gastos
df["Ganancia"] = df["Ventas"]- df["Gastos"]
print(df)

# Se crean la figura y ejes para el gráfico
plt.figure(figsize=(10, 6))
ax = plt.gca()

# Grafica la evolución mensual de las ventas
ax.plot(df["Mes"], df["Ventas"], label="Ventas", color="yellow", marker="o")

# Grafica la evolución mensual de los gastos
ax.plot(df["Mes"], df["Gastos"], label="Gastos", color="green", marker="o")

# Etiquetas a los ejes y título del gráfico
plt.xlabel("Meses del año")
plt.ylabel("Monto en dólares")
plt.title("Gráfico de la evolución Mensual de Ventas y Gastos")
plt.legend()

# Mostrar el gráfico
plt.show()