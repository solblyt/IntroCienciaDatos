import math
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
  vals=[]
  for v in vals_in:
    if math.isfinite(v):
      vals.append(v)

  promedio=sum(vals)/len(vals)
  return promedio

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
  #eliminamos los valores que sean Nan
  vals=[]
  for v in vals_in:
    if math.isfinite(v):
      vals.append(v)

    #ordenar lista
    vals.sort()
    #determinar si es par o impar
    if len(vals)%2 !=0:
      k=len(vals)//2 #valor de al medio mas uno
      mediana=vals[k]
    else:
      k=len(vals)//2 #si no es impar el
      mediana=(vals[k-1]+vals[k])/2.0
    return mediana

def moda(vals):
  """
  Calcula la moda de una lista de numeros
  Parametros
  ----------
  vals : list
    Lista de numeros
  Retorna
  -------
     Moda:str
    Moda de los numeros en la lista
  """
  #encontrar conjuto de elementos unicos
  categorias=[]
  for v in vals:
    if v not in categorias:
      categorias.append(v)

  #obtenr el numero de cuentass en la muestra
  #para cada una de las categorias
  cuentas=[]
  for c in categorias:
    n=0
    for v in vals:
      if v==c:
        n=n+1
    cuentas.append(n)

  #encontrar la posicion del valor de la lista con el maximo de cuenta
  # guess and check
  i_max=0
  val_max=cuentas[0]
  for i in range(1,len(cuentas)):
    if cuentas[i]>val_max:
      i_max=i
      val_max=cuentas[i]
  #determinar todas las categorias que tenga el numero maximo de cuentas,mas de una moda
  #val_max dice cual es el valor maximo en la tabla de frecuencia
  modas=[]#se guardan todas las categorias que tengan el mismo numero, nuermo maximo
  for i in range(len(cuentas)):
    if cuentas[i]==val_max:
      modas.append(categorias[i])
  #retorno la moda
  #moda=categorias[i_max]  , ya no se resporta sola una
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
  #eliminar los Nans
  vals=[]
  for v in vals_in:
    if math.isfinite(v):
      vals.append(v)
  #determinar maximo y minimo desde 0
  # forma 2- gues and check adivino luego rectifico
  for v in vals:
    if v<minimo:
      minimo=v
    if v>maximo:
      maximo=v

  return maximo-minimo


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
  #eliminamos los valores que sean NANs
  vals=[]
  for v in vals_in:
    if math.isfinite(v):
      vals.append(v)

  #estimar promedio
  promedio=promedio(vals)

  #estimamos las desviaciones cuadraticas medias
  dcm=[]
  for v in vals:
    dcm.append((v-promedio)**2)

  #estimamos la varianza
  varianza=sum(dcm)/len(vals)
  return varianza

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
  #eliminamos los valores NANs
  vals=[]
  for v in vals_in:
    if math in vals_in:
      vals.append(v)

  #estimamos llas desviaciones cuadraticas medias
  dcm=[]
  for v in vals:
    dcm.append((v-promedio)**2)

  #estimamos la varianza
  varianza=sum(dcm)/len(vals)
  return varianza**0.5

#funcion de percentiles y rango intercuartil
def percentiles(vals_in):
    """
    Calcula los percentiles 25 y 75 de una lista de números.
    """
    # Usamos numpy para calcular los percentiles 25 y 75
    p25 = np.percentile(vals_in, 25)
    p75 = np.percentile(vals_in, 75)
    return {'25th': p25, '75th': p75}

def iqr(vals_in):
    """
    Calcula el rango intercuartil de una lista de números
    eliminando y detectando los NaNs.
    
    Parametros
    ----------
    vals_in : list
        Lista de números.
    
    Retorna
    -------
    float
        El rango intercuartil (IQR).
    """
    # Eliminar los NaNs
    vals = [v for v in vals_in if math.isfinite(v)]
    
    # Calcular los percentiles 25 y 75
    percentil_vals = percentiles(vals)
    
    # Calcular el IQR
    iqr_value = percentil_vals['75th'] - percentil_vals['25th']
    return iqr_value
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
    Desviacion

  """
  vals=[]
  for v in vals_in:
    if math.isfinite(v):
      vals.append(v)

  mad=sum(abs(vals-promedio(vals)))/len(vals)
  return mad



def covarianza(vals_x,vals_y):
  """
  calcula la variaza de una lista de numeros
  detecta y elimina los NANs
  parametros 
  ----
  vals_x,vals_y: lista
  retorna
  ---------
  covarianza:float
    covarianza 
  """
  x=[]
  y=[]
  for i in range(len(vals_x)):
    if math.isfinite(vlas_x[i]) and math.isfinite(vals_y[i]):
      x.append(vals_x[i])
      y.append(vals_y[i]) 

  p_x=promedio(x)
  p_y=promedio(y)

  tt=[]
  for xv,yv in zip(x,y):
    tt.append((xv-p_x)*(yv-p_y))
  covarianza= sum(tt)/len(tt)
  return covarianza


def correlacion(vals_x,vals_y):
  """
  Calcula la correlacion de dos listas de numeros
  elimina y detecta los NANS
  Parametros
  ----------
  vals1,vals2 : list
    Listas de numeros
  Retorna
  -------
     Correlacion:float
    Correlacion de
  """
  x=[]
  y=[]
  for i in range(len(vals_x)):
    if math.isfinite(vals_x[i]) and math.isfinite(vals_y[i]):
      x.append(vals_x[i])
      y.append(vals_y[i]) 

  rxy=covarianza(x,y)/(varianza(x)*varianza(y))
  return rxy








  #zip entega tuplas















