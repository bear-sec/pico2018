import struct
import binascii

a = open(r'C:\Users\Gera\Documents\GitHub\pico2018\Forensics\15 - LoadSomeBits\pico2018-special-logo.bmp',
         'rb').read()
#data_offset = struct.unpack("<I",a[0xa:0xe])[0] # bitmap offset
data_offset = 0x30
print "bmp data at: ", hex(data_offset)
for i in range(8): # possible offsets
    data = a[data_offset+i:data_offset+0x200+i]
    bits = [ord(x)&1 for x in data]
    dwords = [''.join([str(y) for y in bits[x*8:x*8+8]]) for x in range(len(bits)/8)]
    flag = ''.join([chr(int(x,2)) for x in dwords])
    print "possible flag: " + flag + " at offset: " + str(i)


