<h1>Glory of the Garden</h1>
<h3>Description</h3>
<p>This <a href='https://jupiter.challenges.picoctf.org/static/d0e1ffb10fc0017c6a82c57900f3ffe3/garden.jpg'>garden</a> contains more than it seems.</p>
<h3>Solution</h3>
<p>Flag di data file image</p>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# strings -a garden.jpg | grep "flag" | awk -F'"' '{print $2}'
picoCTF{more_than_m33ts_the_3y3eBdBd2cc}
```

<h3>Flag</h3>
<pre>
picoCTF{more_than_m33ts_the_3y3eBdBd2cc}
</pre>
