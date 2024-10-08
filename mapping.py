import csv
import json
import requests
import time
from secrets import randbelow
from multiprocessing import Process
from node import *
import sys
import random
import numpy as np
class Do:

    def DO(self,m,A,lambda_val,node):
        print('Start Owner {0}.'.format(node.id))
        hash_table = [None] * m
        for i in range(0, m):
            random_value = random.randint(2, 100)
            hash_table[i] = 0

        # Define the hash function
        def hash_function(data, size):
            hash_value = hash(data) % size
            return hash_value

        def g(x, lambda_val, N):
            if x == 1:
                return np.random.randint(0, 2 ** (lambda_val - int(np.log2(lambda_val) ** 2) - int(np.log2(N))))
            else:
                return np.random.randint(0, 2 ** lambda_val)

        def encode_b_to_d(b, lambda_val):
            d = []
            N = len(b)  # 获取列表 b 的长度，用于计算安全参数
            for bi in b:
                di = g(bi, lambda_val, N)
                d.append(di)
            return d

        # Read data from file
        if (node.id==1):
            with open('psi_1.csv', 'r') as file:
                reader = csv.reader(file, delimiter='\n')
                for line in reader:
                    # data = line.strip()
                    index = hash_function(''.join(line), m)
                    # print(index)
                    hash_table[index] = 1
        elif(node.id==2):
            with open('psi_2.csv', 'r') as file:
                reader = csv.reader(file, delimiter='\n')
                for line in reader:
                    # data = line.strip()
                    index = hash_function(''.join(line), m)
                    # print(index)
                    hash_table[index] = 1
        elif(node.id==3):
            with open('psi_3.csv', 'r') as file:
                reader = csv.reader(file, delimiter='\n')
                for line in reader:
                    # data = line.strip()
                    index = hash_function(''.join(line), m)
                    # print(index)
                    hash_table[index] = 1
        elif (node.id == 4):
            with open('psi_4.csv', 'r') as file:
                reader = csv.reader(file, delimiter='\n')
                for line in reader:
                    # data = line.strip()
                    index = hash_function(''.join(line), m)
                    # print(index)
                    hash_table[index] = 1

        #
        '''if (node.id == 1):
            s= [52, 47, 4, 39, 10, 94, 29, 53, 47, 58, 63, 35, 34, 32, 76, 5, 88, 64, 82, 78, 89, 87, 48, 32, 92, 34, 17, 3, 100, 85, 13, 52, 100, 6, 45, 90, 40, 17, 29, 83, 55, 97, 23, 97, 31, 100, 23, 35, 76, 11]
        elif (node.id == 2):
            s = [52, 47, 4, 39, 10, 94, 29, 53, 47, 58, 63, 35, 34, 32, 76, 5, 88, 64, 82, 78, 89, 87, 48, 32, 92, 34, 17, 3, 100, 85, 13, 52, 100, 6, 45, 90, 40, 17, 29, 83, 55, 97, 23, 97, 31, 100, 23, 35, 76, 11]
        elif (node.id == 3):
            s = [52, 47, 4, 39, 10, 94, 29, 53, 47, 58, 63, 35, 34, 32, 76, 5, 88, 64, 82, 78, 89, 87, 48, 32, 92, 34, 17, 3, 100, 85, 13, 52, 100, 6, 45, 90, 40, 17, 29, 83, 55, 97, 23, 97, 31, 100, 23, 35, 76, 11]
        elif (node.id == 4):
            s = [52, 47, 4, 39, 10, 94, 29, 53, 47, 58, 63, 35, 34, 32, 76, 5, 88, 64, 82, 78, 89, 87, 48, 32, 92, 34, 17, 3, 100, 85, 13, 52, 100, 6, 45, 90, 40, 17, 29, 83, 55, 97, 23, 97, 31, 100, 23, 35, 76, 11]
        '''
        s=[34, 63, 21, 56, 62, 53, 40, 51, 100, 64, 43, 32, 33, 96, 1, 13, 61, 50, 26, 72, 13, 98, 44, 60, 40, 30, 8, 98, 9, 15, 98, 37, 88, 27, 81, 46, 21, 36, 57, 63, 20, 100, 36, 72, 100, 11, 75, 24, 90, 54, 88, 69, 64, 87, 24, 72, 73, 94, 49, 86, 71, 62, 71, 5, 37, 92, 52, 79, 91, 53, 46, 37, 97, 53, 25, 100, 99, 92, 49, 23, 26, 30, 15, 63, 18, 66, 11, 47, 88, 61, 88, 55, 56, 38, 51, 66, 35, 98, 27, 91]
        start = time.perf_counter()
        #lambda_val = 60  # 假设的安全参数 λ
        d = encode_b_to_d(hash_table, lambda_val)
        d = np.array(d)
        s= np.array(s)
        c= np.dot(A, s) + d
        end = time.perf_counter()
        print('用时：{:.5f}s'.format(end - start))

        '''print("公共矩阵 A:")
        print(A)
        print("\n随机向量 si:")
        print(s)
        print("\n向量 di:")
        print(d)
        print("\n加密样本索引 ci:")
        print(c)'''
        c1 = c.tolist()
        data = json.dumps(c1)
        url = "http://172.24.122.105:8000/lwe"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data, headers=headers)
        print(x.content)
        #print(c1)
        '''# 计算所占的字节数
        size_in_bytes = sys.getsizeof(c1)
        # 转换为KB
        size_in_kb = size_in_bytes / 1024
        print(f"The size of the list 'c' in KB is: {size_in_kb:.2f} KB")'''
        #start = time.perf_counter()
        #end = time.perf_counter()
        #print('用时：{:.5f}s'.format(end - start))