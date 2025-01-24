org 0x7C00

init:
    mov bx, 0
    mov es, bx
set_display_segment:
    mov bl, [es:0x410] ; read equipment type from BIOS Data Area
    mov bh, [es:bx + equipment_type_to_video_segment_table] ; convert this to the top byte of the video memory segment
    mov bl, 0
    mov ds, bx
    mov bh, 0
print_hello:
    mov al, 'l'
    mov byte [bx],    'H'
    mov byte [bx+2],  'e'
    mov byte [bx+4],  al
    mov byte [bx+6],  al
    mov byte [bx+8],  'o'
    mov byte [bx+10], ','
    mov byte [bx+12], ' '
    mov byte [bx+14], 'W'
    mov byte [bx+16], 'o'
    mov byte [bx+18], 'r'
    mov byte [bx+20], al
    mov byte [bx+22], 'd'
    mov byte [bx+24], '!'
    mov ds, bx ; reset data segment to avoid side effects
; install a new illegal instruction handler that calls itself
    mov word [es:bx + 6 * 4], illegal_instruction_handler
    mov [es:bx + 6 * 4 + 2], bx
    mov cx, sp ; save stack pointer
illegal_instruction_handler:
    mov sp, cx ; reload stack pointer to prevent stack overflow
    mov cs, bx ; continue on an 8086, or enter infinite loop of exceptions on a 286+

equipment_type_to_video_segment_table:
%rep 4
    times 32 db 0
    times 16 db 0xB8 ; type & 0x30 = 0x20; colour display, video memory starts at segment 0xB800
    times 16 db 0xB0 ; type & 0x30 = 0x30; monochrome display, video memory starts at segment 0xB000
%endrep

times 510-($-$$) db 0
dw 0xAA55
