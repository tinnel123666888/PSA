from Crypto.Util import number
import requests
import json
import time
import sys
import csv
import numpy as np

class lwe:
    def __init__(self):
        '''self.A = np.array([
            [12, 39, 20, 6, 3],
            [8, 41, 47, 13, 16],
            [17, 35, 12, 44, 42],
            [18, 7, 29, 12, 51],
            [22, 12, 47, 38, 51]
        ])'''
        self.m=800
        self.n=100
        self.s_sum = np.array([58, 12, 91, 78, 9, 5, 12, 48, 87, 36, 21, 94, 73, 38, 72, 12, 13, 95, 24, 67, 97, 7, 82, 15, 67, 93, 76, 48, 16, 8, 88, 76, 92, 19, 94, 91, 30, 73, 9, 68, 89, 19, 2, 93, 73, 15, 59, 29, 41, 19, 85, 84, 9, 13, 53, 97, 16, 13, 72, 89, 58, 34, 50, 97, 82, 0, 71, 85, 89, 94, 43, 58, 69, 76, 8, 22, 64, 66, 100, 61, 0, 32, 29, 35, 32, 84, 57, 63, 51, 37, 52, 77, 44, 2, 55, 90, 25, 23, 51, 71])
        self.lambda_val = 60
        self.N = 2
        self.A = np.random.randint(1, 2 ** 6, size=(self.m, self.n))
    def g_prime(self, x, lambda_val, N):
        upper_bound = 2 ** (int(np.log2(N)) + lambda_val - int(np.log2(lambda_val) ** 2))
        if x in range(upper_bound):
            return 1
        else:
            return 0

    def column_sums(self, matrix):

        array = np.array(matrix)
        c_sum = np.sum(array, axis=0)
        d_sum = c_sum - np.dot(self.A, self.s_sum)
        d_sum1 = d_sum.tolist()
        results = [self.g_prime(x, self.lambda_val, self.N) for x in d_sum1]
        return results

if __name__ == "__main__":
    l = lwe()
    c1=[]
    c2=[]
    c3=[]
    start = time.perf_counter()
    result = l.column_sums([c1,c2,c3])
    end = time.perf_counter()
    print('用时：{:.5f}s'.format(end - start))
    #print(result)

