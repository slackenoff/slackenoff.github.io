# import os
# t = os.getenv('python')
# s = os.getlogin()
# w = os.getcwd()
# i = os.getpid()
# ii = os.getppid()
# print(t,s,w,i,ii)
# import glob
#
# t = glob.iglob(r'D:\frontend\WebStorm 2022.2.1\*.json')
# print(t)
# for i in t:
#     print(i)
# python 进制转换
'''
bin()  二进制
oct() 八进制
int() 十进制
hex()  十六进制
'''
def convert(*args):
    w = args
    '''
       # 错误写法  w= int(args)
       输出2进制时，格式不对，没有b这个变量
       # int() argument must be a string, a bytes-like object or a real number, not 'tuple'
    '''
    '''
        # 错误写法 print(format(bin(int(t)[2:]),'08'))
        # 'int' object is not subscriptable
    '''
    '''
        # 错误写法 print(++format(bin(int(t))[2:],'08'))
        # bad operand type for unary +: 'str'
    '''
    r = []
    for t in args:
        # print(format(bin(int(t))[2:],'08')):
        # t1 = int(t)
        # t2 = bin(t1)
        # t3 = format(t2[2:], '08')
        # print(t3)
        print(str(bin(int(t))[2:].rjust(8,'0')))
        return r
convert(116,24,143,126)
# print(convert(255,255,255,224), end='\n')
# 计算网络地址和主机在网段中的地址
'''
1. 输入IP地址和子网掩码
2. 转换
3. 输出网络地址，主机地址
'''
