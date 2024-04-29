expectedBakeTime = 40

def bakeTimeRemaining(timeRemaining:int)->int:
    """This function calculates the time remaining"""
    result = 40 - timeRemaining
    return result

print ((bakeTimeRemaining(30)))

def preparationTimeInMinutes(layers:int)->int:
    """This function calculates the time in minutes depending of the number of layers"""
    result = layers*2
    return result

print ((preparationTimeInMinutes(3)))

def elapsedTimeInMinutes(numberOfLayers:int,elapsedBakeTime:int)->int:
    """This function calls the other function to calculate the sum between elapsed time and number of layers
        preparationTimeInMinutes: Return the layers *2 to know how time remaining in minutes is adds to total time 
    """
    result = preparationTimeInMinutes(numberOfLayers) + elapsedBakeTime
    return result

print (elapsedTimeInMinutes(3,20))
print(elapsedTimeInMinutes.__doc__)