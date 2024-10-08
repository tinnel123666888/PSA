import random
from Crypto.Util import number
from sympy import primefactors
from mapping import *
import numpy as np
import hashlib
import multiprocessing
from client_gs import *
def run(processList):
    for process in processList:
        process.start()
    for process in processList:
        process.join()

def main():
    print("system setup")
    z = 20
    ell = 6
    m = 800
    N=2
    n=100
    q = 2 ** 6
    A = np.random.randint(1, q, size=(m, n))
    s = SampleIntersectionSizeEvaluation()

    # 创建一个进程列表
    processList = []
    for i in range(N):
        node = Node(i + 1)
        process = multiprocessing.Process(target=s.start, args=(z,ell,A,m,node))
        processList.append(process)

    # 运行所有进程
    run(processList)


if __name__ == '__main__':
    main()