<h1>SysAdmin Part 2</h1>

<p>User: morpheus<br>
Password: VNZDDLq2x9qXCzVdABbR1HOtz<br>
Host: morpheus@ringzer0ctf.com -p 10148</p>

<h3>Deskription</h3>

```console
morpheus@sysadmin-track:/$ grep -iR 'architect'
morpheus@sysadmin-track:/etc$ cat fstab 
LABEL=rootfs  /         ext4  defaults  0 0
LABEL=UEFI    /boot/efi vfat  defaults  0 0
#//TheMAtrix/phone  /media/Matrix  cifs  username=architect,password=$(base64 -d "RkxBRy0yMzJmOTliNDE3OGJkYzdmZWY3ZWIxZjBmNzg4MzFmOQ=="),iocharset=utf8,sec=ntlm  0  0
morpheus@sysadmin-track:/etc$ echo "RkxBRy0yMzJmOTliNDE3OGJkYzdmZWY3ZWIxZjBmNzg4MzFmOQ==" | base64 -d
FLAG-232f99b4178bdc7fef7eb1f0f78831f9
morpheus@sysadmin-track:/etc$
```
<p>Password architect terdapat pada /etc/fstab</p>
<h3>Flag</h3>
<pre>FLAG-232f99b4178bdc7fef7eb1f0f78831f9</pre>
