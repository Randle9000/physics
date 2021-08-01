from scimath.units.api import UnitScalar
from scimath.units.length import nm
from scimath.units.energy import meV
from physical_constants import ELECTRON_MASS_meV
v_barrier = UnitScalar(267.5, units=meV)
l = UnitScalar(1.0, units=nm)
l_barrier = 5*l
l_well = 15*l

m_w = 0.067
m_b = 0.094

"""
in energy.py of scimath added meV
"""