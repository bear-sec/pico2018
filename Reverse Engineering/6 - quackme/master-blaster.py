from Crypto.Util.strxor import strxor_c

a = 'You have now entered the Duck Web, and you'[:25]
b = [0x29, 0x6, 0x16, 0x4f, 0x2b, 0x35, 0x30, 0x1e, 0x51, 0x1b, 0x5b, 0x14, 0x4b, 0x8, 0x5d, 0x2b, 0x52, 0x17, 0x1, 0x57, 0x16, 0x11, 0x5c, 0x7, 0x5d]

ting = ''
for i in range(25):
        ting += chr(ord(a[i]) ^ b[i])
print ting