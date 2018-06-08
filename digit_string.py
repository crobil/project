def DashInsert(input):
	res = ''
	for idx, var in enumerate(input):
		if idx == 0:
			res += '%s' % (var)
		elif (int(var) % 2 == int(input[idx-1]) % 2) and int(var) % 2 == 1:
			res += '-%s' % (var)
		elif (int(var) % 2 == int(input[idx-1]) % 2) and int(var) % 2 == 0:
			res += '+%s' % (var)
		else:
			res += '%s' % (var)

	return res

print DashInsert('4546793')
