from scipy.constants import hbar
from dataclasses import dataclass

@dataclass
class PhysicalConstant:
    value: float
    unit: str

    def __call__(self):
        return self.value

    def __mul__(self, other):
        if type(other) is PhysicalConstant:
            if other.unit:
                return self.value * other.value, f'{self.unit}*{other.unit}'
            else:
                return self.value * other.value, f'{self.unit}'
        elif isinstance(other, float):
            return PhysicalConstant(self.value * other, self.unit)
        else:
            return PhysicalConstant(self.value * float(other), self.unit)

    def multiply_by(self, number):
        if isinstance(number, float):
            return PhysicalConstant(self.value * number, self.unit)
        else:
            return PhysicalConstant(self.value * float(number), self.unit)

    def __add__(self, other):
        if self.unit == other.unit:
            return PhysicalConstant(self.value + other.value, self.unit)
        else:
            raise Exception("the values of physical constants are different\n",
                            str(self), '\n', str(other))

    def __str__(self):
        return f'value: {self.value}, unit: {self.unit}'

class PhysicalConstantOperations:
    @staticmethod
    def multiply_by(a, b):
        if isinstance(b, float):
            return PhysicalConstant(a.value * b, a.unit)
        else:
            return PhysicalConstant(a.value * float(b), a.unit)

    @staticmethod
    def divide_by(c, d):
        if isinstance(d, float):
            return PhysicalConstant(c.value / d, c.unit)
        else:
            return PhysicalConstant(c.value / float(d), c.unit)



DIRAC_CONSTANT = PhysicalConstant(float(6.58212e-16), 'eV*s')   # reduced planck constant
ELECTRON_MASS = PhysicalConstant(float(0.510999), 'MeV*s')      # electron mass
LIGHT_SPEED = PhysicalConstant(float(299792458), 'm/s')

t1 = PhysicalConstant(1.5, 't')
t2 = PhysicalConstant(2.2, 't')
t3= PhysicalConstantOperations.multiply_by(t1, 15)
t4 = t2+t2
print(t4)