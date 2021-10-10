from sympy import *
a, m, h, x, t = symbols('a m h x t', real=True)



# phi_x = exp(-x**2)
# a = phi_x.subs(x, 2)
# print(a)
# print(a.evalf())



phi_x_t = exp((-x**2)+I*t)
c_phi_x_t = conjugate(phi_x_t)
phi_o = c_phi_x_t*phi_x_t
pprint(phi_o)
x = phi_o.subs([(x, 1), (t, 8)])
print(x.evalf())

#
# b = plot(phi_o, (x, -4, 4), show=False)
# b.show()