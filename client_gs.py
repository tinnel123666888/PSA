
import csv
import hashlib
import json
import requests
from datetime import datetime
import time
from secrets import randbelow
from multiprocessing import Process
from node import *
import sys
import random
import numpy as np
class SampleIntersectionSizeEvaluation:

    def start(self,z,ell,A,m,node):
        print('Start Owner {0}.'.format(node.id))

        def hash_function_k_ell(x):
            """哈希函数 h_k,ℓ 用于生成哈希值。"""
            hash_obj =  hashlib.sha256()
            hash_obj.update(x.encode('utf-8'))
            return int(hash_obj.hexdigest(), 16) % (2 ** ell)

        def collision_resistant_hash(X_j):
            """普通的哈希映射函数。如果有映射值则为1，否则为0，返回列表长度为m。"""
            hash_map = np.zeros(m, dtype=int)
            for x in X_j:
                hash_index = hash_function_k_ell(str(x)) % m
                hash_map[hash_index] = 1
            return hash_map

        def evaluate(Sam,s):
            """执行样本交集大小评估协议。"""
            v_list = []

            for j in range(1, z + 1):
                h_j = lambda x: hash_function_k_ell(str(x))  # 确保输入是字符串
                y_j = np.random.randint(0, 2 ** 16)  # 生成一个整数而不是一个数组
                #print(y_j)
                X_j = {x for x in Sam if h_j(str(x)) == y_j}  # 确保输入是字符串
                #print(X_j)
                u_j = collision_resistant_hash(X_j)
                #print(u_j)
                v_j = np.dot(A, s)[:m] + u_j  # 确保结果维度匹配
                #print(v_j)
                v_j = v_j.tolist()
                v_list.append(v_j)
            return v_list

        if (node.id == 1):
            # 打开文件以读取模式
            with open('psi_1.csv', 'r') as file:
                reader = csv.reader(file, delimiter='\n')
                Sam = []  # 创建一个空列表以存储读取的整数
                for row in reader:
                    Sam.extend(list(map(int, row[0].split(','))))  # 将读取的字符串转换为整数并扩展到列表中
        elif (node.id == 2):
            with open('psi_2.csv', 'r') as file:
                reader = csv.reader(file, delimiter='\n')
                Sam = []  # 创建一个空列表以存储读取的整数
                for row in reader:
                    Sam.extend(list(map(int, row[0].split(','))))  # 将读取的字符串转换为整数并扩展到列表中

        elif (node.id == 3):
            with open('psi_3.csv', 'r') as file:
                reader = csv.reader(file, delimiter='\n')
                Sam = []  # 创建一个空列表以存储读取的整数
                for row in reader:
                    Sam.extend(list(map(int, row[0].split(','))))  # 将读取的字符串转换为整数并扩展到列表中

        elif (node.id == 4):
            with open('psi_4.csv', 'r') as file:
                reader = csv.reader(file, delimiter='\n')
                Sam = []  # 创建一个空列表以存储读取的整数
                for row in reader:
                    Sam.extend(list(map(int, row[0].split(','))))  # 将读取的字符串转换为整数并扩展到列表中
        '''if (node.id == 1):
                    s = [17, 60, 49, 79, 67]
                elif (node.id == 2):
                    s = [27, 60, 49, 79, 67]
                elif (node.id == 3):
                    s = [37, 60, 49, 79, 67]
                elif (node.id == 4):
                    s = [47, 60, 49, 79, 67]'''
        s = [34, 63, 21, 56, 62, 53, 40, 51, 100, 64, 43, 32, 33, 96, 1, 13, 61, 50, 26, 72, 13, 98, 44, 60, 40, 30, 8, 98,
         9, 15, 98, 37, 88, 27, 81, 46, 21, 36, 57, 63, 20, 100, 36, 72, 100, 11, 75, 24, 90, 54, 88, 69, 64, 87, 24,
         72, 73, 94, 49, 86, 71, 62, 71, 5, 37, 92, 52, 79, 91, 53, 46, 37, 97, 53, 25, 100, 99, 92, 49, 23, 26, 30, 15,
         63, 18, 66, 11, 47, 88, 61, 88, 55, 56, 38, 51, 66, 35, 98, 27, 91]
        #start = time.perf_counter()  # 返回系统运行时间
        v_list=evaluate(Sam,s)
        #end = time.perf_counter()
        #print('用时：{:.5f}s'.format(end - start))
        '''print("--")
        print(v_list)
        # 计算所占的字节数
        size_in_bytes = sys.getsizeof(v_list)
        # 转换为KB
        size_in_kb = size_in_bytes / 1024
        print(f"The size of the list 'c' in KB is: {size_in_kb:.2f} KB")'''
        current_time = datetime.now()

        # 格式化时间并包括毫秒
        formatted_time = current_time.strftime("%H:%M:%S") + f".{current_time.microsecond // 1000:03d}"

        # 输出格式化后的时间
        print("当前时间是：", formatted_time)
        data = json.dumps(v_list)
        url = "http://172.24.122.104:8000/lwe"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data, headers=headers)
        print(x.content)



