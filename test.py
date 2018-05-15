#_*_encoding:utf-8_*_

#初步设想，利用numpy里面得dataframe。第一列作为索引，也就是状态列，每行为所选得action所获得得回报。目的也就是通过迭代使得回报接近合理。agent在执行每一步得时候还要通过K，
# 也就是总体资源数算出可以分配得资源，从而得出可以选择得action的列表，选择的时候要从这个列表中选取回报最高的，也就是说有可能回报最高的那个行动由于资源限制，不能选择。这也是个问题，
# 意味着q表最终可能很难收敛，一直在变。r表设为-1，1，2，3...也就是对于不分配资源有个惩罚，对于分配越多，奖励越高，不过不知道惩罚是不是太小了，这样会鼓励agent采取贪心算法。
#任务有一个到达率，为泊松分布，有一个离开率，也为泊松分布，运行时间为指数分布，
#泊松分布如何模拟呢，下一个时间段发生n件事情的概率，那状态怎么算呢
from __future__ import print_function

import numpy as np
import pandas as pd
import time

# lam=1 #任务到达泊松分布
#
# a=np.random.poisson(lam,100)
# b=np.random.poisson(lam,100)
# # print(a)
# # print('***********')
# # print(b)

np.random.seed(2)

N_STATES=6
ACTIONS=['left','right']
EPSILON=0.9#探索欲望
ALPHA=0.1
LAMBDA=0.9
MAX_EPISODES=13
FRESH_TIME=0.3#每一步的时间


#初始化qtable
def build_q_table(n_states,actions):
    table=pd.DataFrame(
        np.zeros((n_states,len(actions))),
        columns=actions,
    )
    # print(table)
    return table

# build_q_table(6,ACTIONS)


#动作选择
def choose_action(state,q_table):
    state_actions=q_table.iloc[state,:]
    if (np.random.uniform()>EPSILON)or(state_actions.all()==0):#随机选取动作，全部为0看成随机
        action_name=np.random.choice(ACTIONS)
    else:
        action_name=state_actions.argmax()
    return action_name



#环境对应
def get_env_eed_back(S,A):
    if A=='right':
        if S==N_STATES-2:
            S_='terminal'
            R=1
        else:
            S_=S+1
            R=0

    else:
        R=0
        if S==0:
            S_=S
        else:
            S_=S-1

    return S_,R


def update_env(S, episode, step_counter):
    # This is how environment be updated
    env_list = ['-']*(N_STATES-1) + ['T']   # '---------T' our environment
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode+1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r                                ', end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)


def rl():
    q_table=build_q_table(N_STATES,ACTIONS)
    for episode in range(MAX_EPISODES):
        step_counter=0
        S=0
        is_terminated=False
        update_env(S,episode,step_counter)
        while not(is_terminated):

            A=choose_action(S,q_table)
            S_,R=get_env_eed_back(S,A)
            q_predict=q_table.loc[S,A]
            if S_!='terminal':
                q_target=R+LAMBDA*q_table.iloc[S_,:].max()

            else:
                q_target=R
                is_terminated=True

            q_table.loc[S,A]+=ALPHA*(q_target-q_predict)
            S=S_

            update_env(S,episode,step_counter+1)

            step_counter+=1
    return q_table

q_table=rl()
print(q_table)