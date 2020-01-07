import numpy as np
import matplotlib.pyplot
import random
import math  # 导入 math 模块
from Paper_RL.User_Power.Channel_Generate import Channel_Generate


class Ag_solve(object):
    def __init__(self, K_In, N_In):
        self.K = K_In
        self.N = N_In

    def solve(self):
        K = self.K
        N = self.N
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
        T = 9.5 * 10 ** -3
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
        dis = 10 + 5 * (np.random.rand(K))
        # dis = K*[10]
        # rand 从0到1之间随机
        # 随机产生距离 20m 之类

        c_k = 950 + 50 * (np.random.rand(K))
        # 处理一位用户k的一位数据需要多少CPU周期

        f_k = (10 ** 9) * (0.6 + 0.1 * (np.random.rand(K)))
        # 用户的计算频率
        a_k = []
        b_k = []
        q = 2
        for i in range(K):
            a_k.append((10 ** (-q)) * random.random() + (10 ** (-q)))
            b_k.append((10 ** (-q)) * random.random() + (10 ** (-q)))
            pass

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
            print("第", i, "个用户为:", gh[i])
        # 初始化变量
        lam = K * [0.4]
        print("初始化卸载比例为:", lam)
        # 卸载比例
        fkm = K * [0]
        # 定义分配频率

        rho = 0.01
        fkm_U = K * [0]
        fkm_L = K * [0]
        l_k = K * [0]
        z = 0
        a_k_u = K * [0]
        b_k_u = K * [0]
        # 迭代
        while z <= Z:
            # 1.求解fkm 二分法
            for i in range(K):
                fkm_U[i] = F
                fkm_L[i] = 0
                fkm[i] = (1 / 2) * (fkm_U[i] + fkm_L[i])
                # print(abs(2*fkm[i]*k_m*lam[i]*c_k[i]*R[i]-(b_k[i]*c_k[i]*R[i]*lam[i])/((fkm[i])**2) + gam))
                while abs(2 * fkm[i] * k_m * lam[i] * c_k[i] * R[i] - (b_k[i] * c_k[i] * R[i] * lam[i]) / (
                        (fkm[i]) ** 2) + gam) > rho:
                    fkm[i] = (1 / 2) * (fkm_L[i] + fkm_U[i])
                    l_k[i] = 2 * fkm[i] * k_m * lam[i] * c_k[i] - (b_k[i] * c_k[i] * R[i] * lam[i]) / (
                            (fkm[i]) ** 2) + gam
                    if l_k[i] > 0:
                        fkm_U[i] = fkm[i]
                    elif l_k[i] < 0:
                        fkm_L[i] = fkm[i]
                print(fkm)

            ####2 子载波求解
            ln_1 = np.zeros([N, K])
            ln_h = K * [0]
            # 初始化子载波分配矩阵
            for i in range(N):
                ln_h = K * [0]
                for j in range(K):
                    if lam[j] > 0:
                        ln_1[i, j] = (B * (math.log((1 + p_max * gh[j][i] / g), 2))) * (
                                1 / (lam[j] * R[j] * (p_max + b_k[j])))
                ln_h = ln_1[i].tolist().copy()
                x[ln_h.index(max(ln_h)), i] = 1
            print("子载波分配矩阵为:", x)
            # 取出子载波矩阵的每一行
            # 判断子载波i 分配给哪个用户
            #  计算卸载用户的传输速度
            r = K * [0]
            for i in range(K):
                for j in range(N):
                    r[i] = r[i] + B * x[i, j] * math.log(1 + (p_max * gh[i][j] / g), 2)
            print("传输速率为:", r)

            # 对偶乘子更新
            gam_u = gam - (sum(fkm) - F) * 10 ** -18
            for i in range(K):
                a_k_u[i] = a_k[i] - (((1 - lam[i]) * R[i] * c_k[i]) / fkm[i] - T) * (10 ** -3)
                b_k_u[i] = b_k[i] - ((lam[i] * R[i]) / r[i] + (lam[i] * R[i] * c_k[i]) / fkm[i] - T) * (10 ** -7)
                if a_k[i] < 0:
                    a_k[i] = 0
                elif b_k[i] < 0:
                    b_k[i] = 0
                elif (a_k_u[i] - a_k[i] <= e) and (b_k_u[i] - b_k[i] <= e) and (gam_u - gam <= e):
                    break
                else:
                    gam = gam_u
                    a_k[i] = a_k_u[i]
                    b_k[i] = b_k_u[i]

            z = z + 1
            print("步数为 :", z)

        # 求解卸载比例
        E_lam = K * [0]
        for i in range(K):
            E_lam[i] = (r[i] * R[i] * c_k[i] * ((fkm[i] ** 2) * k_m - (f_k[i] ** 2) * k) + p_max * R[i]) / r[i]
            # print(E_lam)
            if E_lam[i] > 0:
                if 1 - (T * f_k[i]) / (c_k[i] * R[i]) > 0:
                    lam[i] = 1 - (T * f_k[i]) / (c_k[i] * R[i])
                    # print("lam", lam[i])
                else:
                    lam[i] = 0
            elif E_lam[i] < 0:
                if (T * r[i] * fkm[i]) / (R[i] * fkm[i] + r[i] * R[i] * c_k[i]) < 1:
                    lam[i] = (T * r[i] * fkm[i]) / (R[i] * fkm[i] + r[i] * R[i] * c_k[i])
                else:
                    lam[i] = 1
        # 返回 信道，和 分配情况， 数据量， 卸载比例
            return gh, lam, x, B, R
