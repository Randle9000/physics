from scimath.units.api import UnitScalar
from scimath.units.SI import milli
from scimath.units.energy import MeV, eV, meV
from scimath.units.time import s
from scimath.units.length import m, nm

LIGHT_SPEED = UnitScalar(299792458, units=m/s)
DIRAC_CONSTANT = UnitScalar(6.58212e-16, units=eV*s)   # reduced planck constant
ELECTRON_MASS = UnitScalar(0.510999, units=MeV)# TODO fix should be Mev/C^2


LIGHT_SPEED_nm = LIGHT_SPEED.as_units(nm/s)
DIRAC_CONSTANT_meV = DIRAC_CONSTANT.as_units(meV*s)
ELECTRON_MASS_meV = ELECTRON_MASS.as_units(meV)/(LIGHT_SPEED_nm*LIGHT_SPEED_nm)

SCHRODINGER_LAPLACE_PART_CONSTANT = DIRAC_CONSTANT_meV*DIRAC_CONSTANT_meV/(2*ELECTRON_MASS_meV)