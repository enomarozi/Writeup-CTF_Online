<h1>ReadMyCert</h1>
<h3>Description</h3>
<p>How about we take you on an adventure on exploring certificate signing requests
Take a look at this CSR file <a href='https://artifacts.picoctf.net/c/423/readmycert.csr'>here</a>.</p>
<h3>Solution</h3>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# openssl req -in readmycert.csr -noout -text | grep -i pico
        Subject: CN = picoCTF{read_mycert_57f58832}, name = ctfPlayer
```

<h3>Flag</h3>
<pre>picoCTF{read_mycert_57f58832}</pre>
