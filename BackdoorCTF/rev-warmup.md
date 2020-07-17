<h1><b>rev-warmup</h1></b>
<pre>
n00b is a beginner in reversing, but even he was able to do it. Can you?

<a href="http://static.beast.sdslabs.co/static/rev-warmup/rev-warmup">rev-warmup</a>
</pre>
<h3><b>Solution</b></h3>
<p>Jika kita decompile program maka disana terdapat string compare yaitu membandingkan fungsi input() dengan string("love_u_3000"), eksekusi langsung program pada terminal</p>

```console
root@Python:/home/venom/Downloads# echo "love_u_3000" | ./rev-warmup 
Enter password to view the flag
flag{Did_y0U_jU57_r3V3r53}
root@Python:/home/venom/Downloads# 
```
<h3><b>Flag</b></h3>
<pre>
flag{Did_y0U_jU57_r3V3r53}
</pre>
