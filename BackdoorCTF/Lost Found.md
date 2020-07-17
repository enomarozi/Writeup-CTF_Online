<h1><b>Lost Found</h1></b>
<pre>
Go and enter the flag in <a href="http://static.beast.sdslabs.co/static/LOST-FOUND/lost_found.zip">this zip file</a>.
</pre>
<h3><b>Solution</b></h3>
<p>Ekstrak file zip maka didapatkan git direktori, masuk ke direktori lost-found, disana terdapat file commit. Dan perhatikan juga git log disana juga terdapat beberapa commit.
jadi disini kita bisa melihat perubahan commit master dengan commit pada lost-found.</p>

```console
root@Python:/home/venom/Downloads/.git/lost-found/commit# git log
commit 3b161f0d331a45e48b8866fc4fb85ade0d4fa0f6 (HEAD -> master, origin/master, origin/HEAD)
Author: Abhay Rana <capt.n3m0@gmail.com>
Date:   Tue Feb 10 22:05:37 2015 +0530

    Updates API token instructions

commit 386acf32c272e85af17634a01ae7d63583aa4e5f
Author: Abhay Rana <capt.n3m0@gmail.com>
Date:   Mon Nov 17 18:55:18 2014 +0530

    Fixes heroku deploy button

commit 1bfd33c318cfcee0fb9b5e570093773d5379559b
Author: Abhay Rana <capt.n3m0@gmail.com>
Date:   Mon Nov 3 20:46:55 2014 +0530

    Forces long-polling, so it works over Cloudflare's free SSL.

commit cf0d77f3c6dea534399841b0a56319f4c6d64e43
Author: Abhay Rana <capt.n3m0@gmail.com>
Date:   Wed Oct 1 19:08:13 2014 +0530

    Improves scrollng for the initial message set.
root@Python:/home/venom/Downloads/.git/lost-found/commit# ls
f7cee847b02a589cd3d0fa4e2c32cf9a0ccd94a6
root@Python:/home/venom/Downloads/.git/lost-found/commit# git diff 3b161f0d331a45e48b8866fc4fb85ade0d4fa0f6 f7cee847b02a589cd3d0fa4e2c32cf9a0ccd94a6
diff --git a/flag.txt b/flag.txt
new file mode 100644
index 0000000..5318b5a
--- /dev/null
+++ b/flag.txt
@@ -0,0 +1 @@
+FLAG IS 676a0b9e546e1920c0ff6631f4aac3a9646d843c6bd6d333dda542987570c1b6
root@Python:/home/venom/Downloads/.git/lost-found/commit# 

```

<h3><b>Flag</b></h3>
<pre>
676a0b9e546e1920c0ff6631f4aac3a9646d843c6bd6d333dda542987570c1b6
</pre>
