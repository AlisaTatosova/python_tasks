from expression import AbsractExpression, Const

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

class Polynomial(X):
    def __init__(self, *coefficients):
        self.result = Const(coefficients[0])
        for i, item in enumerate(coefficients):
            self.result += (Const(item) * X(i))

    def __call__(self, value):
        return self.result.__call__(value)

    def derivative(self):
        return self.result.derivative()

    def __str__(self):
        return str(self.result)