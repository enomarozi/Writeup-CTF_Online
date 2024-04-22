<h1>
  HideToSee
</h1>
<h3>Description</h3>
<p>
  How about some hide and seek heh?
  Look at this image <a href='https://artifacts.picoctf.net/c/236/atbash.jpg'>here</a>.
</p>
<h3>
  Solution
</h3>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# steghide extract -sf atbash.jpg 
Enter passphrase: 
wrote extracted data to "encrypted.txt".
root@xisco-VirtualBox:/home/xisco/Downloads# cat encrypted.txt 
krxlXGU{zgyzhs_xizxp_zx751vx6}
root@xisco-VirtualBox:/home/xisco/Downloads#
```
<p>Decrypt atbash <a href='https://rumkin.com/tools/cipher/atbash/'>disini</a> --> picoCTF{atbash_crack_ac751ec6}</p>

<h3>
  Flag
</h3>
<pre>picoCTF{atbash_crack_ac751ec6}</pre>
