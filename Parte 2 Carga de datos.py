import pandas as pd

# Supongamos que 'dataset' es tu conjunto de datos
# Reemplaza esto con el nombre real de tu conjunto de datos

# Convertir la estructura Dataset en un DataFrame de Pandas usando pd.DataFrame
# Aquí asumimos que tienes un diccionario de datos similar al siguiente
data = {
    'Nombre': ['Persona1', 'Persona2', 'Persona3', 'Persona4'],
    'Edad': [25, 30, 22, 35],
    'is_dead': [0, 1, 0, 1]
}

dataset = pd.DataFrame(data)

# Separar el dataframe en dos diferentes
df_perecidos = dataset[dataset['is_dead'] == 1]
df_no_perecidos = dataset[dataset['is_dead'] == 0]

# Calcular los promedios de las edades de cada dataset e imprimir
promedio_edades_perecidos = df_perecidos['Edad'].mean()
promedio_edades_no_perecidos = df_no_perecidos['Edad'].mean()

print(f"Promedio de edades de personas que perecieron: {promedio_edades_perecidos}")
print(f"Promedio de edades de personas que no perecieron: {promedio_edades_no_perecidos}")
