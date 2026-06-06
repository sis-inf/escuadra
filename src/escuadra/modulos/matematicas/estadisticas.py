def calcular(datos: list) -> dict:
   
    if not datos:
        raise ValueError("La lista de datos está vacía.")
    
    for x in datos:
        if not isinstance(x, (int, float)):
            raise ValueError("La lista contiene elementos no numéricos.")

    n = len(datos)
    datos_ordenados = sorted(datos)

    media = sum(datos) / n


    mitad = n // 2
    if n % 2 == 0:
        mediana = (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
    else:
        mediana = datos_ordenados[mitad]

    frecuencias = {}
    for x in datos:
        frecuencias[x] = frecuencias.get(x, 0) + 1
    max_frecuencia = max(frecuencias.values())
    moda = [k for k, v in frecuencias.items() if v == max_frecuencia][0]

    varianza = sum((x - media) ** 2 for x in datos) / n

    desv_std = varianza ** 0.5

    valor_minimo = datos_ordenados[0]
    valor_maximo = datos_ordenados[-1]
    rango = valor_maximo - valor_minimo

    return {
        'media': float(media),
        'mediana': float(mediana),
        'moda': float(moda),
        'varianza': float(varianza),
        'desviacion_estandar': float(desv_std),
        'minimo': float(valor_minimo),
        'maximo': float(valor_maximo),
        'rango': float(rango)
    }
