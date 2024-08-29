
def promedio(*args:tuple)-> int:
    return sum(args)// len(args)

def promedio2(*args:tuple)-> int:
    return ##mean(args)
    
print(promedio(1, 2, 3, 4, 5))
print(promedio2(1, 2, 3, 4, 5))