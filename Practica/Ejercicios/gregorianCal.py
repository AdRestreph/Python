def leap_year(year:int)->bool:
    if(year % 100 != 0 and year % 4 == 0):
        return True
    elif(year % 100 == 0 and year % 400 == 0):
        return True
    return False

print(leap_year(2000))