def decodeMorse(morse_code):
	# ToDo: Accept dots, dashes and spaces, return human-readable message
	_list = morse_code.split('   ')
	res = ''
	for item in _list:
		for x in item.split():
			res += MORSE_CODE[x]
		res += ' '

	return res.rstrip().lstrip()


