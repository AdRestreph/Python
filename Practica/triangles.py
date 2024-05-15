def triangleValidation(a:float, b:float, c:float)->bool:
    """Verify if the sides are >0 in a triangle.
    
    :param side a: float
    :param side b: float
    :param side c: float
    :return: bool - If the sides are <= 0 return False// Use the Triangle inequality validation
    """
    #verify if the sides are > 0
    if(a > 0 and b > 0 and c > 0):
        #verify the triangle inequality
        if((a + b >=c) or (b + c >=a) or (c + a >=b)):
            return True
    else:
        print("Sides error: Not is a valid triangle")
        return False

def typeTriangle(a:float, b:float, c:float)->str:
    """Verify the type of triangle.
    
    :param validation: Use the function triangleValidation. if True, clasifing the triangle
    :param side a: float
    :param side b: float
    :param side c: float
    :return: str - The type of triangle
    """
    validation= triangleValidation(a,b,c)
    result = "Not is possible the classification"
    if validation:
        #Validation equilateral triangle
        if (a==b and a==c):
            result = "triangle equilateral"
        #Validation isosceles triangle
        elif((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            result = "triangle isosceles"
        #Scalene triangle
        else:
            result = "triangle scalene"
    return result

print(typeTriangle(0,3,3))