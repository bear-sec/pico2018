.intel_syntax noprefix
.bits 32
	
.global asm0

asm0:
	push	ebp
	mov	ebp,esp
	mov	eax,DWORD PTR [ebp+0x8] ; first param (0xaa)
	mov	ebx,DWORD PTR [ebp+0xc] ; second param (0xf2)
	mov	eax,ebx ; eax has 0xf2
	mov	esp,ebp
	pop	ebp	
	ret
	
asm0(0xaa, 0xf2) = 0xf2
