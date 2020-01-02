import numpy as np
import time
import sys
import math

class Maze(object):
    def __init__(self):
        # self.action_space = ['0', '1', '2', '3', '4']
        self.action_space = [i for i in range(27)]
        print(self.action_space)
        # 构建动作空间
        self.n_actions = len(self.action_space)
        self.n_features = 1

    # def state(self, action, p0, g0):
    def state(self, action):
        state_init = []
        g = [0.03, 1.23, 2.23]
        state = 3*[0]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    state_init.append([i, j, k])
                    # 建立状态二维数组
        for i in range(3):
            if state_init[action][i] == 0:
                state[i] = 100
            elif state_init[action][i] == 1:
                state[i] = 200
            elif state_init[action][i] == 2:
                state[i] = 300
                # 响应动作
        R = 0
        P = 0
        for i in range(3):
            R = R + 12.5 * 10 ** 3 * math.log((1 + (state[i] * g[i]) / (10**-13)), 2)
            P = P + state[i]
        # 计算传输的功率,速度

        reward = P * (0.5 * 1.5 * 10 ** 3 / R)
        print("功耗为：", reward)
        return action, -reward