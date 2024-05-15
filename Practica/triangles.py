def equilateral(a:float,b:float,c:float)->bool:
    if (a==b and a==c):
        return True
    return False

print("This triang is equilateral: " + str(equilateral(3,3,3)))

def isosceles(a:float,b:float,c:float)->bool:
    if((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
        return True
    return False

print("This triang is isosceles: " + str(isosceles(2,3,2)))

def scalene(a:float,b:float,c:float)->bool:
    if(a != b and a != c and b != c):
        return True
    return False

print("This triang is scalene: " + str(scalene(2,3,4)))