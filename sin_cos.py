import math
from expression import AbsractExpression, Mul

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
        return Mul(MinusOneToCallableObject(), Sin())
    
    def __str__(self):
        return f"cos(x)"
    
class MinusOneToCallableObject(AbsractExpression):         
    def derivative(self):
        return 0

    def __call__(self, value):
        return -1
    
    def __str__(self):
        return f"(-1)"
