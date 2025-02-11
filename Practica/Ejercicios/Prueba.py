numeros = {
    1:'uno',
    2:'dos',
    3:'tres',
    4:'cuatro',
    5:'cinco',
    6:'seis',
    7:'siete',
    8:'ocho',
    9:'nueve'
}

def numbers(n:int,numeros:dict)-> str:
    if ((1<=n) and (n<=9)):
        print(numeros[n])
    else:
        print("Es mayor que nueve (9)")
    
numbers(6, numeros)