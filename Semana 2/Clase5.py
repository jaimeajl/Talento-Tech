# Importar librerías
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Crear un conjunto de datos
# Construir las listas de valores
value_est_list = ['Carlos Rodríguez', 'María Lopez', 'Javier Martínez', 'Laura Fernández', 'Diego Pérez', 'Sofía González', 'Pedro Ramírez', 'Isabel Torres', 'Andrés Sánchez']
print(value_est_list)

value_fn_list = ['12/03/1998', '5/05/1995', '20/01/2000', '8/09/1997', '3/05/1996', '18/11/1999', '27/04/1994', '10/08/1993', '14/02/1992']
value_fi_list = ['12/03/2011', '5/05/2008', '20/01/2013', '8/09/2010', '3/05/2009', '18/11/2012', '27/04/2014', '10/08/2013', '14/02/2012']
value_np_list = [3.1, 4.2, 2.5, 3.5, 2.0, 4.5, 4.0, 1.5, 2.8]
value_nm_list = [5, 6, 5, 4, 5, 6, 4, 5, 6]

# Usar un diccionario ({clave:valor}) con el formato {"str":list}
data_dict = {
    "name": value_est_list,
    "fecha_nacimiento": value_fn_list,
    "fecha_ingreso": value_fi_list,
    "notas_promedio": value_np_list,
    "no_materias": value_nm_list
}

print(data_dict)

# Convertir el diccionario en un DataFrame
df = pd.DataFrame(data_dict)
print(df)

# Obtener estadísticas descriptivas de columnas numéricas
estadisticas_numericas = df.describe()

# Obtener estadísticas descriptivas de columnas categóricas
estadisticas_categoricas = df.describe(include=[object])

# Imprimir estadísticas descriptivas
print("Estadísticas descriptivas de columnas numéricas:")
print(estadisticas_numericas)

print("\nEstadísticas descriptivas de columnas categóricas:")
print(estadisticas_categoricas)
