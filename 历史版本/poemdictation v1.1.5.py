#©2024 Study Corporation。  All rights reserved.
#引入相关库
from random import randint
from datetime import datetime
#from os import system

#--选择，从题库中随机选择三个及答案并输出。que_list（题目）,【输入】ans_list（答案）为列表；【输出】out为二维列表，out[0]为题目，out[1]为答案。--
def choose(que_list,ans_list):
    j=0
    lens=len(que_list)
    #que=ans=[]
    out=[[],[]]
    while j<3:
        cur=randint(0,lens-1)
        if que_list[cur][1]!=True:
            out[0].append(que_list[cur][0])
            que_list[cur][1]=True
            out[1].append(ans_list[cur])
            j+=1
    return out

#--检查题库中所有的题目是否都已经被选中。【输入】que_list为二维列表，cnt为整型，【输出】flag为布尔型--
def check(que_list,cnt):
    flag=False
    lens=len(que_list)
    if cnt>= lens-lens%3: #比较已经选择的题数是否大于全部题数（由于不保证题库内为3的倍数，防止出现死循环所以要减去余数）
        flag= not flag
    return flag

#--输出日志，将本次练习题目及答案写入log.txt文件。【输入】log为二维列表，偶数位为题目，奇数位为对应答案。--
def to_file(log):
    file=open('log.txt','a+',encoding='UTF-8')
    file.write(get_time())
    file.write('\n')
    k=1
    for i in range(0,len(log),2):
            file.write('第'+str(k)+'组')
            file.write('\n')
            file.write('题目')
            file.write('\n')
            for j in log[i]:
                    file.write(j)
            file.write('答案')
            file.write('\n')
            for q in log[i+1]:
                    file.write(q)
            file.write('\n')
            k+=1
    file.write('\n')
    file.close() #关闭文件，否则一个字也写不进去

#--读取文件，读取当前目录下题目和答案写入对应列表。【输入】filename1,filename2为字符串型文件名；【输出】que_list为三维列表，由二维列表构成，ans_list为一维列表。--
def get_file(filename1,filename2):
    que_file=open(filename1,encoding='UTF-8')
    que_file=que_file.readlines()
    ans_file=open(filename2,encoding='UTF-8')
    ans_list=ans_file.readlines()
    que_list=[] 
    for i in range(len(que_file)):
        raw=[que_file[i],False] #raw为二维列表，raw[0]为字符，题目内容，raw[1]为布尔型，标记题目是否遍历
        que_list.append(raw)
    return que_list, ans_list

#--打印列表，将列表分行输出。【输入】alist为一个一维列表。--
def prince(alist):
    for i in range(len(alist)):
        print(alist[i])

#--时间处理，输出当次练习完成时的时间并保存。--
def get_time():
    now=str(datetime.now())[0:16]
    return now
        
#---主程序---
log=[]#日志列表，初始为空
filename1='question.txt'
filename2='answers.txt'
que_list,ans_list=get_file(filename1,filename2)
cnt=0
k=1 #练习序号
while True:               
    out=choose(que_list,ans_list) #从题库中选择题目
    que=out[0]#题目列表
    ans=out[1]#答案列表
    print('第'+str(k)+'组')
    k+=1
    print('题目')
    prince(que)
    cnt+=3   #计数器 （可能更改为其他计数，不一定为3）
    log.append(que)
    log.append(ans)
    ask=input('请输入下一步操作（a为显示答案，b为结束）:')
    if ask=='b':
        print('答案')
        prince(ans)
        break            #先输出答案再结束程序
    elif ask=='a':
        print('答案')
        prince(ans)
    if check(que_list,cnt):#检查是否所有题目都显示完成，全部完成返回值为False
        print('所有题目已完成')
        break
to_file(log) #将日志列表写入log日志文件
print('练习结束')
#system('pause')