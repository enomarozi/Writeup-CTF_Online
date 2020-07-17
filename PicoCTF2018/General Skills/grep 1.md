<h1><b>grep 1</h1></b>
<pre>
Can you find the flag in <a href="https://2018shell.picoctf.com/static/d7d1b6b0a64801c499a5eea393224811/file">file</a>? This would be really obnoxious to look through by hand, 
see if you can find a faster way. You can also find the file in /problems/grep-1_3_8d9cff3d178c231ab735dfef3267a1c2 on the shell server.
</pre>
</b><h3>Solution</h3></b>
<p>Eksekusi dengan perintah strings dan grep</p>

```console
root@Python:/home/venom/Downloads# strings file | grep -i pico
picoCTF{grep_and_you_will_find_cdf2e7c2}
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
picoCTF{grep_and_you_will_find_cdf2e7c2}
</pre>
