# Cargar los conjuntos de datos desde archivos CSV
cursos = pd.read_csv('cursos.csv')
estudiantes = pd.read_csv('estudiantes.csv')

# Realizar una agregación para obtener la cantidad de estudiantes por género
agregacion_genero = estudiantes.groupby('Género').size().reset_index(name='Cantidad')
print(agregacion_genero)

# Realizar una agregación para obtener la edad promedio de los estudiantes por curso
agregacion_edad_curso = estudiantes.groupby('Curso')['Edad'].mean().reset_index(name='Edad Promedio')
print(agregacion_edad_curso)

# Fusionar los DataFrames de estudiantes y cursos utilizando un join por el campo "Curso"
resultados_agregaciones = pd.merge(estudiantes, cursos, on='Curso')

# Guardar los resultados de las agregaciones en un archivo CSV
resultados_agregaciones.to_csv('resultados_agregaciones.csv', index=False)

# Mostrar los resultados de las agregaciones
print(resultados_agregaciones)
