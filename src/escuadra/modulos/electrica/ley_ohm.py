def calcular(V=None, I=None, R=None) -> dict:
    datos_recibidos = 0
    if V is not None: datos_recibidos += 1
    if I is not None: datos_recibidos += 1
    if R is not None: datos_recibidos += 1

    if datos_recibidos != 2:
        raise ValueError("Debes poner exactamente dos valores para calcular el tercero.")

    if (V is not None and V < 0) or (I is not None and I < 0) or (R is not None and R < 0):
        raise ValueError("Los valores no pueden ser negativos.")

    if V is None:
        V = float(I * R)
        
    elif I is None:
        if R == 0:
            raise ValueError("No se puede dividir por cero (Resistencia R no puede ser 0).")
        I = float(V / R)
        
    elif R is None:
        if I == 0:
            raise ValueError("No se puede calcular R si la Intensidad I es 0.")
        R = float(V / I)

    P = float(V * I)

    return {
        'V': V, 
        'I': I, 
        'R': R, 
        'P': P
    }
