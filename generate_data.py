# Copyright 2022 Ant Group Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from random import randint
from random import sample
import csv
import sys

class generate:
    def __init__(self):
        self.row_list = []
        self.len1 = 10 ** 2
        self.len2 = 10
        self.len3 = 10
        self.len4 = 10

        if len(sys.argv) > 1:
            self.len1 = int(sys.argv[1])
            self.len2 = int(self.len1/2)
        if len(sys.argv) > 2:
            self.len3 = int(sys.argv[2])

        self.len4 = int(self.len3/2)
        print(self.len1, self.len2,self.len3,self.len4)

    def random_with_N_digits(self,n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)

    def generate_data(self):
        for i in range(self.len1):
            data_list = [self.random_with_N_digits(18)]
            self.row_list.append(data_list)

        row_list2 = sample(self.row_list, self.len2)
        for i in range(self.len2, self.len1):
            data_list = [self.random_with_N_digits(18)]
            row_list2.append(data_list)

        row_list3 = sample(self.row_list, self.len4)
        for i in range(self.len4, self.len3):
            data_list = [self.random_with_N_digits(18)]
            row_list3.append(data_list)
        row_list4 = []
        for i in range(self.len1):
            if self.row_list[i] in row_list2 and self.row_list[i] in row_list3:
                row_list4.append(self.row_list[i])

        print(len(row_list2))
        print(len(row_list3))
        print(len(row_list4))

        with open('psi_1.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            # writer.writerow(["id"])
            writer.writerows(self.row_list)

        with open('psi_2.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            # writer.writerow(["id"])
            writer.writerows(row_list2)

        with open('psi_3.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            # writer.writerow(["id"])
            writer.writerows(row_list3)

        with open('psi_4.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            # writer.writerow(["id"])
            writer.writerows(row_list4)

s = generate()
s.generate_data()