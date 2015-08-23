
def partition(ls,s,t):
	pivot_val = ls[t]
	i = s
	j = s
	while j < t:
		if ls[j] <= pivot_val:
			temp = ls[j]
			ls[j] = ls[i]
			ls[i] = temp
			i += 1
		j += 1
	temp = ls[t]
	ls[t] = ls[i]
	ls[i] = temp
	return i
def quicksort_inplace(ls,s,t):
	if s < t:
		p = partition(ls,s,t)
		quicksort_inplace(ls,s,p-1)
		quicksort_inplace(ls,p+1,t)

testcase = input()
for _ in range(testcase):
	ls = [int(x) for x in raw_input().strip().split()]
	quicksort_inplace(ls,0,len(ls)-1)
	print " ".join(map(str,ls))
