import pandas as pd
from scipy import stats
# Leer datos del archivo CSV
data = pd.read_csv("data.csv", encoding="latin1")
# Seleccionar las columnas de interés que contienen números
columnasN = data[["num_passengers", "purchase_lead", "length_of_stay", "flight_hour", "wants_extra_baggage", "wants_preferred_seat", "wants_in_flight_meals", "flight_duration", "booking_complete"]]

# Calcular la media, mediana, moda y media geométrica
print("Columna\t\t\tMedia\t\tMediana\tModa\tMedia Geométrica")
for col in columnasN:
    media = columnasN[col].mean()
    mediana = columnasN[col].median()
    moda = columnasN[col].mode()[0]  # Puede haber más de una moda, tomamos la primera
    geo = stats.gmean(columnasN[col])
    print(col,media,mediana,moda,round(geo,3), sep="  \t")