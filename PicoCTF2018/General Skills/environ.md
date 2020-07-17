<h1><b>environ</h1></b>
<pre>
Sometimes you have to configure environment variables before executing a program. 
Can you find the flag we've hidden in an environment variable on the shell server?
</pre>
</b><h3>Solution</h3></b>
<p>Login ke shell <a href=""https://2018game.picoctf.com/shell>server</a>, dan eksekusi command env (env merupakan sebuah aplikasi yang berjalan pada shell linux, contohnya jika kita ketik perintah pwd, maka akan tampil direktori sekarang)</p>
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/PicoCTF2018/Forensics/Images/environ.jpg">
</p>
</b><h3>Flag</h3></b>
<pre>
picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}
</pre>
