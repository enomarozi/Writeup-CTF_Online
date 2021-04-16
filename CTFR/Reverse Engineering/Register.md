<h1><b>Register</b></h1>
<pre>
Masih lanjut dengan First GDB, challenge kali ini akan membahas tentang Register pada GDB. Nah Coba Jalankan aplikasi tadi kemudian cari Address "main".

Challenge --> <a href='https://mega.nz/#!VlQ0HLJK!khDcuxnfhKKOmywe5JHdMPvKy5ReX6lYy5nAnMo5Be4'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Ikuti eksekusi terminal dibawah</p>

```console
root@Python:/home/venom/Downloads# chmod +x first_gdb 
root@Python:/home/venom/Downloads# gdb first_gdb 
GNU gdb (Debian 10.1-1.7) 10.1.90.20210103-git
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from first_gdb...
(No debugging symbols found in first_gdb)
(gdb) disas main
Dump of assembler code for function main:
   0x0000000000001189 <+0>:	endbr64 
   0x000000000000118d <+4>:	push   %rbp
   0x000000000000118e <+5>:	mov    %rsp,%rbp
   0x0000000000001191 <+8>:	lea    0xe71(%rip),%rdi        # 0x2009
   0x0000000000001198 <+15>:	call   0x1090 <puts@plt>
   0x000000000000119d <+20>:	lea    0xe7c(%rip),%rdi        # 0x2020
   0x00000000000011a4 <+27>:	call   0x1090 <puts@plt>
   0x00000000000011a9 <+32>:	mov    $0x0,%eax
   0x00000000000011ae <+37>:	pop    %rbp
   0x00000000000011af <+38>:	ret    
End of assembler dump.
(gdb) b *main
Breakpoint 1 at 0x1189
(gdb) r
Starting program: /home/venom/Downloads/first_gdb 

Breakpoint 1, 0x0000000008001189 in main ()                     
(gdb) 
```
<h3><b>Flag</b></h3>
<pre>
CTFR{0x8001189}
</pre>
