<h1><b>pipe</h1></b>
<pre>
During your adventure, you will likely encounter a situation where you need to process data that you receive over the network rather than through a file. 
Can you find a way to save the output from this program and search for the flag? Connect with 2018shell.picoctf.com 2015.
</pre>
</b><h3>Solution</h3></b>
<p>Connect nc 2018shell.picoctf.com 2015 lalu pipe grep pada terminal</p>

```console
root@Python:/home/venom/Downloads# nc 2018shell.picoctf.com 2015 | grep -i pico
picoCTF{almost_like_mario_8861411c}
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
picoCTF{almost_like_mario_8861411c}
</pre>

