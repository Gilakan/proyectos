import pandas as pd

# DataFrame de empleados
empleados = pd.DataFrame({
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Carlos'],
    'Edad': ['25', '30', '27', '35', '40'],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Bilbao'],
    'Salario': ['2000', '2500', '2200', '3000', '3500']
})

# Conversión de Tipos de Datos
empleados['Edad'] = pd.to_numeric(empleados['Edad'])
empleados['Salario'] = pd.to_numeric(empleados['Salario'])

# Imprimir tipos de datos del DataFrame
print(empleados.dtypes)

# Acceso a Datos Específicos
print(empleados['Ciudad'])

pedro_data = empleados.loc[empleados['Nombre'] == 'Pedro']
print(pedro_data)

# Filtrado Básico
filtro_mayor_30 = empleados[empleados['Edad'] > 30]
print(filtro_mayor_30)
