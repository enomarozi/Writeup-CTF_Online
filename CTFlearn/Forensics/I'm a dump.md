<h1><b>I'm a dump</h1></b>
<pre>
The keyword is hexadecimal, and removing an useless H.E.H.U.H.E. from the flag. 
The flag is in the format CTFlearn{*}

<a href='https://ctflearn.com/challenge/download/883'>file</a>
</pre>
</b><h3>Solution</h3></b>
<p>Eksekusi perintah strings dan lihat setiap line hasilnya</p>

```console
root@Python:/home/venom/Downloads# strings -a file | head -n 15
/lib64/ld-linux-x86-64.so.2
libc.so.6
__stack_chk_fail
__cxa_finalize
__libc_start_main
GLIBC_2.2.5
GLIBC_2.4
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u3UH
CTFlearnH
{fl4ggyfH
l4g}H
[]A\A]A^A_
root@Python:/home/venom/Downloads#
```
<p>Disana terdapat <b>CTFlearnH</b>,<b>{fl4gghyfH</b> dan <b>l4g}H</b>, satukan semuanya dengan menghapus char sesuai pada soal yang hasilnya berupa flag</p>
</b><h3>Flag</h3></b>
<pre>
CTFlearn{fl4ggyflag}
</pre>
