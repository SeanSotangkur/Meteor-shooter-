from collections import defaultdict
find=input("enter a account name ")
file=open(find+".txt","r")
f = []
for line in file:
  print(1)
  f.append(line)

stats_score={}
element=[]
for line in f:
  print(1)
  line=line.strip()
  line=line.split(" ")
  element.append((line[5],line[1]))
stats_score=defaultdict(list)
for key, value in element:
  stats_score[key].append(value)
  print(key,value)
print(stats_score)
stats_time={}
element=[]

for line in f:
  print(10)
  line=line.strip()
  line=line.split(" ")
  element.append((line[5],line[9]))

stats_time=defaultdict(list)
for key, value in element:
  stats_time[key].append(value)
print(stats_time)