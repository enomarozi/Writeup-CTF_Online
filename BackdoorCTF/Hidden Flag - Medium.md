<h1><b>Hidden Flag - Medium</h1></b>
<pre>
n00b became depressed when 'Pro' found the flag in his binary in a matter of seconds. 
This time he hid the flag a little more securely. 
See if you can still find it: <a href="http://static.beast.sdslabs.co/static/HIDE-MEDIUM/hide_medium">file</a>
</pre>
<h3><b>Solution</h3></b>
<p>Pertama saya decompile file, dan disana terdapat beberapa fungsi pertama saya perhatikan fungsi main(),
disana hanya ada fungsi print. lanjut ke fungsi print_flag(), disana terdapat banyak operasi yang saya tidak tau apa eksekusinya</p>
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/Hidden%20Flag%20-%20Medium.jpg">
</p>
<p>Dan, karena fungsi main() tidak terkait dengan fungsi print_flag(), maka langsung saja jalankan tools gdb untuk break fungsi main(), dan compile --> run fungsi print_flag()</p>

```console
root@Python:/home/venom/Downloads# chmod +x hide_medium 
root@Python:/home/venom/Downloads# gdb ./hide_medium 
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
Reading symbols from ./hide_medium...
(No debugging symbols found in ./hide_medium)
(gdb) break main
Breakpoint 1 at 0x8048574
(gdb) r
Starting program: /home/venom/Downloads/hide_medium 

Breakpoint 1, 0x08048574 in main ()
(gdb) compile code -- print_flag()
warning: function has unknown return type; assuming int
841f980abd04b26fe804ca0c207a574bef504cb6a3c3599a449e845ca993d2cf
(gdb) 
```
<h3><b>Flag</b></h3>
<pre>
841f980abd04b26fe804ca0c207a574bef504cb6a3c3599a449e845ca993d2cf
</pre>
