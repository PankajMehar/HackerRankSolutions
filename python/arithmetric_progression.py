n = int(raw_input())

ls = raw_input().split()

ls = map(int,ls)

diff1 = ls[1]-ls[0]
diff2 = ls[2]-ls[1]
if diff1 == diff2:
    diff = diff1
else:
    diff = min(diff1,diff2)
    
i = 0
while i < n-1:
    if ls[i] + diff != ls[i+1]:
        print ls[i] + diff
    i += 1
