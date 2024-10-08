import random
from Crypto.Util import number
from sympy import primefactors
from mapping import *
import numpy as np
import multiprocessing
def run(processList):
    for process in processList:
        process.start()
    for process in processList:
        process.join()

def main():
    # Initialize the hash table
    print("system setup")
    m = 800  #vector b
    n= 100
    q = 2 ** 6
    A = np.random.randint(1, q, size=(m, n))
    N = 2   #client
    lambda_val = 60  # 假设的安全参数 λ
    s = Do()

    # 创建一个进程列表
    processList = []
    for i in range(N):
        node = Node(i + 1)
        process = multiprocessing.Process(target=s.DO, args=(m,A,lambda_val,node))
        processList.append(process)

    # 运行所有进程
    run(processList)


# start = time.perf_counter()  # 返回系统运行时间
# end = time.perf_counter()
# print('用时：{:.5f}s'.format(end - start))

if __name__ == '__main__':
    main()