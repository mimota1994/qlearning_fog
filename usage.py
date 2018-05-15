#_*_encoding:utf-8_*_#
from maze_brain import QLearningTable
from env import Maze
import numpy,pandas
from greedy import greedy

#qtable对于任务到来的反应
def arrive(state ,resource):

    #挑选动作以及执行完动作之后的资源数，如果状态不存在，会在qtable中加入这个状态
    action,resource_ = RL.choose_action(str(state),resource)

    if action==0:
        reject_flag=True
    else:
        reject_flag=False

    #执行完这个动作之后，系统到达的另外一个状态，以及即即时回报
    state_, reward = env.step(action, state)

    #更新qtable的值
    RL.learn(str(state),action,reward,str(state_),resource_)

    state=state_
    resource = resource_

    return state,resource,reject_flag


#任务离开
def leave(state,resource):
    #任务离开后的状态以及资源数
    state_,resource_=choose_leave(state,resource)

    state=state_
    resource=resource_

    return state,resource


#选择某个存在的任务
def choose_leave(state,resource):
    #随机挑选一个任务离开，当然这个任务得存在
    leave_task_index = numpy.random.randint(0,3)
    while(state[leave_task_index]==0):
        leave_task_index=numpy.random.randint(0,3)

    #更新资源数
    state[leave_task_index]-=1
    resource=resource+leave_task_index+1

    return state,resource


#检查状态是否为空
def check_state_empty(state):
    flag=True
    for i in state:
        if i!=0:
            flag=False
            break
    return flag


#初始化qtable和环境
RL=QLearningTable(actions=list(range(4)))
env=Maze()


#初始化状态
initial_state=[0,0,0]
initial_resource=10

state=initial_state
resource=initial_resource

reject_nums=0

for i in range(10000):
    #生成下一个时间片段的任务
    pre_arrive_nums=numpy.random.poisson(7.2)
    pre_leave_nums=numpy.random.poisson(2.4)
    pre_nums=pre_leave_nums+pre_arrive_nums
    if pre_nums==0:
        continue
    task=numpy.random.choice(2,pre_nums,p=[pre_arrive_nums/(pre_nums+0.0),pre_leave_nums/(pre_nums+0.0)])#生成任务队列


    #统计一下任务得个数
    sum=0#代办任务池


    for i in task:
        if i==0:
            #任务加入代办任务池
            sum+=1

            state,resource,reject_flag=arrive(state,resource)

            #统计拒绝率
            if reject_flag==True:
                reject_nums+=1
                continue

            #如果分配了资源得话，任务就从代办任务池离开
            sum-=1

        if i==1:
            #检查state是否为空
            flag=check_state_empty(state)
            if flag==True:
                continue

            state,resource=leave(state,resource)

numpy.set_printoptions(threshold='nan')
pandas.set_option('display.max_rows',None)
print(task)
print(RL.q_table)
print('reject nums',reject_nums)

    # reject_nums=0
    # state=[0,0,0]
    # resource=10
    #
    # for i in task:
    #     if i==0:
    #         state,resource,reject_flag=greedy(state,resource)
    #         if reject_flag==True:
    #             reject_nums+=1
    #
    #     if i==1:
    #         #检查state是否为空
    #         flag=check_state_empty(state)
    #         if flag==True:
    #             continue
    #
    #         state,resource=leave(state,resource)
    #
    # numpy.set_printoptions(threshold='nan')
    # pandas.set_option('display.max_rows',None)
    #
    # print('reject nums',reject_nums)
