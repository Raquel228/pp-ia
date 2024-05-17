import pandas as pd
import numpy as np

# Leer datos del archivo CSV
data = pd.read_csv("data.csv", encoding="latin1")
# Columnas que contienen números
columnasN = data[["num_passengers", "purchase_lead", "length_of_stay", "flight_hour", "wants_extra_baggage", "wants_preferred_seat", "wants_in_flight_meals", "flight_duration", "booking_complete"]]

# Convertir los datos de pandas a un arreglo de NumPy
datos_np = columnasN.to_numpy()

# Calcular el último cuartil y el percentil 80 para cada columna
ultimo_cuartil = np.percentile(datos_np, 75, axis=0)
percentil_80 = np.percentile(datos_np, 80, axis=0)

# Imprimir los resultados
for i, col in enumerate(columnasN.columns):
    print(col,"=>\tÚltimo cuartil=", ultimo_cuartil[i],"\tPercentil-80=", percentil_80[i])