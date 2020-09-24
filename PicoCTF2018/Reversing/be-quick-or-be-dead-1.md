<h1><b>be-quick-or-be-dead-1</h1></b>
<pre>
You find this when searching for some music, which leads you to <a href='https://2018shell.picoctf.com/static/353d7b6da455d29f7e8701952db901cb/be-quick-or-be-dead-1'>be-quick-or-be-dead-1</a>. 
Can you run it fast enough? You can also find the executable 
in /problems/be-quick-or-be-dead-1_4_98374389c5652d0b16055427532f098f.
</pre>
</b><h3>Solution</h3></b>
<p>Diberikan 1 file elf-64bit, dan eksekusi file</p>

```console
root@Python:/home/venom/Downloads# ./be-quick-or-be-dead-1 
Be Quick Or Be Dead 1
=====================

Calculating key...
You need a faster machine. Bye bye.
root@Python:/home/venom/Downloads# 
```
<p>Jika file dieksekusi maka akan muncul pesan tanpa flag. Lanjut decompile dan lihat pseudocode pada file dengan ghidra atau IDA tool, disini saya mendapatkan fungsi main dari progarm</p>

```c
undefined8 main(void)
{
  header();
  set_timer();
  get_key();
  print_flag();
  return 0;
}
```
<p align='center'>Disana fungsi main menjalankan 4 macam fungsi yaitu header, set_timer, get_key dan print_flag. sesuai yang kita butuhkan hanyalah get_key() dan print_flag() untuk menampilkan flag yang ter-encrypt</p>
<p>Eksekusi hanya ke-2 fungsi dengan tool gdb</p>

```console
root@Python:/home/venom/Downloads# gdb ./be-quick-or-be-dead-1 
GNU gdb (Debian 9.2-1) 9.2
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./be-quick-or-be-dead-1...
(No debugging symbols found in ./be-quick-or-be-dead-1)
(gdb) b *main
Breakpoint 1 at 0x400827
(gdb) r
Starting program: /home/venom/Downloads/be-quick-or-be-dead-1 

Breakpoint 1, 0x0000000000400827 in main ()
(gdb) compile code -- get_key()
warning: function has unknown return type; assuming int
Calculating key...
Done calculating key
(gdb) compile code -- print_flag()
warning: function has unknown return type; assuming int
Printing flag:
picoCTF{why_bother_doing_unnecessary_computation_402ca676}
(gdb) 

```
</b><h3>Flag</h3></b>
<pre>
picoCTF{why_bother_doing_unnecessary_computation_402ca676}
</pre>
