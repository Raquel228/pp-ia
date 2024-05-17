# Definir una función para calcular el último cuartil y el percentil 80
def calcular_percentiles(datos):
    datos_ordenados = sorted(datos)
    #CALCULAR INDICES
    ultimo_cuartil_idx = int(len(datos_ordenados) * 0.75)    
    percentil_80_idx = int(len(datos_ordenados) * 0.8)

    # Obtener los valores correspondientes a los índices calculados
    ultimo_cuartil = datos_ordenados[ultimo_cuartil_idx]
    percentil_80 = datos_ordenados[percentil_80_idx]
    return ultimo_cuartil, percentil_80

columnasE = []  # Lista para almacenar los encabezados de las columnas
columnas = [[] for _ in range(14)]  # Lista de listas para almacenar los valores de las columnas

with open("data.csv", "r", encoding="latin1") as file:
    # Leer encabezados
    columnasE = file.readline().strip().split(",")    
    # Leer datos de las columnas
    for line in file:
        valores = line.strip().split(",")
        for i in range(14):
            if i in [0, 3, 4, 5, 9, 10, 11, 12, 13]:
                columnas[i].append(float(valores[i]))

# Calcular el último cuartil y el percentil 80 para cada columna numérica
for i in range(14):
    if i in [0, 3, 4, 5, 9, 10, 11, 12, 13]:
        ultimo_cuartil, percentil_80 = calcular_percentiles(columnas[i])
        print(f"{columnasE[i]} =>\t Último cuartil = {ultimo_cuartil}\tPercentil-80 = {percentil_80}")
