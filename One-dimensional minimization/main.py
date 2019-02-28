import matplotlib.pyplot as plt
from numpy import array, arange

from function import f0, f1
from golden_section import *
from hord import *
from method_of_dichotomy import *
from middle_point import *
from Nyuton import *

x = arange(-4, 4, 0.1)
y = array(list(map(f0, x)))
plt.plot(x, y)
plt.show()

print(method_of_dichotomy(-4, 4, 10**-5, 10**-4))
print(golden_section(-4, 4, 10**-5))

x = arange(1, 5, 0.1)
y = array(list(map(f1, x)))
plt.plot(x, y)
plt.show()

print(middle_point(2, 4, 10**-4))
print(hord(2, 4, 10**-4))

print(Nyuton(2, 10**-4))