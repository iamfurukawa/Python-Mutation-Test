import math

class Math:

    def __init__(self):
        pass

    def sum(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2
    
    def mult(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        if num2 == 0:
            return math.inf
        return num1 / num2

    def divFloor(self, num1, num2):
        if num2 == 0:
            return math.inf
        return num1 // num2
    
    def mod(self, num1, num2):
        if num2 == 0:
            return None
        return num1 % num2
