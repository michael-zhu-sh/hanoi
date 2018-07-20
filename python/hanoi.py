'''
author:Michael Zhu
email:michael.ai@foxmail.com
'''
moveCnt=0
def hanoi(n,A,B,C):
    '''汉诺塔递归演示函数，参数n是圆盘的数量，参数A、B、C是柱子的名称'''
    global moveCnt
    if (1==n):
        print(A,'-->',C)
        moveCnt += 1
    else:
        hanoi(n-1,A,C,B)
        print(A,'-->',C)
        moveCnt += 1
        hanoi(n-1,B,A,C)
    
hanoi(6,'A','B','C')    #2个圆盘，柱子称为A,B,C。
print('移动次数：', moveCnt)