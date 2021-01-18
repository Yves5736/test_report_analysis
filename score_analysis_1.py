#使用了更简洁的代码，并且可以直接在文档中加上总分和平均分
path = input('report文档的位置是：')

with open(path) as f:
    data = f.readlines()
all_data = [(i.strip()).split() for i in data]

headings = all_data[0]
headings.append('总分')
headings.append('平均分')
datas = all_data[1: ]

for i in datas:
    sums = 0
    score = i[1:]
    for j in score:
        sums += int(j)
        average = sums/len(score)
    i.append(sums)
    i.append(average)

datas.sort(key = lambda x:x[10],reverse = True)
average_list = ['平均']

for i in range(1,len(datas[0])):
    average_sum = 0
    for j in datas:
        average_sum += float(j[i])
    average_final = average_sum/len(datas)
    average_list.append(average_final)

datas.insert(0,average_list)

datas_1 = []
for i in datas:
    lines = ['%.2f'%j if isinstance(j,float) else j for j in i]
    datas_1.append(lines)

rank=0
score_all = []

for i in datas_1:
    i.insert(0,rank)
    rank += 1
    new_score = map(lambda x:'不及格' if float(x)<60 else x,i[2:])
    new_score1 = i[0:2]
    new_score1 += list(new_score)
    score_all.append(new_score1)

data_head.insert(0,'名次')
score_all.insert(0,data_head)
with open(path,'w') as f:
    for i in score_all:
        strs = [str(sub) for sub in i]
        result = ' '.join(strs)+'\n'
        f.writelines(result)