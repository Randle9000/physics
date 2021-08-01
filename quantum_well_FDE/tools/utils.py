from numpy import eye, diag, ones

def derivative_matrix_generator(number_of_elements, order=2):
    if order in [2, 'second']:
        DX2 = eye(number_of_elements) * (-2)
        DX2 = DX2 + diag(ones(number_of_elements - abs(1)), -1)
        DX2 = DX2 + diag(ones(number_of_elements - abs(1)), 1)
        return DX2

# def add_efective_mass_effect(qw_matrix, efective_mass_value, start_end_of_effective_mass_places=[]):
#     start_of_effective_mass = start_end_of_effective_mass_places[0]
#     end_of_effective_mass = start_end_of_effective_mass_places[1]
#
#     qw_matrix[:int(start_of_effective_mass)] *= efective_mass_value

def potential_matrix_generator(barrier, size_of_qw_matrix, part_without_barrier=[]):
    n = size_of_qw_matrix
    start_of_potential = part_without_barrier[0]
    end_of_potential = part_without_barrier[1]

    VB = ones(n)
    VB[0:int(start_of_potential)] = barrier
    VB[int(start_of_potential) + 1: int(end_of_potential)] = 0
    VB[int(end_of_potential) + 1:n] = barrier
    return VB


def sort_eigenvalues_and_eigenvectors(eigenValues, eigenVectors):
    idx = eigenValues.argsort()[::1]
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:, idx]
    return eigenValues,eigenVectors