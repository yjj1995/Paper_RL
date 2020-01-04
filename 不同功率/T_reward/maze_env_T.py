"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the environment part of this example.
The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""
import math
import numpy as np


class Maze(object):
    def __init__(self):
        self.action_space = [i for i in range(27)]
        print(self.action_space)
        # 构建动作空间
        self.n_actions = len(self.action_space)
        self.n_features = 1

    # 　信道变化
    def Channel_Generate(self):
        dis = 10
        H = []
        gh = []
        for i in range(3):
            H.append(2 ** 0.5 / 2 * (np.random.randn(1, 1)) + 1j * (np.random.randn(1, 1)) * dis ** -2)
            gh.append(np.linalg.norm(H[i]))
        return gh

    # def state(self, action, p0, g0):
    def state(self, action, gh):
        state_init = []
        state = 3 * [0]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    state_init.append([i, j, k])
                    # 建立状态二维数组
        for i in range(3):
            if state_init[action][i] == 0:
                state[i] = 1000
            elif state_init[action][i] == 1:
                state[i] = 2000
            elif state_init[action][i] == 2:
                state[i] = 3000
        R = 0
        # 功耗
        E = 0
        # reward
        reward = 0
        # 传输时间
        for i in range(3):
            R = R + 12.5 * 10 ** 3 * math.log((1 + (state[i] * gh[i]) / (10 ** -13)), 2)
        T = 0.5 * 1.5 * 10 ** 3 / R
            # 1.功耗为reward
        # for i in range(3):
        #     reward = reward + state[i] * (0.5 * 1.5 * 10 ** 3 / R)
        # print("功耗为：", reward)
        # print("选择的功率为", state)
        # return action, -reward
        # 2. 以最小的值作为衡量标准
        for i in range(3):
            E = E + state[i] * (0.5 * 1.5 * 10 ** 3 / R)
        print("功耗为：", E)
        print("传输的时间为", T)
        print("选择的功率为", state)
        # 200000次


        return action, reward, E
