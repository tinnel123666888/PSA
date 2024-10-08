from flask import Flask, request, jsonify
import json
import time
import requests
from server_agg import *
from datetime import datetime
import csv

app = Flask(__name__)

shares = []
count = 0
shares1= []
count1 = 0

def combine(data):
    global count
    global shares
    count += 1
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)
    shares.append(data_dict)
    print(shares)
    if count == 2:
        # 获取当前时间
        current_time = datetime.now()

        # 格式化时间并包括毫秒
        formatted_time = current_time.strftime("%H:%M:%S") + f".{current_time.microsecond // 1000:03d}"

        # 输出格式化后的时间
        print("当前时间是：", formatted_time)
        t = Server()
        start = time.perf_counter()
        combined_shares =t.combine_client_shares(shares)
        print(combined_shares)
        end = time.perf_counter()
        print('用时：{:.5f}s'.format(end - start))
        client1 = []
        client2 = []
        client3 = []
        client4 = []
        print("组合后的分片:")
        for key, value in combined_shares.items():
            if key == 1:
                client1 = value
            elif key == 2:
                client2 = value
            elif key == 3:
                client3 = value
            else:
                client4 = value
        print(client1)
        print(client2)
        print(client3)
        print(client4)

        data1 = json.dumps(client1)
        url = "http://172.24.122.105:8000/client1"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data1, headers=headers)
        print(x.content)

        data2 = json.dumps(client2)
        url = "http://172.24.122.106:8000/client2"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data2, headers=headers)
        print(x.content)

        '''data3 = json.dumps(client3)
        url = "http://172.24.122.107:8000/client3"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data3, headers=headers)
        print(x.content)

        data4 = json.dumps(client4)
        url = "http://172.24.122.108:8000/client4"
        headers = {
            "User-Agent": "123"
        }
        x = requests.post(url=url, data=data4, headers=headers)
        print(x.content)'''
def combine1(data):
    global count1
    global shares1
    count1 += 1
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)
    l=len(data_dict)
    shares1.append(data_dict)
    print(shares1)
    if count == 2:
        t = Server()
        start = time.perf_counter()
        combined_shares = []
        for i in range(l):
            combined_shares.append([shares1[j][i] for j in range(len(shares1))])
        print(combined_shares)

        reconstructed_vector = []
        for share in combined_shares:
            # 使用全部点进行插值
            y_t = t.recover_secret(share)
            reconstructed_vector.append(y_t)
        print("重构的向量列表:", reconstructed_vector)
        # 获取当前时间
        current_time = datetime.now()

        # 格式化时间并包括毫秒
        formatted_time = current_time.strftime("%H:%M:%S") + f".{current_time.microsecond // 1000:03d}"

        # 输出格式化后的时间
        print("当前时间是：", formatted_time)
        end = time.perf_counter()
        print('用时：{:.5f}s'.format(end - start))


@app.route('/server', methods=['POST'])
def server():
    data = request.get_data()
    combine(data)
    return 'ok'

@app.route('/server1', methods=['POST'])
def server1():
    data = request.get_data()
    combine1(data)
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)