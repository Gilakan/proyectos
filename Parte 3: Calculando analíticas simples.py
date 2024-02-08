import pandas as pd

# Supongamos que 'dataset' es tu DataFrame
# Reemplaza esto con el nombre real de tu DataFrame

# Verificar que los tipos de datos son correctos en cada columna
# Asegurar que las columnas numéricas no estén en formato de cadena
dataset['Edad'] = pd.to_numeric(dataset['Edad'], errors='coerce')
# Agrega más conversiones si es necesario para otras columnas

# Calcular la cantidad de hombres fumadores vs mujeres fumadoras usando agregaciones en Pandas
agregacion_fumadores = dataset.groupby(['Género', 'Fumador']).size().reset_index(name='Cantidad')

# Filtrar y mostrar solo la cantidad de hombres y mujeres fumadores
cantidad_hombres_fumadores = agregacion_fumadores[(agregacion_fumadores['Género'] == 'Hombre') & (agregacion_fumadores['Fumador'] == 'Sí')]['Cantidad'].values[0]

cantidad_mujeres_fumadoras = agregacion_fumadores[(agregacion_fumadores['Género'] == 'Mujer') & (agregacion_fumadores['Fumador'] == 'Sí')]['Cantidad'].values[0]

print(f"Cantidad de hombres fumadores: {cantidad_hombres_fumadores}")
print(f"Cantidad de mujeres fumadoras: {cantidad_mujeres_fumadoras}")
