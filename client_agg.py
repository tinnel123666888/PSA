import random
import numpy as np
import csv
import json
import requests
class Client:
    def __init__(self):
        self.n = 400
        self.N = 2
        self.t = 2  # 阈值参数
        self.q = 101  # 素数作为模数
        self.fixed_id=1
        self.si=[6, 80, 46, 49, 66, 18, 31, 24, 78, 48, 93, 14, 37, 67, 39, 87, 40, 88, 91, 20, 48, 67, 88, 28, 36, 83, 22, 22, 43, 0, 79, 100, 11, 1, 79, 75, 73, 33, 37, 31, 91, 65, 9, 99, 1, 66, 79, 57, 44, 64, 94, 28, 82, 35, 76, 30, 20, 51, 42, 60, 62, 4, 41, 52, 63, 85, 56, 12, 69, 69, 82, 77, 18, 48, 14, 18, 68, 38, 24, 89, 97, 27, 2, 78, 20, 69, 3, 52, 89, 23, 80, 96, 94, 94, 41, 71, 89, 50, 55, 25, 78, 15, 41, 67, 63, 76, 56, 75, 92, 11, 28, 0, 91, 73, 68, 39, 21, 3, 49, 64, 77, 64, 18, 46, 97, 36, 65, 5, 50, 4, 8, 54, 54, 99, 98, 94, 20, 58, 47, 68, 1, 86, 33, 72, 39, 76, 25, 68, 7, 20, 67, 90, 86, 32, 42, 6, 30, 78, 47, 90, 77, 8, 67, 33, 65, 54, 86, 7, 99, 52, 12, 33, 0, 17, 75, 32, 51, 77, 8, 43, 98, 57, 37, 96, 1, 10, 74, 25, 2, 94, 26, 7, 66, 96, 8, 45, 47, 94, 58, 91, 66, 22, 66, 74, 87, 70, 88, 76, 82, 23, 24, 27, 66, 29, 95, 16, 94, 43, 66, 9, 86, 84, 30, 58, 67, 22, 45, 26, 63, 79, 69, 48, 51, 71, 33, 49, 94, 97, 95, 25, 69, 61, 40, 90, 90, 24, 8, 25, 21, 5, 68, 52, 81, 16, 86, 78, 89, 93, 64, 3, 81, 81, 8, 96, 69, 15, 93, 91, 71, 11, 22, 19, 56, 73, 61, 93, 100, 97, 22, 60, 89, 71, 86, 30, 95, 92, 62, 27, 56, 98, 7, 55, 97, 63, 73, 20, 66, 33, 47, 81, 68, 9, 42, 62, 25, 53, 87, 11, 9, 43, 60, 17, 6, 79, 67, 51, 75, 25, 44, 41, 10, 47, 16, 63, 8, 73, 48, 3, 80, 63, 80, 72, 44, 65, 57, 2, 61, 34, 81, 82, 100, 95, 22, 5, 33, 80, 43, 67, 86, 10, 55, 7, 74, 95, 62, 14, 1, 38, 19, 42, 0, 91, 7, 0, 0, 51, 12, 94, 0, 3, 29, 58, 53, 8, 10, 99, 94, 49, 10, 30, 77, 95, 45, 50, 28, 23, 93, 35, 82, 1, 99, 76, 84, 57, 13, 36, 38, 41, 7, 35]
    def process_shares(self, organized_shares):
        # 获取嵌套列表的长度
        length = len(organized_shares[0])

        # 初始化结果列表
        result = []

        # 对每个位置计算和
        for i in range(length):
            sum_value = sum(client_shares[i] for client_shares in organized_shares)
            result.append((self.fixed_id, sum_value))

        return result

    def polynomial_coefficients(self, secret, k, q):
        # 生成一个多项式，secret 是常数项，k 是阈值
        coeffs = [secret] + [random.randint(0, q - 1) for _ in range(k - 1)]
        return coeffs

    def evaluate_polynomial(self, coeffs, x, q):
        # 计算多项式在点 x 的值
        return sum([coeff * (x ** i) for i, coeff in enumerate(coeffs)]) % q

    def shamir_split(self, secret, N, k, q):
        # 生成多项式并计算 N 个分片
        coeffs = self.polynomial_coefficients(secret, k, q)
        shares = [(i, self.evaluate_polynomial(coeffs, i, q)) for i in range(1, N + 1)]
        return shares

    def client_side(self):
        #si = np.random.randint(0, self.q, size=self.n)
        # 打开一个文件以写入模式
        shares = [self.shamir_split(s, self.N, self.t, self.q) for s in self.si]
        return shares

    def organize_shares(self, shares):
        organized_shares = {i: [] for i in range(1, self.N+1)}
        for share_set in shares:
            for share in share_set:
                organized_shares[share[0]].append(share[1])
        return organized_shares

    def convert_numpy_types(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, dict):
            return {self.convert_numpy_types(key): self.convert_numpy_types(value) for key, value in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [self.convert_numpy_types(element) for element in obj]
        return obj

if __name__ == "__main__":
    #no_id=1
    client = Client()

    #第一步分片生成
    shares = client.client_side()
    organized_shares = client.organize_shares(shares)
    #enc_shares={}
    #enc_shares[no_id]=organized_shares
    print("分片:", shares)
    print("组织后的分片:", organized_shares)
    #print(enc_shares)


    # 转换 numpy 数据类型
    #organized_shares = client.convert_numpy_types(organized_shares)
    data = json.dumps(organized_shares)
    '''data_size = len(data.encode('utf-8'))
    print(f"Request data size: {data_size} bytes")

    # 请求头部大小
    headers = {
        "User-Agent": "123"
    }

    headers_size = sum(len(k) + len(v) + 4 for k, v in headers.items())
    default_headers = {
        "Host": "172.24.122.104:8000",
        "Content-Length": str(data_size),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    headers_size += sum(len(k) + len(v) + 4 for k, v in default_headers.items())
    headers_size += 2
    print(f"Request headers size: {headers_size} bytes")
    print(f"Total communication size: {data_size+headers_size} bytes")'''
    url = "http://172.24.122.104:8000/server"
    headers = {
        "User-Agent": "123"
    }
    x = requests.post(url=url, data=data, headers=headers)
    print(x.content)


    '''#示例接收的数据
    organized_shares = [[50, 89, 5, 3, 33], [77, 39, 41, 51, 16], [23, 7, 42, 69, 10]]

    # 处理数据
    processed_shares = client.process_shares(organized_shares)

    print("处理后的分片:", processed_shares)'''