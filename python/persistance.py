from functools import reduce


def persistence(n):

	def recursive(num, ctr):
		if len(str(num)) == 1:
			return ctr
		else:
			new_num = reduce(lambda x, y: x * y, [int(ch) for ch in str(num)])
			return recursive(new_num, ctr + 1)

	return recursive(n, 0)

print(persistence(39))
