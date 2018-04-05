def intersect_two_sorted_arrays(A, B):
    return [a for i, a in enumerate(A) if (i == 0 or a != A[i - 1]) and a in B]


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
