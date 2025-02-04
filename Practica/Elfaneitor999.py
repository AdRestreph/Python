def comprobar_palindromo(numero:int)->bool:
    """
    Parameteros
    ----------
    numero : int
    ----------
    Comprueba si un numero es palindromo
    Returns booleano
    Retorna True si el numero es palindromo, de lo contrario retorna False
    """
    numero = str(numero)
    if numero == numero[::-1]:
        return True
    else:
        return False

def comprobar_par_o_impar(numero:int)->bool:
    """
    Parameteros
    ----------
    numero : int
    ----------
    Comprueba si el numero es par o impar para categorizar el regalo
    Returns string
    Retorna True o False respectivamente
    """
    if numero % 2 == 0:
        return True
    else:
        return False

def comprobar_regalo(palindromo:bool, par:bool)->str:
    """
    Parameteros
    ----------
    palindromo : bool
    par_o_impar : bool
    ----------
    Comprueba si el numero es par o impar, palindromo o no para categorizar el regalo y ser entregado
    Returns string
    """
    if palindromo == True and par == True:
        return "El regalo es para un niño"
    elif palindromo == True and par == False:
        return "El regalo es para una niña"
    elif palindromo == False and par == True:
        return "El regalo es para un hombre"
    else:
        return "El regalo es para una mujer"

etiqueta = int(input("Ingrese un numero para clasificar la etiqueta: "))
print(f'El numero ingresado es: {etiqueta} y {comprobar_regalo(comprobar_palindromo(etiqueta), comprobar_par_o_impar(etiqueta))}')

