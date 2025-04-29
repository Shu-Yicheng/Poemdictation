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

#--打印列表，将列表分行输出。[输入]alist为一个一维列表。--
def prince(alist):
    for i in range(len(alist)):
        print(alist[i])

passages=readpassages('data/passages.txt')
title=''
while True:
	while title not in passages: #防止因为输入不存在的标题导致报错
	    title=input('请输入待查找文章标题，输入exit退出：')
	    if title=='exit':
	    	break  
	if title=='exit':
		break    
	prince(passages[title])
	title=''