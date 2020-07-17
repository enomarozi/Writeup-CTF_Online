<h1><b>HEEEEEEERE'S Johnny!</h1></b>
<pre>
Okay, so we found some important looking files on a linux computer. 
Maybe they can be used to get a password to the process. 
Connect with <b>nc 2018shell.picoctf.com 40157</b>. 
Files can be found here: <a href="https://2018shell.picoctf.com/static/7a017af70c0b86ab002896616376499e/passwd">passwd</a><a href="https://2018shell.picoctf.com/static/7a017af70c0b86ab002896616376499e/passwd"> shadow</a>.
</pre>
</b><h3>Solution</h3></b>
<p>Crack password pada shadown dengan john</p>

```console
root@Python:/home/venom/Downloads# unshadow passwd shadow > will_crack.txt
root@Python:/home/venom/Downloads# cat will_crack.txt 
root:$6$IGI9prWh$ZHToiAnzeD1Swp.zQzJ/Gv.iViy39EmjVsg3nsZlfejvrAjhmp5jY.1N6aRbjFJVQX8hHmTh7Oly3NzogaH8c1:0:0:root:/root:/bin/bash
root@Python:/home/venom/Downloads# john will_crack.txt --show
0 password hashes cracked, 1 left
root@Python:/home/venom/Downloads# john will_crack.txt
Warning: detected hash type "sha512crypt", but the string is also recognized as "HMAC-SHA256"
Use the "--format=HMAC-SHA256" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 128/128 AVX 2x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 8 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 2 candidates buffered for the current salt, minimum 16 needed for performance.
Warning: Only 6 candidates buffered for the current salt, minimum 16 needed for performance.
Warning: Only 7 candidates buffered for the current salt, minimum 16 needed for performance.
Warning: Only 11 candidates buffered for the current salt, minimum 16 needed for performance.
Warning: Only 7 candidates buffered for the current salt, minimum 16 needed for performance.
Warning: Only 5 candidates buffered for the current salt, minimum 16 needed for performance.
Almost done: Processing the remaining buffered candidate passwords, if any.
Warning: Only 2 candidates buffered for the current salt, minimum 16 needed for performance.
Proceeding with wordlist:/usr/share/john/password.lst, rules:Wordlist
password1        (root)
1g 0:00:00:00 DONE 2/3 (2020-07-16 16:39) 1.333g/s 1784p/s 1784c/s 1784C/s 123456..crawford
Use the "--show" option to display all of the cracked passwords reliably
Session completed
root@Python:/home/venom/Downloads# john will_crack.txt --show
root:password1:0:0:root:/root:/bin/bash

1 password hash cracked, 0 left
root@Python:/home/venom/Downloads# 
```
<p>password didapatkan yaitu <b>password1</b>, dan username <b>root</b></p>

```console
root@Python:/home/venom/Downloads# nc 2018shell.picoctf.com 40157
Username: root  
Password: password1
picoCTF{J0hn_1$_R1pp3d_1b25af80}
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
picoCTF{J0hn_1$_R1pp3d_1b25af80}
</pre>
