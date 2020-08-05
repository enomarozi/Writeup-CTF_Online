<h1><b>unzip</h1></b>
<pre>
Can you unzip this file and get the flag?
</pre>
</b><h3>Solution</h3></b>
<p>Alur sederhana</p>

```console
root@Python:/home/venom/Downloads# unzip flag.zip 
Archive:  flag.zip
  inflating: flag.png                
root@Python:/home/venom/Downloads# eog 
root@Python:/home/venom/Downloads# eog flag.png 
```
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/PicoCTF2019/Forensics/Images/flag.jpg'>
  </p>
</b><h3>Flag</h3></b>
<pre>
picoCTF{unz1pp1ng-1s3a5y}
</pre>
