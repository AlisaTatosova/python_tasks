from abc import ABC, abstractmethod

class AbsractExpression(ABC):
    @abstractmethod
    def __call__(self, value):
        pass

    @abstractmethod
    def derivative(self):
        pass

    def __add__(self, other):
        return Add(self, other)

    def __sub__(self, other):
        return Sub(self, other)

    def __mul__(self, other):
        return Mul(self, other)

    def __truediv__(self, other):
        return Div(self, other)
    
class Add(AbsractExpression):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, value):
        return self.f(value) + self.g(value)

    # (f(x) + g(x))' = f'(x) + g'(x)
    def derivative(self):
        return Add(self.f.derivative(), self.g.derivative())
    
    def __str__(self):
        return f"({self.f} + {self.g})"

class Sub(AbsractExpression):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, value):
        return self.f(value) - self.g(value)

    # (f(x) - g(x))' = f'(x) - g'(x)
    def derivative(self):
        return Sub(self.f.derivative(), self.g.derivative())
    
    def __str__(self):
        return f"({self.f} - {self.g})"

class Mul(AbsractExpression):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, value):
        return self.f(value) * self.g(value)

    # (f(x) * g(x))' = f'(x) g(x) + f(x) g'(x)
    def derivative(self):
        return Add(Mul(self.f.derivative(), self.g), Mul(self.f, self.g.derivative()))
    
    def __str__(self):
        return f"({self.f} * {self.g})"

class Div(AbsractExpression):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, value):
        return self.f(value) / self.g(value)

    # (f(x) / g(x))' = (f'(x) * g(x) - f(x) * g'(x)) / g^2(x)
    def derivative(self):
        return Div(Sub(Mul(self.f.derivative(), self.g), Mul(self.f, self.g.derivative())), Mul(self.g, self.g))
    
    def __str__(self):
        return f"({self.f} / {self.g})"
    

