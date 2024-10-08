from flask import Flask, request, jsonify
import json
import time
import requests
from server_lew import *
from datetime import datetime
import csv

app = Flask(__name__)

shares = []
count = 0

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
        t = lwe()
        start = time.perf_counter()
        combined_shares =t.column_sums(shares)
        end = time.perf_counter()
        print('用时：{:.5f}s'.format(end - start))
        print(combined_shares)



@app.route('/lwe', methods=['POST'])
def lwe():
    data = request.get_data()
    combine(data)
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8100)