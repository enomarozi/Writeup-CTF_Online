<h1>GDB baby step 3</h1>
<h3>Description</h3>
<pre>
Now for something a little different. 0x2262c96b is loaded into memory in the main function. Examine byte-wise the memory that the constant is loaded in by using the GDB command x/4xb addr. The flag is the four bytes as they are stored in memory. If you find the bytes 0x11 0x22 0x33 0x44 in the memory location, your flag would be: picoCTF{0x11223344}.
Debug <a href='https://artifacts.picoctf.net/c/531/debugger0_c'>this</a>.
</pre>
<h3>Solution</h3>
<p>Intruksi soal</p>

```assembly
gef➤  disas main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:	endbr64
   0x000000000040110a <+4>:	push   rbp
   0x000000000040110b <+5>:	mov    rbp,rsp
=> 0x000000000040110e <+8>:	mov    DWORD PTR [rbp-0x14],edi
   0x0000000000401111 <+11>:	mov    QWORD PTR [rbp-0x20],rsi
   0x0000000000401115 <+15>:	mov    DWORD PTR [rbp-0x4],0x2262c96b
   0x000000000040111c <+22>:	mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040111f <+25>:	pop    rbp
   0x0000000000401120 <+26>:	ret
End of assembler dump.
```
<p>Set Breakpint main dan jump ke 0x000000000040111f</p>

```console
gef➤  b main
Breakpoint 1 at 0x40110e
gef➤  run
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0x00007fffffffe100│+0x0000: 0x0000000000000001	 ← $rsp, $rbp
0x00007fffffffe108│+0x0008: 0x00007ffff7c29f68  →  <__libc_start_call_main+0078> mov edi, eax
0x00007fffffffe110│+0x0010: 0x0000000000000000
0x00007fffffffe118│+0x0018: 0x0000000000401106  →  <main+0000> endbr64 
0x00007fffffffe120│+0x0020: 0x00000001ffffe200
0x00007fffffffe128│+0x0028: 0x00007fffffffe218  →  0x00007fffffffe4e2  →  "/home/venom/Downloads/debugger0_c"
0x00007fffffffe130│+0x0030: 0x00007fffffffe218  →  0x00007fffffffe4e2  →  "/home/venom/Downloads/debugger0_c"
0x00007fffffffe138│+0x0038: 0x5ee5abda7a2b5c35
───────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:64 ────
     0x401106 <main+0000>      endbr64 
     0x40110a <main+0004>      push   rbp
     0x40110b <main+0005>      mov    rbp, rsp
●→   0x40110e <main+0008>      mov    DWORD PTR [rbp-0x14], edi
     0x401111 <main+000b>      mov    QWORD PTR [rbp-0x20], rsi
     0x401115 <main+000f>      mov    DWORD PTR [rbp-0x4], 0x2262c96b
     0x40111c <main+0016>      mov    eax, DWORD PTR [rbp-0x4]
     0x40111f <main+0019>      pop    rbp
     0x401120 <main+001a>      ret    
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "debugger0_c", stopped 0x40110e in main (), reason: BREAKPOINT
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x40111c → main()
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  until *0x40111c
●    0x40110e <main+0008>      mov    DWORD PTR [rbp-0x14], edi
     0x401111 <main+000b>      mov    QWORD PTR [rbp-0x20], rsi
     0x401115 <main+000f>      mov    DWORD PTR [rbp-0x4], 0x2262c96b
 →   0x40111c <main+0016>      mov    eax, DWORD PTR [rbp-0x4]
     0x40111f <main+0019>      pop    rbp
     0x401120 <main+001a>      ret    
     0x401121                  cs     nop WORD PTR [rax+rax*1+0x0]
     0x40112b                  nop    DWORD PTR [rax+rax*1+0x0]
     0x401130 <__libc_csu_init+0000> endbr64 
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "debugger0_c", stopped 0x40111c in main (), reason: TEMPORARY BREAKPOINT
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x40111c → main()
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  p/x $rbp-0x4
$1 = 0x7fffffffe0fc
gef➤  x/4bx 0x7fffffffe0fc
0x7fffffffe0fc:	0x6b	0xc9	0x62	0x22

```
<h3>Flag</h3>
<pre>
picoCTF{0x6bc96222}
</pre>
