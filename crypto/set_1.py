import math

"""def hex_to_int(hex):
	ascii = ord(hex)
	if 0x61 <= ascii:
		int_out = ascii - 87
	else:
		int_out = ascii - 48
	return int_out"""
	
	
def int_to_base64(int_in):
	if int_in <= 25:
		b64_out = int_in + 65
	elif int_in <= 51:
		b64_out = int_in + 71
	elif int_in <= 61:
		b64_out = int_in - 4
	elif int_in == 62:
		b64_out = 43
	else:
		b64_out = 47
		
	return b64_out
	
	
def hex_to_int(hexa):
	int = 0
	for char in hexa:
		int = int << 4
		ascii = ord(char)
		if 0x61 <= ascii:
			char_value = ascii - 87
		else:
			char_value = ascii - 48
		int += char_value
	return int

	
def int_to_hex(int_in):
	binary = int_to_binary(int_in, 0)
	mask = 15
	temp = int_in
	while len(binary)%4 != 0 and len(binary)/4 != 0:
		binary = '0' + binary
	
	out = ''	
	for i in range(int(len(binary)/4)):
		hex_value = mask & temp
		if hex_value <= 9:
			hex_char = hex_value + 48
		else:
			hex_char = hex_value + 87
		out += chr(hex_char)
		temp = temp >> 4
		
	return out[::-1]
	
	
def hex_to_base64(hex):
	binary = hex_to_int(hex)
	buffer = (6-len(hex)*4) % 6			# Number of zeros to append to bring length to multiple of 6
	for i in range(buffer):
		binary = binary << 1
	
	numBits = len(hex)*4 + buffer 
	numShifts = int(numBits/6 - 1)
	
	out = ''
	mask = 63 << (numShifts*6)
	while mask != 0:
		b64_temp = (mask & binary) >> (numShifts * 6)
		b64_char = int_to_base64(b64_temp)
		out = out + chr(b64_char)
		mask = mask >> 6
		numShifts -= 1
	return out
	

def hex_to_binary(hex):
	out = ''
	for char in hex:
		hex_value = hex_to_int(char)
		binary_char = int_to_binary(hex_value, 4)
		out += binary_char
	return out
		
	
	
def hex_to_ascii(hex):
	ascii = ''
	for i in range(0, len(hex), 2):
		char_value = hex_to_int(hex[i:i+2])
		char = chr(char_value)
		ascii += char
	return ascii

	
def int_to_binary(int_in, numBits):
	out = ''
	temp = int_in

	while temp != 0 or len(out) < numBits:
		if temp % 2 == 0:
			out += '0'
		else:
			out += '1'
		temp = math.floor(temp/2)
	return out[::-1]


def get_message_ranking(string):
	ranking = 'etaoinshrdlcumwfgypbvkjxqz'
	
	total = 0
	for char in string:
		if char in ranking:
			weight = ranking.find(char)
		else:
			weight = 4
		total += 1/(math.exp(weight))
	return total
	

def un_xor(bin1, bin2):
	""" Undoes the XOR operation given one of the input strings - bin1, and the result - bin2. """
	
	output = 0
	for i in range(len(bin1)):
		if bin2[i] == '0':
			if bin1[i] == '1':
				output += 1
		else:
			if bin1[i] == '0':
				output += 1
		output = output << 1
	return output >> 1

	
def fixed_xor(hex1, hex2):
	binXor = hex_to_int(hex1) ^ hex_to_int(hex2)
	
	numBits = len(hex1)*4
	numShifts = len(hex1) - 1
	
	out = ''
	mask = 15 << (numShifts*4)
	while mask != 0:
		hex_temp = (mask & binXor) >> (numShifts * 4)
		hex_char = int_to_hex(hex_temp)
		out = out + hex_char
		mask = mask >> 4
		numShifts -= 1
	return out
	

def single_byte_xor(hex):
	"""Didn't realize that should be checking all possible bytes (of which there are 256, not 16)."""
	ranking = [0 for i in range(16)]
	messages = ['' for i in range(16)]
	bin_in = hex_to_binary(hex)

	for i in range(16):
		temp_bin = bin_in
		xor_char = int_to_hex(i)
		xor_string = len(hex) * xor_char
		xor_bin = hex_to_binary(xor_string)
		while len(temp_bin) < len(xor_bin):
			temp_bin = '0' + temp_bin
		while len(xor_bin) < len(temp_bin):
			xor_bin = '0' + xor_bin
			
		print(fixed_xor(hex, xor_string))
		xor_result = un_xor(xor_bin, temp_bin)
		xor_hex = int_to_hex(xor_result)
		
		message = hex_to_ascii(xor_hex)
		ranking[i] = get_message_ranking(message)
		messages[i] = message
		print('message: ' + message)
	
	key = ranking.index(max(ranking))
	print(key)
	print(int_to_hex(key))
	return messages[key]
		
		
		
print(single_byte_xor('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))