import pandas as pd

# DataFrame de estudiantes duplicados
estudiantes_duplicados = pd.DataFrame({
    'Nombre': ['Juan', 'María', 'Carlos', 'Ana', 'Pedro'],
    'Edad': [20, 22, 21, 20, 23],
    'Curso': ['Matemáticas', 'Historia', 'Matemáticas', 'Historia', 'Inglés'],
    'Calificación': [85, 78, 92, 85, 76]
})

# Visualizar los primeros registros del DataFrame
print(estudiantes_duplicados.head())

# Identificar y mostrar registros duplicados basados en las columnas "Nombre" y "Curso"
duplicados = estudiantes_duplicados[estudiantes_duplicados.duplicated(subset=['Nombre', 'Curso'], keep=False)]
print(duplicados)

# Eliminar registros duplicados manteniendo la primera ocurrencia
estudiantes_sin_duplicados = estudiantes_duplicados.drop_duplicates(subset=['Nombre', 'Curso'], keep='first')

# Calcular la cantidad de registros duplicados que se eliminaron
cantidad_duplicados_eliminados = len(estudiantes_duplicados) - len(estudiantes_sin_duplicados)
print(f"Registros duplicados eliminados: {cantidad_duplicados_eliminados}")

# Calcular la calificación promedio para cada curso
calificaciones_promedio = estudiantes_sin_duplicados.groupby('Curso')['Calificación'].mean().reset_index()
print(calificaciones_promedio)

# Guardar el nuevo DataFrame en un archivo CSV
calificaciones_promedio.to_csv('calificaciones_promedio.csv', index=False)
