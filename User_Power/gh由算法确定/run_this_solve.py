import matplotlib.pyplot as plt
import numpy as np

from Paper_RL.User_Power.Channel_Generate import Channel_Generate
from Paper_RL.User_Power.gh由算法确定.RL_brain import DeepQNetwork
from Paper_RL.User_Power.gh由算法确定.maze_env import Maze
from Paper_RL.User_Power.gh由算法确定.Ag_solve import Ag_solve


def run_maze():
    observation = [[0]]
    E_ = []
    # 用户使用子载波情况
    gh, lam, x, B, R = AG.Solve()
    print("**************************")
    print("**************************")
    print("**************************")
    print("数学求解的子载波分配矩阵为", x)
    sub = len(x)*[0]
    gh_ = np.zeros([3, 32]).tolist()
    for i in range(3):
        k = 0
        sub[i] = int(sum(x[i]))
        # 输出子载波矩阵
        for j in range(len(x[i])):
            if x[i][j] == 1:
                gh_[i][k] = gh[i][j]
                k = k + 1
    print(gh_)
    # 创建信道增益矩阵
    # 方法1. gh = [[0] * 3 for i in range(3)]
    for step in range(10000):
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
            # 传入子载波数量
        observation_, reward, E_all = env.state(action, gh_, sub, lam, B, R)
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
    AG = Ag_solve(3, 32)
    env = Maze()
    RL = DeepQNetwork(env.n_actions, env.n_features,
                      learning_rate=0.1,
                      reward_decay=0.9,
                      e_greedy=0.7,
                      replace_target_iter=200,
                      memory_size=2000,
                      # output_graph=True
                      )
    run_maze()
    RL.plot_cost()
