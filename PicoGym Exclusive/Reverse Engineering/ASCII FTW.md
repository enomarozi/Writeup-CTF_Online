<h1>ASCII FTW</h1>
<h3>Description</h3>
<pre>
This program has constructed the flag using hex ascii values. Identify the flag text by disassembling the program.
You can download the file from <a href='https://artifacts.picoctf.net/c/507/asciiftw'>here.</a>
</pre>
<h3>Description</h3>
<p>Dissas main check pada RBP-0x30 sesuai hint</p>

```console
┌──(root㉿Python)-[/home/venom/Downloads]
└─# gdb -q asciiftw.elf
GEF for linux ready, type `gef' to start, `gef config' to configure
93 commands loaded and 5 functions added for GDB 15.1 in 0.00ms using Python engine 3.12
Reading symbols from asciiftw.elf...
(No debugging symbols found in asciiftw.elf)
gef➤  b *0x0000555555555204
Breakpoint 1 at 0x555555555204
gef➤  r
Starting program: /home/venom/Downloads/asciiftw.elf 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x0000555555555204 in main ()

[ Legend: Modified register | Code | Heap | Stack | String ]
───────────────────────────────────────────────────────────────── registers ────
$rax   : 0x70              
$rbx   : 0x00007fffffffe388  →  0x00007fffffffe62d  →  "/home/venom/Downloads/asciiftw.elf"
$rcx   : 0x00007ffff7f97680  →  0x00007ffff7f98fc0  →  0x0000000000000000
$rdx   : 0x00007fffffffe398  →  0x00007fffffffe650  →  "LANG=C.UTF-8"
$rsp   : 0x00007fffffffe240  →  "picoCTF{ASCII_IS_EASY_7BCD971D}"
$rbp   : 0x00007fffffffe270  →  0x0000000000000001
$rsi   : 0x00007fffffffe388  →  0x00007fffffffe62d  →  "/home/venom/Downloads/asciiftw.elf"
$rdi   : 0x1               
$rip   : 0x0000555555555204  →  <main+009b> movsx eax, al
$r8    : 0x00005555555552b0  →  <__libc_csu_fini+0000> endbr64 
$r9    : 0x00007ffff7fcbe20  →  <_dl_fini+0000> push rbp
$r10   : 0x00007fffffffdfa0  →  0x0000000000800000
$r11   : 0x206             
$r12   : 0x0               
$r13   : 0x00007fffffffe398  →  0x00007fffffffe650  →  "LANG=C.UTF-8"
$r14   : 0x00007ffff7ffd000  →  0x00007ffff7ffe2e0  →  0x0000555555554000  →   jg 0x555555554047
$r15   : 0x0               
$eflags: [ZERO carry PARITY adjust sign trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x33 $ss: 0x2b $ds: 0x00 $es: 0x00 $fs: 0x00 $gs: 0x00 
───────────────────────────────────────────────────────────────────── stack ────
0x00007fffffffe240│+0x0000: "picoCTF{ASCII_IS_EASY_7BCD971D}"	 ← $rsp
0x00007fffffffe248│+0x0008: "ASCII_IS_EASY_7BCD971D}"
0x00007fffffffe250│+0x0010: "_EASY_7BCD971D}"
0x00007fffffffe258│+0x0018: 0x007d443137394443 ("CD971D}"?)
0x00007fffffffe260│+0x0020: 0x00007fffffffe340  →  0x0000000000000000
0x00007fffffffe268│+0x0028: 0x3b4bb1815ee95500
0x00007fffffffe270│+0x0030: 0x0000000000000001	 ← $rbp
0x00007fffffffe278│+0x0038: 0x00007ffff7de4dba  →  <__libc_start_call_main+007a> mov edi, eax
─────────────────────────────────────────────────────────────── code:x86:64 ────
   0x5555555551f8 <main+008f>      mov    BYTE PTR [rbp-0x13], 0x44
   0x5555555551fc <main+0093>      mov    BYTE PTR [rbp-0x12], 0x7d
   0x555555555200 <main+0097>      movzx  eax, BYTE PTR [rbp-0x30]
●→ 0x555555555204 <main+009b>      movsx  eax, al
   0x555555555207 <main+009e>      mov    esi, eax
   0x555555555209 <main+00a0>      lea    rdi, [rip+0xdf4]        # 0x555555556004
   0x555555555210 <main+00a7>      mov    eax, 0x0
   0x555555555215 <main+00ac>      call   0x555555555070 <printf@plt>
   0x55555555521a <main+00b1>      nop    
─────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "asciiftw.elf", stopped 0x555555555204 in main (), reason: BREAKPOINT
───────────────────────────────────────────────────────────────────── trace ────
[#0] 0x555555555204 → main()
────────────────────────────────────────────────────────────────────────────────
gef➤  x/s $rbp-0x30
0x7fffffffe240:	"picoCTF{ASCII_IS_EASY_7BCD971D}"

```

<p>Flag terdapat pada $rbp-0x30 s/d $rbp-0x12</p>
<h3>Flag</h3>
<pre>
picoCTF{ASCII_IS_EASY_7BCD971D}
</pre>
