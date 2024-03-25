<h1>Time Machine</h1>
<h3>Description</h3>
<p>What was I last working on? I remember writing a note to help me remember...
You can download the challenge files here:</p>
<a href='https://artifacts.picoctf.net/c_titan/163/challenge.zip'>File</a>
<h3>Solution</h3>

<p>git log</p>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# ls
challenge.zip
root@xisco-VirtualBox:/home/xisco/Downloads# unzip challenge.zip 
Archive:  challenge.zip
   creating: drop-in/
  inflating: drop-in/message.txt     
   creating: drop-in/.git/
   creating: drop-in/.git/branches/
  inflating: drop-in/.git/description  
   creating: drop-in/.git/hooks/
  inflating: drop-in/.git/hooks/applypatch-msg.sample  
  inflating: drop-in/.git/hooks/commit-msg.sample  
  inflating: drop-in/.git/hooks/fsmonitor-watchman.sample  
  inflating: drop-in/.git/hooks/post-update.sample  
  inflating: drop-in/.git/hooks/pre-applypatch.sample  
  inflating: drop-in/.git/hooks/pre-commit.sample  
  inflating: drop-in/.git/hooks/pre-merge-commit.sample  
  inflating: drop-in/.git/hooks/pre-push.sample  
  inflating: drop-in/.git/hooks/pre-rebase.sample  
  inflating: drop-in/.git/hooks/pre-receive.sample  
  inflating: drop-in/.git/hooks/prepare-commit-msg.sample  
  inflating: drop-in/.git/hooks/update.sample  
   creating: drop-in/.git/info/
  inflating: drop-in/.git/info/exclude  
   creating: drop-in/.git/refs/
   creating: drop-in/.git/refs/heads/
 extracting: drop-in/.git/refs/heads/master  
   creating: drop-in/.git/refs/tags/
 extracting: drop-in/.git/HEAD       
  inflating: drop-in/.git/config     
   creating: drop-in/.git/objects/
   creating: drop-in/.git/objects/pack/
   creating: drop-in/.git/objects/info/
   creating: drop-in/.git/objects/43/
 extracting: drop-in/.git/objects/43/246218ab4fc7b30e9a9dff073e012316851469  
   creating: drop-in/.git/objects/25/
 extracting: drop-in/.git/objects/25/16effb8d70e33bdd0023629b164a77225e1ec2  
   creating: drop-in/.git/objects/e6/
 extracting: drop-in/.git/objects/e6/5fedb3a72a16c577f4b17023b63997134b307d  
  inflating: drop-in/.git/index      
 extracting: drop-in/.git/COMMIT_EDITMSG  
   creating: drop-in/.git/logs/
  inflating: drop-in/.git/logs/HEAD  
   creating: drop-in/.git/logs/refs/
   creating: drop-in/.git/logs/refs/heads/
  inflating: drop-in/.git/logs/refs/heads/master  
root@xisco-VirtualBox:/home/xisco/Downloads# cd drop-in/
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# ls
message.txt
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# git log
commit e65fedb3a72a16c577f4b17023b63997134b307d (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:29 2024 +0000

    picoCTF{t1m3m@ch1n3_88c35e3b}
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# git checkout e65fedb3a72a16c577f4b17023b63997134b307d
```

<h3>Flag</h3>
<pre>picoCTF{t1m3m@ch1n3_88c35e3b}</pre>
