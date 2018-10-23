import binascii

def bloop1(a):
    b = [chr(int(x,2)) for x in a.split(' ')]
    print ''.join(b)

def bloop2(a):
    print binascii.unhexlify(a)
    
def bloop3(a):
	b = [chr(int(x,8)) for x in a.split(' ')]
	print b

thing = raw_input()
print bloop1(thing)
thing = raw_input()
print bloop2(thing)
thing = raw_input()
print bloop3(thing)
