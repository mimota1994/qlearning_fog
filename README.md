# qlearning_fog
使用qlearning来做资源分配
随机生成下一个片段的到来任务数以及离开任务数
为了解决不知道先处理哪个任务，随机打乱这些任务，0代表任务到来，1代表任务离开
封装了两个函数，arrive和leave
对于arrive函数，输入是state，resource，输出是新的state，resource，中间还有一个flag来表明action是否为0，也就是是否拒绝任务，用于最后的统计，当然统计结果很差，汗颜。。。
对于leave函数，输入是state，resource，输出是新的state，resource，随机挑选一个存在的任务，解放它，更新state和resource
