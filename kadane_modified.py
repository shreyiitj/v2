# kadane's with Max Sum with Min length.
# Need a max sum subarray - print sum and indexes, If there are more than 1 then give the smallest.


arr = [1,4,-2,7,-10,5,5]

max_sum,summ = arr[0], arr[0]
x,y,x_temp = 0,0,0
for i in range(1,len(arr)):
	summ += arr[i]
	if summ > max_sum:
		max_sum = summ
		y = i
		x = x_temp
	if summ == max_sum:
		if (y-x) > (i-x_temp):
			y=i
			x = x_temp
	if summ <= 0: 				# will choose max length if 2 subaarys are possible ==> NO
		summ = 0 
		x_temp = i+1


print(max_sum,x,y)
