<h1><b>Git Is Good</h1></b>
<pre>
The flag used to be there. But then I redacted it. Good Luck. 
https://mega.nz/#!3CwDFZpJ!Jjr55hfJQJ5-jspnyrnVtqBkMHGJrd6Nn_QqM7iXEuc
</pre>
</b><h3>Solution</h3></b>
<p>Terdapat file flag.txt yang contentnya sudah dihapus. reverse content pada commit d10f77c4e766705ab36c7f31dc47b0c5056666bb dan buka file flag.txt lagi</p>

```console
root@Python:/home/venom/Downloads# cd gitIsGood/
root@Python:/home/venom/Downloads/gitIsGood# ls
flag.txt
root@Python:/home/venom/Downloads/gitIsGood# cat flag.txt 
flag{REDACTED}
root@Python:/home/venom/Downloads/gitIsGood# git rev-list all
fatal: ambiguous argument 'all': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'
root@Python:/home/venom/Downloads/gitIsGood# git rev-list --all
d10f77c4e766705ab36c7f31dc47b0c5056666bb
195dd65b9f5130d5f8a435c5995159d4d760741b
6e824db5ef3b0fa2eb2350f63a9f0fdd9cc7b0bf
root@Python:/home/venom/Downloads/gitIsGood# git log
commit d10f77c4e766705ab36c7f31dc47b0c5056666bb (HEAD -> master)
Author: LaScalaLuke <lascala.luke@gmail.com>
Date:   Sun Oct 30 14:33:18 2016 -0400

    Edited files

commit 195dd65b9f5130d5f8a435c5995159d4d760741b
Author: LaScalaLuke <lascala.luke@gmail.com>
Date:   Sun Oct 30 14:32:44 2016 -0400

    Edited files

commit 6e824db5ef3b0fa2eb2350f63a9f0fdd9cc7b0bf
Author: LaScalaLuke <lascala.luke@gmail.com>
Date:   Sun Oct 30 14:32:11 2016 -0400

    edited files
root@Python:/home/venom/Downloads/gitIsGood# git revert d10f77c4e766705ab36c7f31dc47b0c5056666bb
[master 41c4156] Revert "Edited files"
 Committer: root <root@venom.com>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+), 1 deletion(-)
root@Python:/home/venom/Downloads/gitIsGood# cat flag.txt 
flag{protect_your_git}
root@Python:/home/venom/Downloads/gitIsGood# 
```
</b><h3>Flag</h3></b>
<pre>
flag{protect_your_git}
</pre>
