import numpy as np
import matplotlib.pyplot
import random
import math  # 导入 math 模块
from Paper_RL.User_Power.Channel_Generate import Channel_Generate


class Ag_solve(object):
    def __init__(self):
        self.K = 4
        self.N = 64
        self.e = 10 ** -5
        self.Z = 100
        self.k = 10 ** -25
        self.k_m =
