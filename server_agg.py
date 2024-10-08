import random

class Server:
    def __init__(self):
        self.q = 101  # 素数作为模数
        self.t = 2  # 阈值参数

    def modinv(self, a, q):
        # 使用扩展欧几里得算法计算 a 在模 q 下的逆
        def egcd(a, b):
            if a == 0:
                return b, 0, 1
            g, y, x = egcd(b % a, a)
            return g, x - (b // a) * y, y

        g, x, y = egcd(a, q)
        if g != 1:
            raise ValueError('模逆不存在')
        return x % q

    def lagrange_interpolation(self, x, shares, q):
        k = len(shares)
        xs, ys = zip(*shares)
        result = 0
        for i in range(k):
            term = ys[i]
            for j in range(k):
                if i != j:
                    denominator = xs[i] - xs[j]
                    if denominator == 0:
                        continue
                    try:
                        term *= (x - xs[j]) * self.modinv(denominator, q)
                    except ValueError:
                        continue
                    term %= q
            result += term
            result %= q
        return result

    def recover_secret(self, shares):
        """
        使用拉格朗日插值法从 t 个分片中恢复秘密
        :param shares: 分片列表 [(x1, y1), (x2, y2), ...]
        :param t: 阈值
        :param q: 大素数
        :return: 恢复的秘密值
        """
        selected_shares = random.sample(shares, self.t)
        secret = self.lagrange_interpolation(0, selected_shares, self.q)
        return secret

    def combine_client_shares(self, organized_shares_list):
        combined_shares = {1: [], 2: [], 3: [], 4:[]}
        for client_shares in organized_shares_list:
            for key in combined_shares.keys():
                str_key=str(key)
                if str_key in client_shares:
                    combined_shares[key].append(client_shares[str_key])

        return combined_shares

if __name__ == "__main__":
       server = Server()
       #第二步接受处理分片
       client1_shares = {'1': [28, 36, 68, 20, 22], '2': [39, 12, 87, 62, 78], '3': [50, 89, 5, 3, 33]}
       client2_shares = {'1': [6, 27, 100, 93, 69], '2': [92, 33, 20, 72, 93], '3': [77, 39, 41, 51, 16]}
       client3_shares = {'1': [54, 6, 94, 67, 30], '2': [89, 57, 68, 68, 20], '3': [23, 7, 42, 69, 10]}

       organized_shares_list = [client1_shares, client2_shares, client3_shares]
       print(organized_shares_list)
       combined_shares = server.combine_client_shares(organized_shares_list)
       print(combined_shares)
       client1=[]
       client2=[]
       client3=[]
       client4=[]
       print("组合后的分片:")
       for key, value in combined_shares.items():
           if key==1:
               client1 =value
           elif key==2:
               client2 = value
           elif key==3:
               client3 = value
           else:
               client4=value
       print(client1)
       print(client2)
       print(client3)

       '''server = Server()
       # 示例接收的来自3个客户端的点值对
       client1_shares = [(1, 88), (1, 69), (1, 262), (1, 180), (1, 121)]
       client2_shares = [(1, 220), (1, 102), (1, 175), (1, 202), (1, 191)]
       client3_shares = [(1, 150), (1, 135), (1, 88), (1, 123), (1, 59)]

       all_shares = [client1_shares, client2_shares, client3_shares]

       # 将所有客户端的点值对聚合在一起
       combined_shares = []
       for i in range(len(client1_shares)):
           combined_shares.append([all_shares[j][i] for j in range(len(all_shares))])
       print(combined_shares)

       reconstructed_vector = []
       for shares in combined_shares:
           # 使用全部点进行插值
           y_t = server.recover_secret(shares, server.t, server.q)
           reconstructed_vector.append(y_t)

       print("重构的向量列表:", reconstructed_vector)'''
