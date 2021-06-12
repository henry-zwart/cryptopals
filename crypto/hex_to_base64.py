base64 = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
#hexa = 0x49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
hexa = 0x61
mask = 63

out = ''

maxShift = hexa.bit_length()
temp = hexa
shifts = 0
while shifts < maxShift:
    dig = temp & mask
    temp = temp >> 6
    shifts += 6
    out = base64[dig] + out
print(out)


# Task 2
a = 0x1c0111001f010100061a024b53535009181c
b = 0x686974207468652062756c6c277320657965
out = ''
tempA = a
tempB = b
mask = 1
out = tempA ^ tempB
print(hex(out))
