<h1><b>Rubber Duck</h1></b>
<pre>
Find the flag! Simple forensics challenge to get started with.

<a href='https://ctflearn.com/challenge/download/933'>RubberDuck.jpg</a> 
</pre>
</b><h3>Solution</h3></b>
<p>Eksekusi exiftool dan grep pada file JPG</p>

```console
root@Python:/home/venom/Downloads# exiftool RubberDuck.jpg -a | grep -i comment
Comment                         : CTFlearn{ILoveJakarta}.
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
CTFlearn{ILoveJakarta}
</pre>
