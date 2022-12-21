global _start

exit:
	mov rax, 60
	mov rdi, 0
	syscall
print:
	mov rax, 1
	mov rdi, 1
	mov rsi, [rsp]
	mov rdx, 1
	syscall

	ret
input:
	mov rax, 0
	mov rax, 0
	mov rsi, [rsp]
	mov rdx, 1
	syscall

	ret
array_init:
	cmp ecx, 100
	je main

	push byte 0

	add ecx, 1
	jmp array_init
reset_pointer:
	cmp ecx, 0
	je main

	dec rsp
	sub ecx, 1

	jmp reset_pointer
_start:
	mov ecx, 0
	jmp array_init
main:
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	jmp loop0
loop0:
	cmp [rsp], byte 0
	je end_loop0
	inc rsp
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	dec rsp
	sub [rsp], byte 1
	jmp loop0
end_loop0:
	inc rsp
	call print
	add [rsp], byte 1
	call print
	add [rsp], byte 1
	call print
	add [rsp], byte 1
	call print
	add [rsp], byte 1
	call print
	add [rsp], byte 1
	call print
	add [rsp], byte 1
	call print
	dec rsp
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	add [rsp], byte 1
	call print
	jmp exit