#_*_encoding:utf-8_*_#
#迷宫

import numpy as np
import pandas as pd


class QLearningTable:
    def __init__(self,actions,learning_rate=0.01,reward_decay=0.9,e_greedy=0.9):
        self.actions=actions
        self.lr=learning_rate
        self.gamma=reward_decay
        self.epsilon=e_greedy
        self.q_table=pd.DataFrame(columns=self.actions,dtype=np.float64)


#sum代表资源剩余总数
    def choose_action(self,observation,sum):
        self.check_state_exist(observation)

        # 动作过滤，也就是筛去不能选择的动作

        #action selection
        if np.random.uniform()<self.epsilon:
            #choose best action
            state_action=self.q_table.loc[observation,:]
            temp=[]
            for action in [0,1,2,3]:
                if action<=sum:
                    temp.append(state_action[action])
            state_action=pd.Series(temp)
            #打乱索引
            state_action=state_action.reindex(np.random.permutation(state_action.index))
            action=state_action.idxmax()

        else:
            temp=[]
            for action in self.actions:
                if action<=sum:
                    temp.append(action)
            #choose random action
            action=np.random.choice(temp)

        return action,sum-action


    def learn(self,s,a,r,s_,resource):
        self.check_state_exist(s_)
        q_predict=self.q_table.loc[s,a]
        if s_!='terminal':
            #去除不能选取的
            t=self.q_table.loc[s_,:]
            for i in [0,1,2,3]:
                if i>resource:
                    t=t[:i]
                    break
            q_target=r+self.gamma*t.max()

        else:
            q_target=r

        self.q_table.loc[s,a]+=self.lr*(q_target-q_predict)

    def check_state_exist(self,state):
        if state not in self.q_table.index:
            #append new state to q table
            self.q_table=self.q_table.append(
                pd.Series(
                    [0]*len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )