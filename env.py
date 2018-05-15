import numpy as np

class Maze(object):
    def step(self,action,s):
        # block=False
        if action == 0:
            s_=s
            reward = -1
            # block=True

        elif action == 1:
           s_ = s[:]
           s_[0]=s_[0]+1

           reward = 1

        elif action == 2:
            s_=s[:]
            s_[1] = s_[1] + 1

            reward = 2

        elif action == 3:
            s_ = s[:]
            s_[2] = s_[2] + 1

            reward = 3



        return s_, reward

    def nums(self,time):
        arrive_nums=np.random.poisson(7.2,1)[0]
        depature_time=np.random.exponential(6.6,arrive_nums)+time
        return arrive_nums,depature_time