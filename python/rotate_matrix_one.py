# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n = int(raw_input())
ls = []
for i in range(n):
    row = map(int,raw_input().split())
    if len(row) != n:
        print "ERROR"
        sys.exit()
    else:
        ls.append(row)

matrix =[[0]*n for x in range(n)]

    
num_same = n - 1
circle = n/2
flag = 0
for i in range(circle):
    if flag == 0:
        for j in range(i+1,i+1+num_same):
            matrix[i][j] = ls[i][j-1]
        flag += 1
    if flag == 1:
        for j in range(i+1,i+1+num_same):
            matrix[j][n-i-1] = ls[j-1][n-i-1]
        flag += 1
    if flag == 2:
        for j in range(n-i-2,n-i-2-num_same,-1):
            matrix[n-i-1][j] = ls[n-i-1][j+1]
        flag += 1
    if flag ==3 :
        for j in range(n-i-2,n-i-2-num_same,-1):
            matrix[j][i] = ls[j+1][i]
        flag =0
    num_same = num_same - 2
    
if n%2 != 0:
    matrix[n/2][n/2] = ls[n/2][n/2]

for i, row in enumerate(matrix):
    print ' '.join(map(str,row))
        
        
        
