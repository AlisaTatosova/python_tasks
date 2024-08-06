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
    
    def apply(self, other):
        return Composition(self, other)
    
class Add(AbsractExpression):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, value):
        return self.f(value) + self.g(value)

    # (f(x) + g(x))' = f'(x) + g'(x)
    def derivative(self):
        return self.f.derivative() + self.g.derivative()
    
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
        return self.f.derivative() - self.g.derivative()
    
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
        return (self.f.derivative() * self.g) + (self.f * self.g.derivative())
    
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
        return ((self.f.derivative() * self.g) - (self.f * self.g.derivative())) / (self.g * self.g)
    
    def __str__(self):
        return f"({self.f} / {self.g})"
    
class Composition(AbsractExpression):
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def __call__(self, value):
        return self.f(self.g(value))

    # (f ∘ g)′(x) = f′(g(x)) ⋅ g′(x)
    def derivative(self):
        return self.f.derivative().apply(self.g) * self.g.derivative()
    
    def __str__(self):
        outer = str(self.f)
        inner = str(self.g)
        return outer.replace('(x)', f"({inner})")
        