import statistics
import pandas as pd


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def run_test(test):
    calc = statistics.BasicStatistics()
    result = calc.perform(test[0], test[1])
    for i in range(len(result)):
        for j in range(len(result[i])):
            if not isclose(result[i][j], test[2][i][j]):
                return False
    return True


def run_calculationbasis_test():
    testset = [[pd.DataFrame([[1, 2, 3, 4], [4, 3, 2, 1], [-1, -2, -3, -4], [0, 0, 0, 0], [0, 0, 0, 0]]),
                [],
                [[4, 3, 3, 4], [-1, -2, -3, -4], [4, 3, 2, 1],
                 [0.8, 0.6, 0.4, 0.2]]],
               [pd.DataFrame([[1, 2, 3, 4], [4, 3, 2, 1]]),
                [],
                [[4, 3, 3, 4], [1, 2, 2, 1], [5, 5, 5, 5],
                 [2.5, 2.5, 2.5, 2.5]]]]

    for i in range(len(testset)):
        assert run_test(testset[i])
