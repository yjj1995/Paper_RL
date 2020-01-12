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

    # def state(self, action, p0, g0):
    # 传入 子载波状态， 子载波分配，卸载比例，B, 卸载量
    def state(self, action, gh, sub, lam, B, R):
        print("卸载比例为:", lam)
        print("卸载量为:", R)
        state_init = []
        state = 3 * [0]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    state_init.append([i, j, k])
                    # 建立状态二维数组
        for i in range(3):
            if state_init[action][i] == 0:
                state[i] = 0.6
            elif state_init[action][i] == 1:
                state[i] = 1.2
            elif state_init[action][i] == 2:
                state[i] = 1.8
        r = 3 * [0]
        # 功耗
        E = 3 * [0]
        # reward
        reward = 0
        # 传输时间
        for i in range(3):
            # for i in range(3): 假设信道全部为3
            for j in range(sub[i]):
                r[i] = r[i] + B * math.log((1 + (state[i] * gh[i][j]) / (10 ** -13)), 2)
            # 1.功耗为reward
        # for i in range(3):
        #     reward = reward + state[i] * (0.5 * 1.5 * 10 ** 3 / R)
        # print("功耗为：", reward)
        # print("选择的功率为", state)
        # return action, -reward
        # 2. 以最小的值作为衡量标准
        for i in range(3):
            E[i] = E[i] + state[i] * (lam[i] * R[i] / r[i])
        for i in range(3):
            print("第", i + 1, "个用户的传输功耗为", E[i])
        e = sum(E) * 1000
        print("选择的功率为", state)
        print("总功耗为", e)
        # if E < 1.2:
        #     reward = 100
        # elif E == 1.2:
        #     reward = 0
        # elif E > 1.2:
        #     reward = -100
        # 和 靠近最优的值进行比较
        reward = -(e - 0.5)*100
        return action, reward, e
