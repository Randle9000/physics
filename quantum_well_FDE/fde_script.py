from numpy import ceil, round, eye, diag, ones, full, linalg, sort
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt

from physical_constants import *
from config import l, l_well, l_barrier, v_barrier, m_b, m_w
from tools.utils import derivative_matrix_generator, potential_matrix_generator, sort_eigenvalues_and_eigenvectors

#TODO print steps! it helps a lot we then know what's going on!
#resolution
#TODO figure it out!
dx = l/10

# qw length
s_x = l_well+2*l_barrier
Nx = ceil(s_x/dx)
s_x = Nx*dx

nx = round(l_well/dx)
nx1 = round((Nx - nx)/2)
nx2 = nx + nx1
Nx = int(Nx)


""" second derivative matrix """
DX2 = derivative_matrix_generator(Nx, 2)
DX2 = DX2 * SCHRODINGER_LAPLACE_PART_CONSTANT.item()
DX2 = csr_matrix(DX2)               # sparse DX2 matrix
DX2 = (-1*DX2/(dx**2))              # TODO is it integral part of derivative matrix generator?

# add effective masses
DX2[:int(nx1)] /= m_b
DX2[int(nx1)+1: int(nx2)] /= m_w
DX2[int(nx2)+1: int(Nx)] /= m_b


# barrier
VB = potential_matrix_generator(v_barrier, Nx, [nx1, nx2])
VB = csr_matrix(diag(VB))

#wektor falowy
K = eye(Nx) * (1)
K = K * SCHRODINGER_LAPLACE_PART_CONSTANT.item()
K = csr_matrix(K)

#Full equation
first_eigenvalues = []
second = []
third = []
for k in range(0, 25, 1):
    A = DX2 + VB + K * (k*0.1)**2
    A = csr_matrix.todense(A)
    eigenValues, eigenVectors = linalg.eig(A) #dziala
    eigenValues, eigenVectors = sort_eigenvalues_and_eigenvectors(eigenValues, eigenVectors)
    first_eigenvalues.append(eigenValues[0])
    second.append(eigenValues[1])
    third.append(eigenValues[2])

a = first_eigenvalues
x = range(0, len(a), 1)
# y = [a[n, 1] for n in range(eigenVectors[0].size)]
fig, ax = plt.subplots()
ax.plot(x, a)
ax.plot(x,second)
ax.plot(x,third)
fig.savefig("test.png")
plt.show()
print('end')

# plot
# x = range(0, eigenVectors[0].size, 1)
# y = [eigenVectors[n, 1] for n in range(eigenVectors[0].size)]
# fig, ax = plt.subplots()
# ax.plot(x, y)
# fig.savefig("test.png")
# plt.show()
# print(eigenValues[0])