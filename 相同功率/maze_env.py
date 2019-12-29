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
        self.action_space = [0, 1, 2, 3]
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
        if action == 0:
            state = 0
            p = 1000
        elif action == 1:
            state = 1
            p = 2000
        elif action == 2:
            state = 2
            p = 3000
        elif action == 3:
            state = 3
            p = 4000
        R = 0
        for i in range(3):
            R = R + 12.5 * 10 ** 3 * math.log((1 + (p * gh[i]) / (10 ** -13)), 2)
        # 计算传输的功率,速度
        reward = 3 * p * (0.5 * 1.5 * 10 ** 3 / R)
        print("功耗为：", reward)
        return state, -reward
