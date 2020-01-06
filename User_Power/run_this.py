import matplotlib.pyplot as plt
import numpy as np

from Paper_RL.User_Power.Channel_Generate import Channel_Generate
from Paper_RL.User_Power.RL_brain import DeepQNetwork
from Paper_RL.User_Power.maze_env import Maze


def run_maze():
    observation = [[0]]
    E_ = []
    # 用户使用子载波数量
    Sub = [5, 15, 12]
    # 创建信道增益矩阵
    # 方法1. gh = [[0] * 3 for i in range(3)]
    gh = np.zeros([3, 15]).tolist()
    for step in range(150000):
        # e = 0
        ########################更改
        # for step in range(5):
        # RL choose action based on observation
        action = RL.choose_action(observation, step)
        print("action", action)
        # RL take action and get next observation and reward
        # observation_, reward, e1, p, g = env.state(action, p0, g0)
        # print("能耗为:", e1)
        # p0 = p
        # g0 = g
        # 传出能量消耗
        # 传入步数和动作和当前状态
        # 　每20步换一次信道
        #   每个用户的距离不同
        if step % 20 == 0:
            for i in range(Sub[0]):
                gh[0][i] = Channel_Generate(10)
            for i in range(Sub[1]):
                gh[1][i] = Channel_Generate(20)
            for i in range(Sub[2]):
                gh[2][i] = Channel_Generate(30)
            # 传入子载波数量
        observation_, reward, E_all = env.state(action, gh, Sub)
        E_.append(E_all)
        # print(observation, action, reward, [[observation_]])
        RL.store_transition(observation, action, reward, [[observation_]])
        ###########################12.19##################
        # swap observation
        if (step > 200) and (step % 5 == 0):
            RL.learn()
        observation = [[observation_]]
        print(observation)
        # break while loop when end of this episode
        # e = e + e1
        # print("第", episode, '回合的第', step+1, '步')
        #     E.append(e)
        # print(E)
        print('第', step, '步')
    plt.plot(E_)
    plt.show()


if __name__ == "__main__":
    # maze game
    env = Maze()
    RL = DeepQNetwork(env.n_actions, env.n_features,
                      learning_rate=0.01,
                      reward_decay=0.9,
                      e_greedy=0.6,
                      replace_target_iter=200,
                      memory_size=2000,
                      # output_graph=True
                      )
    run_maze()
    RL.plot_cost()
