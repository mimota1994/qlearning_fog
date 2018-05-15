#_*_encoding:utf-8_*_#
"""
Reinforcement learning maze example.
Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].
This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.
View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

from env import Maze
from maze_brain import QLearningTable
import time
import numpy as np



def update():
    for episode in range(50000):
        # initial observation
        observation = [0,0,0]
        # block_num = 0
        sum=10#资源数
        # time=0
        # leave_queue=np.array([])
        while (sum>0):
            #
            # # 得到下一个时间片段到来的任务个数以及任务的持续时间
            # arrive_nums,depature_time=env.nums(time)
            # #将任务的持续时间加入任务池
            # leave_queue=np.append(leave_queue,depature_time)
            # leave_queue=np.sort(leave_queue)
            #
            # resource=np.random.choice([0,1,2])
            # while(observation[resource]==0):
            #     resource=np.random.choice([0,1,2])
            # observation[resource]=observation[resource]-1
            # sum=sum+resource+1

            # RL choose action based on observation,做完决策之后的剩余资源数
            action,sum = RL.choose_action(str(observation),sum)

            # RL take action and get next observation and reward
            observation_, reward = env.step(action,observation)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            # if block:
            #     block_num+=1
            #     print(block_num)
            #
            # if block_num>100:
            #     break


    print(RL.q_table)

    # end of game
    print('game over')
    # env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(4)))

    update()

    # env.after(100, update)
    # env.mainloop()