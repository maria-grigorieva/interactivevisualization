import normalize
import numpy as np


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def run_test(test):
    calc = normalize.NormalizeData()
    result = calc.perform(test[0], test[1])
    assert result == test[2]
    if (result):
        for i in range(len(test[3])):
            for j in range(len(test[3][i])):
                if not isclose(test[3][i][j], test[3][i][j]):
                    return False
    return True


def run_normalize_test():
    testset = [[np.array([[1, 2, 3, 4], [5, 4, 10, 2], [0, 0, 0, 3], [1, 1, 1, 0]]),
                [[2, 3, 4]],
                False,
                np.array([[0.2, 0.5, 0.3, 1], [1, 1, 1, 0.5], [0, 0, 0, 0.75], [0.2, 0.25, 0.1, 0]])],
               [[1, 2, 3],
                [[2, 3, 4]],
                False,
                None],
               [np.array([[1, 2, 3, 4], [5, 4, 10, 2], [0, 0, 0, 3], [1, 1, 1, 0]]),
                [[1, 2, 3, 4], [1, 2, 3]],
                False,
                np.array([[0.2, 0.5, 0.3, 1], [1, 1, 1, 0.5], [0, 0, 0, 0.75], [0.2, 0.25, 0.1, 0]])],
               [np.array([[1, 2, 3, 4], [5, 4, 10, 2], [0, 0, 0, 3], [1, 1, 1, 0]]),
                [],
                True,
                np.array([[0.2, 0.5, 0.3, 1], [1, 1, 1, 0.5], [0, 0, 0, 0.75], [0.2, 0.25, 0.1, 0]])],
               [np.array([[1, 2, 3, 4], [5, 4, 10, 2], [0, 0, 0, 3], [1, 1, 1, 0]]),
                [[10] * 4],
                True,
                np.array([[2, 5, 3, 10], [10, 10, 10, 5], [0, 0, 0, 7.5], [2, 2.5, 1, 0]])],
               [np.array([[1, 2, 3, 4], [5, 4, 10, 2], [0, 0, 0, 3], [1, 1, 1, 0]]),
                [[10] * 4, [20] * 4],
                True,
                np.array([[12, 15, 13, 20], [20, 20, 20, 15], [10, 10, 10, 17.5], [12, 12.5, 11, 10]])],
               [np.array([[1, 2, 3, 4], [5, 4, 10, 2], [0, 0, 0, 3], [1, 1, 1, 0]]),
                [[10, 10, 0, 0], [20, 20, 10, 10]],
                True,
                np.array([[12, 15, 3, 10], [20, 20, 10, 5], [10, 10, 0, 7.5], [12, 12.5, 1, 0]])]]
    print("Testing normalize data class:")
    for i in range(len(testset)):
        print(f"Data set number {i}")
        assert run_test(testset[i])
        print("passed")
    print("Test was passed successfully")
