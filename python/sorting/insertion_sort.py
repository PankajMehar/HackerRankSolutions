def insertion_sort(ls):
	i = 1
	while i < len(ls):
		j = i-1
		key = ls[i]
		while j >= 0:
			if ls[j] > key:
				ls[j+1] = ls[j]
				ls[j] = key
			j -= 1
		i += 1
	return ls
testcase = input()
print testcase
for _ in range(testcase):
	ls = [int(x) for x in raw_input().strip().split()]
	print "old:" + " ".join(map(str,ls))
	ls_new = insertion_sort(ls)
	print "new:" + " ".join(map(str,ls_new))
