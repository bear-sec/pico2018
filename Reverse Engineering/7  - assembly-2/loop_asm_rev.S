.intel_syntax noprefix
.bits 32
	
.global asm2

asm2:
	push   	ebp
	mov    	ebp,esp
	sub    	esp,0x10
	mov    	eax,DWORD PTR [ebp+0xc] ; eax = 0x2d
	mov 	DWORD PTR [ebp-0x4],eax ; some_local = 0x2d
	mov    	eax,DWORD PTR [ebp+0x8] ; eax = 0x4
	mov		DWORD PTR [ebp-0x8],eax ; some_local2 = 0x4
	jmp    	part_b
part_a:	
	add    	DWORD PTR [ebp-0x4],0x1 ; 0x2d + 1
	add		DWORD PTR [ebp+0x8],0x64 ; 0x4 + 0x64
part_b:	
	cmp    	DWORD PTR [ebp+0x8],0x1d89 ; 0x4 < 0x1d89
	jle    	part_a ; jmp taken
	mov    	eax,DWORD PTR [ebp-0x4]
	mov		esp,ebp
	pop		ebp
	ret

asm2(0x4, 0x2d)