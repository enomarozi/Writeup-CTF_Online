<b><h1>Hidden Flag - Easy</b></h1>
<pre>
n00b just learnt about binary files. He tried to hide a flag in it. Here is the <a href="http://static.beast.sdslabs.co/static/HIDE-EASY/hide_easy">file</a>.
</pre>
<h3><b>Solution</b></h3>
<p>Sederhana saja, dengan perintah strings pada terminal</p>

```console
root@Python:/home/venom/Downloads# strings -a hide_easy | head -n 15
/lib/ld-linux.so.2
;%dD&
libc.so.6
_IO_stdin_used
puts
printf
__libc_start_main
__gmon_start__
GLIBC_2.0
PTRh
QVhl
[^_]
939d9556640d4
47f5847d92e9fbbd4d762036ff684ccde6a80d3a171c4dcd0b724fae25826c36
What do you think you will get here?
root@Python:/home/venom/Downloads#
```
<h3><b>Flag</b></h3>
<pre>
47f5847d92e9fbbd4d762036ff684ccde6a80d3a171c4dcd0b724fae25826c36
</pre>
