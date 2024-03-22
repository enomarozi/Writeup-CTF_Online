<h1>Super SSH</h1>
<h3>Description</h3>
Using a Secure Shell (SSH) is going to be pretty important.
Can you ssh as ctf-player to titan.picoctf.net at port 49226 to get the flag?
You'll also need the password 6abf4a82. If asked, accept the fingerprint with yes.
<h3>Solution</h3>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# ssh ctf-player@titan.picoctf.net -p 49226
The authenticity of host '[titan.picoctf.net]:49226 ([3.139.174.234]:49226)' can't be established.
ED25519 key fingerprint is SHA256:4S9EbTSSRZm32I+cdM5TyzthpQryv5kudRP9PIKT7XQ.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[titan.picoctf.net]:49226' (ED25519) to the list of known hosts.
ctf-player@titan.picoctf.net's password: 
Welcome ctf-player, here's your flag: picoCTF{s3cur3_c0nn3ct10n_65a7a106}
Connection to titan.picoctf.net closed.
root@xisco-VirtualBox:/home/xisco/Downloads#
```
<h3>Flag</h3>
<pre>
  picoCTF{s3cur3_c0nn3ct10n_65a7a106}
</pre>
