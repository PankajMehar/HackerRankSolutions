def mergesort(ls):
	



testcase = input()
for _ in range(testcase):
	ls = [int(x) for x in raw_input().strip().split()]
	ls_new = mergesort(ls)
	print " ".join(map(str,ls_new))

