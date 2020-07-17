<h1><b>strings</h1></b>
<pre>
Can you find the flag in this <a href="https://2018shell.picoctf.com/static/a3d311b507256d5d9299c0e94dfc4fc5/strings">file</a> without actually running it? 
You can also find the file in /problems/strings_4_40d221755b4a0b134c2a7a2e825ef95f on the shell server.
</pre>
</b><h3>Solution</h3></b>
<p>check dengan perintah strings dan grep pada terminal</p>

```console
root@Python:/home/venom/Downloads# strings strings | grep -i pico
picoCTF{sTrIngS_sAVeS_Time_d3ffa29c}
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
picoCTF{sTrIngS_sAVeS_Time_d3ffa29c}
</pre>
