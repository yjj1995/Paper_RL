import numpy as np
import math  # 导入 math 模块

def Channel_Generate(dis):
    h = math.sqrt(2)/ 2. * (np.random.randn(1, 1)) + 1j * (np.random.randn(1, 1)) * dis ** -2
    gh = np.linalg.norm(h)*(10**-4)
    return gh
