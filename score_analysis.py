name_dic = {} 
name_dic_a = {} 
name_li = []
chinese = {}
math = {}
english = {}
phisics = {}
chemistry ={}
biology = {}
politics = {}
history = {}
geography = {}
all_data = []
rank_dic = {}

def sort(dic): 
    import operator
    out = sorted(dic.items(), key = operator.itemgetter(1), reverse= True)
    return out

def add_score(dic_given):
    a = 0
    li = dic_given.values()
    for item in li:
        a += item
    return a

def average(dic_given):
    s = add_score(dic_given)
    b = s / len(dic_given)
    return b

def change_score(list_given, dic_given):
    dic_output = dic_given
    for i in range(0, len(list_given) - 1):
        if dic_output[list_given[i]] < 60:
            dic_output[list_given[i]] = '不及格'
    return dic_output

lines = 0

path = input('report文档的位置是：')

f = open(path,'r')
for line in f:
    lines += 1
    line = line.strip('\n')
    line_0 = line.split(' ')
    all_data += line_0

f.close()

for i in range(0,lines - 1):
    name_dic[all_data[(i + 1) * 10]] = 0
    name_li.append(all_data[(i + 1) * 10])
    chinese[all_data[(i + 1) * 10]] = int(all_data[(i + 1) * 10 + 1])
    math[all_data[(i + 1) * 10]] = int(all_data[(i + 1) * 10 + 2])
    english[all_data[(i + 1) * 10]] = int(all_data[(i + 1) * 10 + 3])
    phisics[all_data[(i + 1) * 10]] = int(all_data[(i + 1) * 10 + 4])
    chemistry[all_data[(i + 1) * 10]] = int(all_data[(i + 1) * 10 + 5])
    biology[all_data[(i + 1) * 10]] = int(all_data[(i + 1) * 10 + 6])
    politics[all_data[(i + 1) * 10]] = int(all_data[(i + 1) * 10 + 7])
    history[all_data[(i + 1) * 10]] = int(all_data[(i + 1) * 10 + 8])
    geography[all_data[(i + 1) * 10]] = int(all_data[(i + 1) * 10 + 9])

for i in range(0, len(name_li)):
    name_dic[name_li[i]] += chinese[name_li[i]]
    name_dic[name_li[i]] += math[name_li[i]]
    name_dic[name_li[i]] += english[name_li[i]]
    name_dic[name_li[i]] += phisics[name_li[i]]
    name_dic[name_li[i]] += chemistry[name_li[i]]
    name_dic[name_li[i]] += biology[name_li[i]]
    name_dic[name_li[i]] += politics[name_li[i]]
    name_dic[name_li[i]] += history[name_li[i]]
    name_dic[name_li[i]] += geography[name_li[i]]

for i in range(0, len(name_li)):
    name_dic_a[name_li[i]] = name_dic[name_li[i]] / 9

score_ranked_s = sort(name_dic)
score_ranked_a = sort(name_dic_a)

i = 0
for item in score_ranked_s:
    i += 1
    rank_dic[item[0]] = i

s = ''

for i in range(0, len(score_ranked_s) - 1):
    s = s + score_ranked_s[i][0] + '总分是%d'%score_ranked_s[i][1] + '，' +  '平均分是%.2f'%score_ranked_a[i][1] + '，' + '第%d名'%rank_dic[score_ranked_s[i][0]] + '\n'

print(s)
print('\n')

sum_chinese = add_score(chinese)
average_chinese = average(chinese)
sum_math = add_score(math)
average_math = average(math)
sum_english = add_score(english)
average_english = average(english)
sum_phisics = add_score(phisics)
average_physics = average(phisics)
sum_chemistry = add_score(chemistry)
average_chemistry = average(chemistry)
sum_biology = add_score(biology)
average_biology = average(biology)
sum_politics = add_score(politics)
average_politics = average(politics)
sum_history = add_score(history)
average_history = average(history)
sum_geography = add_score(geography)
average_geography = average(geography)

print('语文成绩总和：%d'%sum_chinese)
print('语文成绩平均：%.2f'%average_chinese)
print('数学成绩总和：%d'%sum_math)
print('数学成绩平均：%.2f'%average_math)
print('英语成绩总和：%d'%sum_english)
print('英语成绩平均：%.2f'%average_english)
print('物理成绩总和：%d'%sum_phisics)
print('物理成绩平均：%.2f'%average_physics)
print('化学成绩总和：%d'%sum_chemistry)
print('化学成绩平均：%.2f'%average_chemistry)
print('生物成绩总和：%d'%sum_biology)
print('生物成绩平均：%.2f'%average_biology)
print('政治成绩总和：%d'%sum_politics)
print('政治成绩平均：%.2f'%average_politics)
print('历史成绩总和：%d'%sum_history)
print('历史成绩平均：%.2f'%average_history)
print('地理成绩总和：%d'%sum_geography)
print('地理成绩平均：%.2f'%average_geography)

'修改各科成绩'

chinese = change_score(name_li, chinese)
math = change_score(name_li, math)
english = change_score(name_li,english)
phisics = change_score(name_li,phisics)
chemistry = change_score(name_li,chemistry)
biology = change_score(name_li,biology)
politics = change_score(name_li,politics)
history = change_score(name_li,history)
geography = change_score(name_li,geography)

s = '姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理\n'

for i in range(0, len(name_li) - 1):
    s = s + str(name_li[i])
    s = s + ' ' + str(chinese[name_li[i]])
    s = s + ' ' + str(math[name_li[i]])
    s = s + ' ' + str(english[name_li[i]])
    s = s + ' ' + str(phisics[name_li[i]])
    s = s + ' ' + str(chemistry[name_li[i]])
    s = s + ' ' + str(biology[name_li[i]])
    s = s + ' ' + str(politics[name_li[i]])
    s = s + ' ' + str(history[name_li[i]])
    s = s + ' ' + str(geography[name_li[i]])
    s = s + '\n'

f = open(path,'w')
f.write(s)
f.close()