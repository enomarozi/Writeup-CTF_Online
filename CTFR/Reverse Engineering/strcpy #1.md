<h1><b>strcpy #1</b></h1>
<pre>
Apa itu strcpy pada C++ ? strcpy adalah sebuah fungsi yang memindahkan / menduplikat / menambahkan karakter pada pointer yang di tentukan. Nah coba Reverse Attachment yang diberikan.

Download : <a href='https://mega.nz/file/skAxGaTD#4bcKaublTSHcqswF0HWbXIKhHDTNZVh1sfVcMug97Ho'>strcpy #1</a>

</pre>
<h3><b>Solution</b></h3>
<p>Lakukan Disassembler pada fungsi main dengn GDB tool, dan perhatikan operasi add dan mov</p>

```console
root@Python:/home/venom/Downloads# gdb ./strcpy 
GNU gdb (Debian 9.2-1) 9.2
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./strcpy...
(No debugging symbols found in ./strcpy)
(gdb) disas main
Dump of assembler code for function main:
   0x00000000000011a9 <+0>:	endbr64 
   0x00000000000011ad <+4>:	push   %rbp
   0x00000000000011ae <+5>:	mov    %rsp,%rbp
   0x00000000000011b1 <+8>:	sub    $0x70,%rsp
   0x00000000000011b5 <+12>:	mov    %fs:0x28,%rax
   0x00000000000011be <+21>:	mov    %rax,-0x8(%rbp)
   0x00000000000011c2 <+25>:	xor    %eax,%eax
   0x00000000000011c4 <+27>:	lea    -0x70(%rbp),%rax
   0x00000000000011c8 <+31>:	movl   $0x52465443,(%rax)
   0x00000000000011ce <+37>:	movw   $0x7b,0x4(%rax)
   0x00000000000011d4 <+43>:	lea    -0x70(%rbp),%rax
   0x00000000000011d8 <+47>:	add    $0x5,%rax
   0x00000000000011dc <+51>:	movw   $0x3433,(%rax)
   0x00000000000011e1 <+56>:	movb   $0x0,0x2(%rax)
   0x00000000000011e5 <+60>:	lea    -0x70(%rbp),%rax
   0x00000000000011e9 <+64>:	add    $0x7,%rax
   0x00000000000011ed <+68>:	movw   $0x7973,(%rax)
   0x00000000000011f2 <+73>:	movb   $0x0,0x2(%rax)
   0x00000000000011f6 <+77>:	lea    -0x70(%rbp),%rax
   0x00000000000011fa <+81>:	add    $0x9,%rax
   0x00000000000011fe <+85>:	movw   $0x5f,(%rax)
   0x0000000000001203 <+90>:	lea    -0x70(%rbp),%rax
   0x0000000000001207 <+94>:	add    $0xa,%rax
   0x000000000000120b <+98>:	movl   $0x727473,(%rax)
   0x0000000000001211 <+104>:	lea    -0x70(%rbp),%rax
   0x0000000000001215 <+108>:	add    $0xd,%rax
   0x0000000000001219 <+112>:	movl   $0x79703063,(%rax)
   0x000000000000121f <+118>:	movw   $0x5f,0x4(%rax)
--Type <RET> for more, q to quit, c to continue without paging--
   0x0000000000001225 <+124>:	lea    -0x70(%rbp),%rax
   0x0000000000001229 <+128>:	add    $0x12,%rax
   0x000000000000122d <+132>:	movw   $0x66,(%rax)
   0x0000000000001232 <+137>:	lea    -0x70(%rbp),%rax
   0x0000000000001236 <+141>:	add    $0x13,%rax
   0x000000000000123a <+145>:	movl   $0x7d67346c,(%rax)
   0x0000000000001240 <+151>:	movb   $0x0,0x4(%rax)
   0x0000000000001244 <+155>:	lea    0xdbe(%rip),%rsi        # 0x2009
   0x000000000000124b <+162>:	lea    0x2dee(%rip),%rdi        # 0x4040 <_ZSt4cout@@GLIBCXX_3.4>
   0x0000000000001252 <+169>:	callq  0x1090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
   0x0000000000001257 <+174>:	lea    0xdc2(%rip),%rsi        # 0x2020
   0x000000000000125e <+181>:	lea    0x2ddb(%rip),%rdi        # 0x4040 <_ZSt4cout@@GLIBCXX_3.4>
   0x0000000000001265 <+188>:	callq  0x1090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
   0x000000000000126a <+193>:	mov    $0x0,%eax
   0x000000000000126f <+198>:	mov    -0x8(%rbp),%rdx
   0x0000000000001273 <+202>:	xor    %fs:0x28,%rdx
   0x000000000000127c <+211>:	je     0x1283 <main+218>
   0x000000000000127e <+213>:	callq  0x10a0 <__stack_chk_fail@plt>
   0x0000000000001283 <+218>:	leaveq 
   0x0000000000001284 <+219>:	retq   
End of assembler dump.
```
<p>Disana terdapat nilai hexa yang memungkinkan dapat mencetak ascii text</p>

```python
print(bytes.fromhex('7d67346c665f797030637274735f797334337b52465443')[::-1].decode('ascii'))

```
<h3><b>Flag</b></h3>
<pre>
CTFR{34sy_strc0py_fl4g}
</pre>
