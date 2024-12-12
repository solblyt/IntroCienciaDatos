import math
import numpy as np

def promedio(vals_in):
    """
    Calcula el promedio de una lista de numeros
    Parametros
    ----------
    vals_in : list
        Lista de numeros
    Retorna
    -------
    Promedio:float
        Promedio de los numeros en la lista
    """
    vals = [v for v in vals_in if math.isfinite(v)]
    return sum(vals) / len(vals)

def mediana(vals_in):
    """
    Calcula la mediana de una lista de numeros
    Parametros
    ----------
    vals : list
        Lista de numeros
    Retorna
    -------
    Mediana:float
        Mediana de los numeros en la lista excluyendo Nans
    """
    vals = [v for v in vals_in if math.isfinite(v)]
    vals.sort()
    
    if len(vals) % 2 != 0:
        return vals[len(vals)//2]
    else:
        mid = len(vals) // 2
        return (vals[mid-1] + vals[mid]) / 2.0

def moda(vals):
    """
    Calcula la moda de una lista de numeros
    Parametros
    ----------
    vals : list
        Lista de numeros
    Retorna
    -------
    Moda: list
        Lista de modas de los numeros en la lista
    """
    categorias = list(set(vals))
    cuentas = [vals.count(c) for c in categorias]
    
    max_count = max(cuentas)
    modas = [categorias[i] for i in range(len(cuentas)) if cuentas[i] == max_count]
    
    return modas

def rango(vals_in):
    """
    Calcula el rango de una lista
    Detecta y elimina los NaN
    Parametros
    ----------
    vals : list
        Lista de numeros
    Retorna
    -------
    Rango:float
        Rango de los numeros (excluyendo NANs)
    """
    vals = [v for v in vals_in if math.isfinite(v)]
    return max(vals) - min(vals)

def varianza(vals_in):
    """
    Calcula la varianza de una lista de numeros
    elimina y detecta los NANS
    Parametros
    ----------
    vals : list
        Lista de numeros
    Retorna
    -------
    Varianza:float
        Varianza de los numeros en la lista
    """
    vals = [v for v in vals_in if math.isfinite(v)]
    prom = promedio(vals)
    return sum((v - prom) ** 2 for v in vals) / len(vals)

def std(vals_in):
    """
    Calcula la desviacion estandar de una lista de numeros
    elimina y detecta los NANS
    Parametros
    ----------
    vals : list
        Lista de numeros
    Retorna
    -------
    Desviacion estandar:float
        Desviacion estandar de los numeros en la lista
    """
    vals = [v for v in vals_in if math.isfinite(v)]
    var = varianza(vals)
    return math.sqrt(var)

def percentiles(vals_in):
    """
    Calcula los percentiles 25 y 75 de una lista de números.
    """
    p25 = np.percentile(vals_in, 25)
    p75 = np.percentile(vals_in, 75)
    return {'25th': p25, '75th': p75}

def iqr(vals_in):
    """
    Calcula el rango intercuartil de una lista de números eliminando y detectando los NaNs.
    Parametros
    ----------
    vals_in : list
        Lista de números.
    Retorna
    -------
    float
        El rango intercuartil (IQR).
    """
    vals = [v for v in vals_in if math.isfinite(v)]
    percentil_vals = percentiles(vals)
    return percentil_vals['75th'] - percentil_vals['25th']

def mad(vals_in):
    """
    Calcula la desviacion media absoluta de una lista de numeros
    elimina y detecta los NANS
    Parametros
    ----------
    vals : list
        Lista de numeros
    Retorna
    -------
    Desviacion media absoluta:float
        Desviacion media absoluta de los numeros en la lista
    """
    vals = [v for v in vals_in if math.isfinite(v)]
    prom = promedio(vals)
    return sum(abs(v - prom) for v in vals) / len(vals)

def covarianza(vals_x, vals_y):
    """
    Calcula la covarianza de dos listas de numeros
    Detecta y elimina los NaNs
    Parametros
    ----------
    vals_x, vals_y : list
        Listas de numeros
    Retorna
    -------
    covarianza: float
        Covarianza entre las dos listas
    """
    x = [vals_x[i] for i in range(len(vals_x)) if math.isfinite(vals_x[i]) and math.isfinite(vals_y[i])]
    y = [vals_y[i] for i in range(len(vals_y)) if math.isfinite(vals_x[i]) and math.isfinite(vals_y[i])]
    
    prom_x = promedio(x)
    prom_y = promedio(y)
    
    return sum((x[i] - prom_x) * (y[i] - prom_y) for i in range(len(x))) / len(x)

def correlacion(vals_x, vals_y):
    """
    Calcula la correlacion de dos listas de numeros
    elimina y detecta los NANS
    Parametros
    ----------
    vals_x, vals_y : list
        Listas de numeros
    Retorna
    -------
    correlacion: float
        Correlación entre las dos listas
    """
    covar = covarianza(vals_x, vals_y)
    std_x = std(vals_x)
    std_y = std(vals_y)
    
    return covar / (std_x * std_y)


def eliminar_nans(vals_in):
    """
    Elimina los valores NaN de una lista de números, asegurándose de que los elementos sean flotantes.
    Parametros
    ----------
    vals_in : list
        Lista de números que puede contener NaN o cadenas de texto.
    Retorna
    -------
    list
        Lista sin los valores NaN ni los valores no convertibles a float.
    """
    cleaned_vals = []
    for v in vals_in:
        try:
            # Convertir a flotante, y verificar si es un número finito
            v_float = float(v)
            if math.isfinite(v_float):
                cleaned_vals.append(v_float)
        except ValueError:
            # Si no se puede convertir a float, simplemente lo descartamos
            continue
    return cleaned_vals











