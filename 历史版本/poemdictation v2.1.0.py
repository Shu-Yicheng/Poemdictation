#©2024 Study Corporation。  All rights reserved.
#引入相关库
from random import randint
from datetime import datetime

#必要参数赋初值
log=[]#写入用户日志列表
logf=[]#存储已练习指针
globalflag=True#标记是否继续执行程序 True为继续执行
k=1#标记练习组数
filename1='data/question.txt' #存储题目的文件
filename2='data/answers.txt' #存储答案的文件
filename3='data/passages.txt' #存储参考文章的文件

#文件处理函数
#--将参考文章以列表形式存储在字典中。[输入]filename为字符串形式，存储待读文件标题;[输出]passage为一个字典，键为文章标题对应的首字母，值为存储参考文章的列表。--
def readpassages(filename):
	pas_file=open(filename,encoding='UTF-8')
	pas_lines=pas_file.readlines()
	passage={}
	raw=[]
	for i in pas_lines:
	    if i[0]=='#':
	        raw=[]
	        title=i[1:-1]
	    elif '#' in i:
	        raw.append(i[:i.find('#')])
	        passage[title]=raw
	    else:
	    	raw.append(i[:-1])
	pas_file.close()
	return passage   

#--将文件读入列表中。[输入]filename为字符串形式，存储待读文件；[输出]lines为一个列表，存储每一行。--
def readfile(filename):
	file=open(filename,encoding='UTF-8')
	lines=file.readlines()
	file.close()
	return lines

#	列表操作相关函数
#--对一个列表进行冒泡排序。[输入]alist为一个无序列表；[输出]alist为一个有序列表。--
def sort_list(alist):
	for i in range(1,len(alist)):
		c=0
		for j in range(-1,-len(alist)+i-1,-1):
			if alist[j]<alist[j-1]:
				c+=1
				alist[j],alist[j-1]=alist[j-1],alist[j]
		if c==0: #冒泡排序的优化，检查是否已经有序
			return alist	
	return alist

#--对列表中的特定对象进行二分查找。[输入]alist为一个升序列表，cur为一个整型，为待查找对象；[输出]flag为布尔型字符，标记是否找到，找到为Flase，未找到为True--			
def find_list(alist,cur):
	flag=True
	if len(alist)==0:
		return not flag
	m,n=0,len(alist)-1
	while n>=m:
		k=(m+n)//2 #左偏移
		if alist[k]==cur:
			flag=not flag
			break
		elif alist[k]>cur:				
		    n=k-1
		elif alist[k]<cur:
			m=k+1
	return flag
		
#日志操作相关函数
#--从日志文件中读取特定用户练习记录并写入列表。[输入]usn为字符串，用户名；[输出]logf为列表，元素为整型。--
def get_log(usn):
	file=open('log/logs.txt',encoding='UTF-8')
	filelines=file.readlines()
	file.close()
	logf=[]
	for i in filelines:
		if usn in i:
			for j in range(len(i)):
				if i[j]==',':
					logf.append(int(i[j+1:-1]))
	return logf
					
#--将题目序号写入日志列表。[输入]cur为整型，题目序号，logf为一个列表，存储历史题目序号[输出]logf为更新后的列表。--
def write_logf(cur,logf):
	logf.append(cur)
	logf=sort_list(logf)
	return logf
	
#--将日志行写入日志文件。[输入]usn为字符串，为用户名，cur为整型，为题目序号，logf为日志列表；[输出]logf为更新后的列表。--
def write_log(usn,cur,logf):
	logfile=open('log/logs.txt','a+',encoding='UTF-8')
	logfile.write(usn+','+str(cur))
	logfile.write('\n')
	logfile.close()
	logf=write_logf(cur,logf)
	return logf

#--将练习记录写入对应用户日志文件。[输入]usn为字符串，用户名，log为二维列表，存储题目和对应答案。--    
def write_logfile(usn,log):
	filename='log/'+usn+'.txt' #用户名对应的日志文件
	file=open(filename,'a+',encoding='UTF-8')
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
	        file.write('\n')
	    file.write('答案')
	    file.write('\n')
	    for q in log[i+1]:
	        file.write(q)
	        file.write('\n')
	    file.write('\n')
	    k+=1
	file.close() #关闭文件，否则一个字也写不进去

#与题目选取相关的函数
#--从题目和答案列表中随机选取一组题目和答案。[输入]que_list，ans＿list为一个列表，分别存储题目和对应的答案；[输出]out为一个二维列表，out[0]为题目，out[1]为答案。--
def choose(que_list,ans_list,logf):
	i=0
	out=[[],[]]
	while i<3:
		cur=randint(0,len(que_list)-1)
		#print(cur)
		if check(cur,logf)==True: #若不存在，则写入列表并保持升序排序
			i+=1
			out[0].append(str(cur)+'.'+que_list[cur][:-1])
			out[1].append(ans_list[cur][:-1])
			logf=write_log(usn,cur,logf)
	return out

#--检查选中题目序号是否存在。[输入]cur为u整型，为题目序号，logf为一个列表，存储已经选择过的题目序号，升序；输出]out_flag为布尔型，标记cur是否存在于logf中，True则为存在。--
def check(cur,logf):
    #out_flag=False
    if len(logf)==0:
    	logf=get_log(usn)
    	logf=sort_list(logf)
    out_flag=find_list(logf,cur)
    return out_flag	

#与操作相关的函数
#--操作栏。[输入]ans为一个列表，存储答案；globalflag为布尔型[，与全局变量globalflag对应。--
def operation_bar(ans,globalflag):
	helplist=['操作   对应代码','显示帮助   help','显示答案   ans','查询   pas','继续练习   next','退出练习   exit']
	while True:
		ope=input('请输入操作，输入help显示帮助：')
		if ope=='help':#输出帮助
			prince(helplist)
		elif ope=='ans':#输出答案
			print('答案')
			prince(ans)
		elif ope=='pas':#查询参考文章
			title=''
			while title not in passages:#防止因为输入不存在的标题导致报错
				title=input('请输入待查找文章标题，输入exit退出：')
				if title=='exit':
					break
			if title=='exit':#退出查询
				continue
			else:    
			    prince(passages[title])
		elif ope=='next':#继续练习
			break
		if ope=='exit':#退出练习
			globalflag=False
			return globalflag
		if ope=='debug':
			print(logf)
	return globalflag
	
#其他必要函数
#--打印列表，将列表分行输出。[输入]alist为一个一维列表。--
def prince(alist):
    for i in range(len(alist)):
        print(alist[i])

#--时间处理，输出当次练习完成时的时间并保存。--
def get_time():
    now=str(datetime.now())[0:16]
    return now

#---主程序---
que_list=readfile(filename1)
ans_list=readfile(filename2)
passages=readpassages(filename3)
usn=input('请输入用户名开始练习：')
logf=get_log(usn)#获取之前练习记录，防止出现重复
logf=sort_list(logf)#排序方便查找
while globalflag==True:
	out=choose(que_list,ans_list,logf)#选择一组题目
	que=out[0]
	ans=out[1]
	print('第'+str(k)+'组')
	k+=1
	print('题目')
	prince(que)
	log.append(que)
	log.append(ans)
	globalflag=operation_bar(ans,globalflag)
write_logfile(usn,log)#练习结束时将本次练习记录写入用户对应的日志中
print('练习结束')