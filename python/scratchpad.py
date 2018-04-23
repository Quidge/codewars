from functools import reduce
def thing(array):
	answer = [x*(x+1) for x in array[:len(array)-1]]
	print(answer)
	return answer

#print(thing([1,2,3,4]))

#thing([1,2,3,4])

arr = [1,2,3,4]

def persistance(n):
	answer = reduce(lambda x, y: x * y, n)
	return answer

#print(persistance(arr))

# reduce(lambda x, y: x * y, [int(ch) for ch in string])

print(reduce(lambda x, y: x * y, [int(ch) for ch in str(39)]))