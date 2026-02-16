<h1>Forky</h1>
<h3>Description</h3>
<pre>
In <a href='https://challenge-files.picoctf.net/c_fickle_tempest/da39d11624b65446205d9525558d877c27faa3bc76277546d5317d7fe5130182/vuln'>this program</a>, identify the last integer value that is passed as parameter to the function doNothing().
</pre>
<h3>Solution</h3>
<label>Disassembly program dengan ghidra</label>

```c
undefined4 main(void)

{
  int *piVar1;
  
  piVar1 = mmap((void *)0x0,4,3,0x21,-1,0);
  *piVar1 = 1000000000;
  fork();
  fork();
  fork();
  fork();
  *piVar1 = *piVar1 + 0x499602d2;
  doNothing();
  return 0;
}
```
<label>Fork merupakan system call Membuat proses baru(Child process), jadi jika 4 fork() maka 2^4 = 16 process, jadi</label>
<pre>
1000000000 + (2**4 * 0x499602d2)
</pre>

```python3
import ctypes
ctypes.c_int32(1000000000 + (2**4 * 0x499602d2))
c_int(-721750240)
```
<h3>Flag</h3>
<pre>
picoCTF{-721750240}
</pre>
