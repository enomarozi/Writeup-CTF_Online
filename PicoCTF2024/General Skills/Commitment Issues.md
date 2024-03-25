<h1>Commitment Issues</h1>
<h3>Description</h3>

<p>I accidentally wrote the flag down. Good thing I deleted it!
You download the challenge files here:</p>
<a href='https://artifacts.picoctf.net/c_titan/139/challenge.zip'>File</a>
<h3>Solution</h3>
<p>Git checkout</p>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# cd drop-in/
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# ls
message.txt
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# git log
commit 144fdc44b09058d7ea7f224121dfa5babadddbb9 (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:06:25 2024 +0000

    remove sensitive info

commit 7d3aa557ff7ba7d116badaf5307761efb3622249
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:06:25 2024 +0000

    create flag
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# git checkout 7d3aa557ff7ba7d116badaf5307761efb3622249
Note: switching to '7d3aa557ff7ba7d116badaf5307761efb3622249'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 7d3aa55 create flag
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# cat message.txt 
picoCTF{s@n1t1z3_be3dd3da}
```
<h3>Flag</h3>
<pre>picoCTF{s@n1t1z3_be3dd3da}</pre>
