from collections import deque

n = int(raw_input())
ls = []
for i in range(n):
    ls.append(map(int,raw_input().split()))
limit = int(raw_input())

flag = 0
d = deque((),limit)
for i in range(len(ls)):
    for j in range(len(ls[i])):
        if ls[i][j] in d:
            print "YES"
            flag = 1
        else:
            d.append(ls[i][j])
if flag == 0:
    print "NO"
            
