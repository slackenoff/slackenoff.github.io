# 冒泡排序   最基础的交换排序，远离，每次将最大的数移至排序的末尾
# 原理   比较+交换
# 时间复杂度  顺序，逆序
import time
lists = [13, 53, 55, 65, 2, 21, 531, 6, 453]
'''
for t in range(len(lists)):
    if t < len(lists):
        print(lists[t])
        ++t
    else:
        break
默认从0-8开始取下标
'''
count = 0
for t in range(len(lists)-1):
    for s in range(len(lists)-1-t):
        if lists[s] > lists[s+1]:
            # python交换位置方式
            lists[s], lists[s+1] = lists[s+1], lists[s]
            count = count + 1
            print(t, s, '第', count, '次转换后的列表为：', lists)
# 思路
'''
从无序的列表中，每次将最大值，比较后交换
'''





