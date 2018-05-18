import numpy as np


def column_sum(data, c):
    return np.sum(data[:, c])


data1 = np.array(np.genfromtxt('dataSets/densEst1.txt'))
data2 = np.array(np.genfromtxt('dataSets/densEst2.txt'))
N1 = len(data1)
N2 = len(data2)

#unbiased
mu1 = [column_sum(data1, i) / N1 for i in [0, 1]]
mu2 = [column_sum(data2, i) / N2 for i in [0, 1]]

#biased
data1 = data1 - mu1
data2 = data2 - mu2

# print([np.matmul(np.transpose(data1[i, :]), data1[i, :]) for i in range(0, N1)])

# np.matmul(data1, np.transpose(data1))
# np.matmul(data2, np.transpose(data2))

# print(data1[0, :])
# print(data1[0, :].)
print(np.outer(data1[0, :], data1[0, :]))
