<h1>Need For Speed</h1>
<h3>Description</h3>
<pre>
The name of the game is <a href='https://www.youtube.com/watch?v=8piqd2BWeGI'>speed</a>. Are you quick enough to solve this problem and keep it above 50 mph? <a href='https://jupiter.challenges.picoctf.org/static/cd51b2c95be9f3626db6fe6665afb5a3/need-for-speed'>need-for-speed</a>.
</pre>
<h3>Solution</h3>
<p>Saat dirunning terjadi timeout pada SIGNAL ALRM, dari fungsi main langsung saja ke get_key() fungsi</p>

```console
gef➤  disas main
Dump of assembler code for function main:
   0x000000000000091a <+0>:	push   rbp
   0x000000000000091b <+1>:	mov    rbp,rsp
   0x000000000000091e <+4>:	sub    rsp,0x10
   0x0000000000000922 <+8>:	mov    DWORD PTR [rbp-0x4],edi
   0x0000000000000925 <+11>:	mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000000929 <+15>:	mov    eax,0x0
   0x000000000000092e <+20>:	call   0x8d8 <header>
   0x0000000000000933 <+25>:	mov    eax,0x0
   0x0000000000000938 <+30>:	call   0x82f <set_timer>
   0x000000000000093d <+35>:	mov    eax,0x0
   0x0000000000000942 <+40>:	call   0x87d <get_key>
   0x0000000000000947 <+45>:	mov    eax,0x0
   0x000000000000094c <+50>:	call   0x8ac <print_flag>
   0x0000000000000951 <+55>:	mov    eax,0x0
   0x0000000000000956 <+60>:	leave
   0x0000000000000957 <+61>:	ret
End of assembler dump.
gef➤  break *main
Breakpoint 1 at 0x91a
gef➤  r
Starting program: /home/venom/Downloads/need-for-speed 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x000055555540091a in main ()
gef➤  call (int) get_key()
Creating key...
Finished
$1 = 0x9
gef➤  c
Continuing.
Keep this thing over 50 mph!
============================

Creating key...

Program received signal SIGALRM, Alarm clock.
Finished
Printing flag:
PICOCTF{Good job keeping bus #24c43740 speeding along!}
[Inferior 1 (process 3609) exited normally]
```

<h3>Flag</h3>
<pre>
PICOCTF{Good job keeping bus #24c43740 speeding along!}
</pre>
