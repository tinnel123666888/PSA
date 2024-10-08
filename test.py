'''import numpy as np

class SampleAlignment:
    def __init__(self, A, s_sum, lambda_val, N):
        self.A = np.array(A)
        self.s_sum = np.array(s_sum)
        self.lambda_val = lambda_val
        self.N = N

    def g(self, x):
        if x == 1:
            return np.random.randint(0, 2 ** (self.lambda_val - int(np.log2(self.lambda_val) ** 2) - int(np.log2(self.N))))
        else:
            return np.random.randint(0, 2 ** self.lambda_val)

    def g_prime(self, x):
        upper_bound = 2 ** (int(np.log2(self.N)) + self.lambda_val - int(np.log2(self.lambda_val) ** 2))
        return 1 if 0 <= x < upper_bound else 0

    def sample_index_generation(self, bit_vectors):
        encoded_vectors = np.array([[self.g(b) for b in bit_vector] for bit_vector in bit_vectors])
        summed_indices = np.sum(encoded_vectors, axis=0)
        return [self.g_prime(x) for x in summed_indices]

# 构建示例数据
A = [
    [12, 39, 20, 6, 3],
    [8, 41, 47, 13, 16],
    [17, 35, 12, 44, 42],
    [18, 7, 29, 12, 51],
    [22, 12, 47, 38, 51]
]
s_sum = [1, 1, 1, 1, 1]
lambda_val = 60
N = 3

# 创建样本对齐对象
alignment = SampleAlignment(A, s_sum, lambda_val, N)

# 构建比特向量
bit_vectors = [
    [1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

# 执行样本索引生成
results = alignment.sample_index_generation(bit_vectors)
print(f"Encoded and summed indices: {results}")

# 输出中间过程
encoded_vectors = np.array([[alignment.g(b) for b in bit_vector] for bit_vector in bit_vectors])
summed_indices = np.sum(encoded_vectors, axis=0)
print(f"Encoded vectors:\n{encoded_vectors}")
print(f"Summed indices: {summed_indices}")
results = [alignment.g_prime(x) for x in summed_indices]
print(results)'''


import random
import numpy as np
import time
'''si = np.random.randint(0,101, size=50)
print(si.tolist())'''
c1=[1, 2, 3, 4, 5]
c2=[1, 2, 3, 4, 5]
c3=[1, 2, 3, 4, 5]
c=[c1,c2,c3]
print(c)



