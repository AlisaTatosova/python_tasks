from expression import AbsractExpression, Const, Add

class X(AbsractExpression):
    def __init__(self, power = 1):
        self.power = power

    def __call__(self, value):
        result = 1
        for _ in range(0, self.power):
            result *= value
        return result
    
    def derivative(self):
        return Const(self.power) * X(self.power - 1)

    def __str__(self):
        return f"(x) ^ {self.power}"


def Polynomial(*coefficients):
    print(coefficients[0])
    result = Const(0)
    for i, item in enumerate(coefficients):
        result += (Const(item) * X(i))
    return result

   