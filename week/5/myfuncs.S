section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file

my_memset:
        push rbp
        mov rbp, rsp
        xor rcx, rcx

set_loop:
        cmp rcx, rdx
        jz set_end
        mov byte [rdi + rcx], sil
        inc rcx
        jmp set_loop
set_end:
        mov rsp, rbp
        pop rbp
        ret


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file

my_strncpy:
        push rbp
        mov rbp, rsp
        xor rcx, rcx

cpy_loop:
        cmp rcx, rdx
        jz cpy_end
        mov al, byte [rsi + rcx]
        mov byte [rdi + rcx], al
        inc rcx
        jmp cpy_loop
cpy_end:
        mov rsp, rbp
        pop rbp
        ret
