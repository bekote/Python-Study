# -*- coding: UTF-8 -*-
import re


class pipei():
    def __init__(self,amount,n,k,t,all):
        self.amount = amount
        self.n = n
        self.k = k
        self.t = t
        self.all = all

    def count(self,wl):
        file = open('/home/lin/文档/zuoye/太空旅客.txt', 'rw+')
        txt = file.read()
        for line in wl.readlines():
            word = line.strip()
            same = re.findall(word, txt)
            self.amount = self.amount + len(same)
        return self.amount

    def countf(self):
        for i in range(self.n):
            wl = self.t[i]
            print self.k[i],self.count(wl)
            self.all = self.all + self.count(wl)
        print self.k[(self.n+1)],'总计',self.all



amount = 0
all = 0
k0 = ['反派','角色','角色中的其他','男主角','女主角','配角','角色']
f0 = open('/home/lin/文档/zuoye/角色/反派.txt','rw+')
f1 = open('/home/lin/文档/zuoye/角色/角色.txt','rw+')
f2 = open('/home/lin/文档/zuoye/角色/角色中的其他.txt','rw+')
f3 = open('/home/lin/文档/zuoye/角色/男主角.txt','rw+')
f4 = open('/home/lin/文档/zuoye/角色/女主角.txt','rw+')
f5 = open('/home/lin/文档/zuoye/角色/配角.txt','rw+')
t0 = [f0,f1,f2,f3,f4,f5]
n0 = len(t0)-1
result = pipei(amount,n0,k0,t0,all)
result.countf()
print '\n'

k1 = ['发展','结局','剧情','开头','泪点','笑点','剧情']
f6 = open('/home/lin/文档/zuoye/剧情/发展.txt','rw+')
f7 = open('/home/lin/文档/zuoye/剧情/结局.txt','rw+')
f8 = open('/home/lin/文档/zuoye/剧情/剧情.txt','rw+')
f9 = open('/home/lin/文档/zuoye/剧情/开头.txt','rw+')
f10 = open('/home/lin/文档/zuoye/剧情/泪点.txt','rw+')
f11 = open('/home/lin/文档/zuoye/剧情/笑点.txt','rw+')
t1 = [f6,f7,f8,f9,f10,f11]
n1 = len(t1)-1
result1 = pipei(amount,n1,k1,t1,all)
result1.countf()
print '\n'