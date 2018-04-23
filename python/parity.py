def find_outlier(int_array):
	outlier = None

	# determines whether the list is even or odd. it's only necessary to
	# check the first three values of the list to determine this.
	odds = [x for x in int_array[:3] if x % 2 == 1]

	# if the resultant list is > 1, the entire list must be odd. otherwise,
	# if len(odds) == 0, the list is even 
	# else if len(odds) == 1, the list is even AND the outlier is within the
	# first 3 values.
	
	if len(odds) > 1:
		outlier = [x for x in int_array if x % 2 == 0][0]
	else:
		outlier = [x for x in int_array if x % 2 == 1][0]
	return outlier

even_array = [3, 4, 2, 10, 12]
odd_array = [5, 7, 2, 11, 25, 27]

print('even array: ', find_outlier(even_array))
print('odd array: ', find_outlier(odd_array))
#print(array[:2])