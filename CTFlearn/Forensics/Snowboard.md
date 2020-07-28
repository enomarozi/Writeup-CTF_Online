<h1><b>Snowboard</h1></b>
<pre>
Find the flag in the jpeg file. Good Luck!

<a href='https://ctflearn.com/challenge/download/934'>Snowboard.jpg</a> 
</pre>
</b><h3>Solution</h3></b>
<p>Eksekusi Exiftool dan grep pada file lalu decode base64</p>

```console
root@Python:/home/venom/Downloads# exiftool Snowboard.jpg -a | grep -i comment
Comment                         : CTFlearn{CTFIsEasy!!!}.
Comment                         : Q1RGbGVhcm57U2tpQmFuZmZ9Cg==.
root@Python:/home/venom/Downloads# echo "Q1RGbGVhcm57U2tpQmFuZmZ9Cg==" | base64 -d
CTFlearn{SkiBanff}
root@Python:/home/venom/Downloads# 
```

</b><h3>Flag</h3></b>
<pre>
CTFlearn{SkiBanff}
</pre>
