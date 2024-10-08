from flask import Flask, request, jsonify
import json
import time
import requests
from server_agg import *
from datetime import datetime
import csv

app = Flask(__name__)

shares1= []
count1 = 0
def combine1(data):
    global count1
    global shares1
    count1 += 1
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)
    l=len(data_dict)
    shares1.append(data_dict)
    print(shares1)
    if count1 == 2:
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


@app.route('/server1', methods=['POST'])
def server1():
    data = request.get_data()
    combine1(data)
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8100)