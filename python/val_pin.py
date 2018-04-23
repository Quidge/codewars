def validate_pin(pin):
	# return true or false

	if len(pin) != 4 and len(pin) != 6:
		return False

	import re
	p = re.compile(r'\D')
	if p.search(pin):
		# print(p.match(pin))
		return False
	return True


print(validate_pin('2h&@'))
