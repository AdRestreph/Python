## PROBLEMA: REALIZAR ECUACION
## -------------------------------
## ODE - ECUACION DIFERENCIAL ORDINARIA
## ENTRADAS:
## - DATO INICIAL
## - CONCENTRACION DE MOLES INCIALES EN TIEMPO X
## - PARAMETROS
## -------------------------------
## MAIN:
## ENTRADAS:
## - BALANCE DE MASA (ODE)
## - CONSTANTE DE VELOCIDAD
## PROCESO:
## - DADO EL BALANCE DE MASA - LOS DATOS FALTANTES
##------------------------------
## SALIDAS:
## CONCENTRACION ESPECIFICA DE ACETONA 99% EN UN REACTOR POR UNA PERTUBACION

## -> BLOQUE DE INTEGRACION SIMPLE

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definir la ecuación diferencial
def balance_masa(y, t, k):
    dydt = -k * y
    return dydt

# Condiciones iniciales
dato_inicial = 5
k = 0.3

# Puntos de tiempo donde se evaluará la solución
t = np.linspace(0, 20, 100)

# Resolver la ODE
solucion = odeint(balance_masa, dato_inicial, t, args=(k,))

# Graficar la solución
plt.plot(t, solucion)
plt.xlabel('Tiempo')
plt.ylabel('Concentración')
plt.title('Solución de la ODE')
plt.show()