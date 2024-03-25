<h1>Blame Game</h1>
<h3>Description</h3>

<p>Someone's commits seems to be preventing the program from working. Who is it?
You can download the challenge files here:</p>
<a href='https://artifacts.picoctf.net/c_titan/159/challenge.zip'>File</a>
<h3>Solution</h3>
<p>git log</p>

```console
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# git log | head -n 20
commit 23e9d4ce78b3cea725992a0ce6f5eea0bf0bcdd4
Author: picoCTF{@sk_th3_1nt3rn_81e716ff} <ops@picoctf.com>
Date:   Tue Mar 12 00:07:15 2024 +0000

    optimize file size of prod code

commit 3ce5c692e2f9682a866c59ac1aeae38d35d19771
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:15 2024 +0000

    create top secret project
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# 
```
<h3>Flag</h3>
<pre>picoCTF{@sk_th3_1nt3rn_81e716ff}</pre>
