import math
from sin_cos import Sin, Cos
from polynomial import Polynomial

sin = Sin()
cos = Cos()
tg = sin / cos
print(tg(math.pi / 4))  # 1.0
tg_ = tg.derivative() # ((cos(x) * cos(x)) - (sin(x) * ((-1) * sin(x)))) / (cos(x) * cos(x))
print(tg_)
print(tg_(math.pi / 4))  # 2.0

x_2 = Polynomial(0, 0, 1)  # 0*1 + 0*x + 1*x^2
print(x_2(12))  # 144

sin_2 = x_2.apply(sin)
print(sin_2)
print(sin_2(3 * math.pi / 2))  # 1.0
cos_x_2 = cos.apply(x_2)  
print(cos_x_2)
print(cos_x_2(-math.sqrt(math.pi)))  # -1.0

