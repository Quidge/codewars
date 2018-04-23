def song_decoder(string):
	import re
	return re.sub('[WUB]+', " ", string).strip()

print(song_decoder('thisisWUBIWUBWUBIAMWUBstringWUB'))