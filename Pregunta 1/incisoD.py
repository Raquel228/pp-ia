import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos CSV en un DataFrame de pandas
data = pd.read_csv("data.csv", encoding="latin1")

# Obtener las columnas del DataFrame
columnas = data.columns

# Iterar sobre cada columna y graficar
for col in columnas:
    # Verificar si la columna es categórica (es decir, tiene menos de 10 valores únicos)
    if data[col].nunique() < 10:
        plt.figure(figsize=(8, 6))
        sns.countplot(x=col, data=data)
        plt.title(f'Distribución de {col}')
        plt.xlabel(col)
        plt.ylabel('Cantidad')
        plt.show()
    else:
        plt.figure(figsize=(8, 6))
        sns.histplot(data[col], bins=20, kde=True)
        plt.title(f'Distribución de {col}')
        plt.xlabel(col)
        plt.ylabel('Cantidad')
        plt.show()