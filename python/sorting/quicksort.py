def quicksort(ls):
	if len(ls) <= 1:
		return ls
	pivot_val = ls[0]
	pivot_ind = 0
	i = 1
	while i < len(ls):
		if ls[i] < pivot_val:
			temp = ls[i]
			del ls[i]
			ls.insert(0,temp)
			pivot_ind += 1

		i += 1
	p = quicksort(ls[0:pivot_ind])
	p.append(pivot_val)
	p.extend(quicksort(ls[pivot_ind+1:]))
	return p

testcase = input()
for _ in range(testcase):
	ls = [int(x) for x in raw_input().strip().split()]
	ls_new = quicksort(ls)
	print " ".join(map(str,ls_new))
