from flask import Flask, request, jsonify
import json
import time
import requests
from client_agg import *
import csv

app = Flask(__name__)
@app.route('/client1', methods=['POST'])
def client1():
    data1 = request.get_data()
    json_str = data1.decode('utf-8')
    data = json.loads(json_str)
    print("解析后的数据:", data)  # 打印解析后的数据
    client = Client()
    start = time.perf_counter()
    processed_shares = client.process_shares(data)
    end = time.perf_counter()
    print('用时：{:.5f}s'.format(end - start))
    print("处理后的分片:", processed_shares)

    datas= json.dumps(processed_shares)
    url = "http://172.24.122.104:8000/server1"
    headers = {
        "User-Agent": "123"
    }
    x = requests.post(url=url, data=datas, headers=headers)
    print(x.content)

    return 'ok'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)