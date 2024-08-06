from expression import AbsractExpression

class Polynomial(AbsractExpression):
    def __init__(self, *coefficients):
        self.coefficients = coefficients

    def __call__(self, value):
        result = 0
        for i, coefficient in enumerate(self.coefficients):
            result += coefficient * (value ** i)
        return result

    def derivative(self):
        new_coefficients = []
        for i, coefficient in enumerate(self.coefficients):
            new_coefficients.append(i * coefficient)
        new_coefficients = new_coefficients[1:]

        return Polynomial(*new_coefficients)

    def __str__(self):
        strs = []
        for i, coefficient in enumerate(self.coefficients):
            if coefficient == 0:
                continue
            elif coefficient < 0:
                coefficient = f"({coefficient})"

            if i == 0:
                strs.append(f"{coefficient}")
            elif i == 1:
                strs.append(f"{coefficient} * (x)")
            else:
                strs.append(f"{coefficient} * (x) ^ {i}")
        return " + ".join(strs)