from 相同功率.maze_env import Maze
from 相同功率.RL_brain import DeepQNetwork
import matplotlib.pyplot as plt

def run_maze():
    E = []
    observation = [[0]]
    p0 = 30
    g0 = 3
    for episode in range(3000):
        print(observation)
        e = 0
        ########################更改
        for step in range(5):
            # RL choose action based on observation
            action = RL.choose_action(observation, episode)
            # 传入episode
            print("action", action)
            # RL take action and get next observation and reward
            observation_, reward, e1, p, g = env.state(action, p0, g0)
            print("能耗为:", e1)
            p0 = p
            g0 = g
            # 传出能量消耗
            # 传入步数和动作和当前状态
            RL.store_transition(observation, action, reward, [[observation_]])
            ###########################12.19##################
            # swap observation
            observation = [[observation_]]
            # break while loop when end of this episode
            e = e + e1
            print("第", episode, '回合的第', step+1, '步')
        if (episode > 200) and (episode % 5 == 0):
            RL.learn()
        E.append(e)
    print(E)
    plt.plot(E)
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