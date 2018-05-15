

def greedy(state,resource):
    reject_flag=False
    if resource>=3:
        state[2]+=1
        resource-=3

    elif resource==2:
        state[1]+=1
        resource-=2

    elif resource==1:
        state[0]+=1
        resource-=1

    elif resource==0:
        reject_flag=True

    return state,resource,reject_flag
