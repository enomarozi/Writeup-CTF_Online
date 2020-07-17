<h1><b>hex editor</h1></b>
<pre>
This cat has a secret to teach you. 
You can also find the <a href="https://2018shell.picoctf.com/static/8bf13e0b1ce613af3b79223abb8f8d6d/hex_editor.jpg">file</a> in /problems/hex-editor_2_c1a99aee8d919f6e42697662d798f0ff on the shell server.
</pre>
</b><h3>Solution</h3></b>
<p>Eksekusi perintah strings dan grep pada terminal</p>


```console
root@Python:/home/venom/Downloads# strings -a hex_editor.jpg | grep -i picoCTF{
Your flag is: "picoCTF{and_thats_how_u_edit_hex_kittos_22C1d865}"
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
picoCTF{and_thats_how_u_edit_hex_kittos_22C1d865}
</pre>
