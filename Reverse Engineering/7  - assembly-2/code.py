
def asm2(int1, int2):
    local1 = int2
    local2 = int1
    while int1 < 0x1d89:
        local1 += 1
        int1 += 0x64
    return local1

print hex(asm2(0x4, 0x2d))
