import math
from expression import AbsractExpression
from polynomial import Polynomial

class Sin(AbsractExpression):
    def __call__(self, value):
        return math.sin(value)

    def derivative(self):
        return Cos()
    
    def __str__(self):
        return f"sin(x)"
    
class Cos(AbsractExpression):
    def __call__(self, value):
        return math.cos(value)

    def derivative(self):
        return Polynomial(-1) * Sin()
    
    def __str__(self):
        return f"cos(x)"