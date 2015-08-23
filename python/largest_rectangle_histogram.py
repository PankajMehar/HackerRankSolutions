#Find the largest rectangular area possible in a given histogram 
#where the largest rectangle can be made of a number of contiguous bars. 
#For simplicity, assume that all bars have same width and the width is 1 unit.
#For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 2, 6}.
#The largest possible rectangle possible is 12 

#1) Create an empty stack.

#2) Start from first bar, and do following for every bar 'hist[i]'' where 'i' varies from 0 to n-1.
#  a) If stack is empty or hist[i] is higher than the bar at top of stack, then push 'i' to stack.
#  b) If this bar is smaller than the top of stack, then keep removing the top of stack while top of 
#the stack is smaller. Let the removed bar be hist[tp]. Calculate area of rectangle with hist[tp] as 
#smallest bar. For hist[tp], the 'left index' is previous (previous to tp) item in stack and 'right index' is 'i' (current index).

#3) If the stack is not empty, then one by one remove all bars from stack and do step 2.b for every removed bar.

from collections import deque

def largestRec(ls):
	stk = deque()
	max_area = 0
	n = len(ls)
	i = 0

	while i<n:
		if not stk or ls[stk[-1]] <= ls[i]:
			stk.append(i)
			i += 1
		elif ls[stk[-1]] > ls[i]:
			temp = stk.pop()
			if stk:
				area = ls[temp] * (i-stk[-1]-1)
			else:
				area = ls[temp] * i
			if area > max_area:
				max_area = area
	while stk:
		temp = stk.pop()
		if stk:
			area = ls[temp] * (i-stk[-1]-1)
		else:
			area = ls[temp] * i
		if area > max_area:
			max_area = area
	return max_area

ls = [6,2,5,4,5,1,6]
print largestRec(ls)



