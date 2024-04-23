<h1>SysAdmin Part 1</h1>
<p>Find Trinity password

User: morpheus<br>
Password: VNZDDLq2x9qXCzVdABbR1HOtz<br>
Host: morpheus@ringzer0ctf.com -p 10089<br>
</p>
<h3>Description</h3>

```console
morpheus@sysadmin-track:~$ ps -f -u root | grep -i 'trinity'
root         411       1  0 Apr11 ?        00:00:23 /bin/sh /root/backup.sh -u trinity -p Flag-7e0cfcf090a2fe53c97ea3edd3883d0d
morpheus@sysadmin-track:~$ 
```

<p>Check process active pada linux pada UID root</p>
<h3>Flag</h3>
<pre>Flag-7e0cfcf090a2fe53c97ea3edd3883d0d</pre>
