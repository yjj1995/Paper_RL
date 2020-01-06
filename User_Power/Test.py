import numpy as np
import matplotlib.pyplot
import random
import math  # 导入 math 模块
from Paper_RL.User_Power.Channel_Generate import Channel_Generate

K = 5
# 用户数
N = 32
# 子载波数
e = 10 ** -5
# 对偶因子迭代误差
Z = 100
# 迭代次数
k = 10 ** -25
# 用户k的能耗系数
k_m = 10 ** -26
# MEC的能耗系数
g = 10 ** -13
# segma**2 单位w
B = 12.5 * (10 ** 3)
# 带宽 单位w
p_max = 0.6
# 用户的最大功率
T = 9.5*10**-3
# 时间延迟
F = 10 ** 10
# MEC 总的计算频率，单位为HZ

# 1.间隔100
# R = np.arange(1500,(1500+K*100),100)
# 2.随机1500-1800
# K个用户的数据量
# 取整
# R = np.trunc((1500 + 300*(np.random.uniform(0,1,K))))
# uniform 指定范围 随机
R = 1500 + 100 * (np.random.uniform(0, 1, K))
print("数据量为:", R)
dis = 10 + 10 * (np.random.rand(K))
print("距离为:", dis)
# dis = K*[10]
# rand 从0到1之间随机
# 随机产生距离 20m 之类

c_k = 950 + 50 * (np.random.rand(K))
print("c为:", c_k)
# 处理一位用户k的一位数据需要多少CPU周期

f_k = (10 ** 9) * (0.6 + 0.1 * (np.random.rand(K)))
print("用户频率为:", f_k)
# 用户的计算频率
a_k = []
b_k = []
q = 2
for i in range(K):
    a_k.append((10 ** (-q)) * random.random() + (10 ** (-q)))
    b_k.append((10 ** (-q)) * random.random() + (10 ** (-q)))
    pass

print("乘子为:", a_k)
print("乘子为:", b_k)
gam = 10 ** -q
# 对偶乘子初始化

h = np.zeros([K, N]).tolist()
# list中元素为一维数组 即变成了二维数组，索引为L[i][j]
# 如果是numpy的二维数组 可以用[i][j]，也可以用[i,j]
# h = [ [0] * N for i in range(K)]
gh = np.zeros((K, N)).tolist()
# 初始化信道功率矩阵

# 定义子载波分配矩阵并初始化
x = np.zeros([K, N])
# x.tolist()
# 转化为列表


# 初始化每个子载波的相关属性
for i in range(K):
    for j in range(N):
        h[i][j] = Channel_Generate(dis[i])
        gh[i][j] = np.linalg.norm(h[i][j])
# 初始化变量
print(gh)
lam = K * [0.5]
# 卸载比例
fkm = K * [0]
# 定义分配频率

rho = 0.01
fkm_U = K * [0]
fkm_L = K * [0]
l_k = K * [0]
z = 0