<h1>SysAdmin Part 5</h1>
<p>Decrypt the oracle encrypted file<br>

User: oracle<br>
Host: ssh -i ssh.key oracle@ringzer0ctf.com -p 10149</p>

<h3>Deskription</h3>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# ssh -i ssh.key oracle@ringzer0ctf.com -p 10149
oracle@sysadmin-track:~$ openssl enc -aes-256-cbc -a -d -pbkdf2 -in encflag.txt.enc -k 'lp6PWgOwDctq5Yx7ntTmBpOISc'
FLAG-54e7f8d0ea560fa7ed98e832900fc45b
oracle@sysadmin-track:~$
```
<p>Login dengan private key, dan check file .basrc pada directory HOME oracle, disana terdapat alias untuk decrypt file flag</p>

<h3>Flag</h3>
<pre>FLAG-54e7f8d0ea560fa7ed98e832900fc45b</pre>
