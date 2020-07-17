<h1><b>1/3 Do not waste the environment</h1></b>
<pre>
<a href="https://ringzer0ctf.com/files/b64021d477b2505fcb37e6b46701bb5a.zip">File</a>
</pre>
</b><h3>Solution</h3></b>
<p>Identifikasi file dengan tool volatility, maka didapatkan file merupakan proses dump file dari Windows 7 SP0 x86</p>

```console
root@Python:/home/venom/Downloads# ../Tools/volatility/vol.py imageinfo -f 5bd2510a83e82d271b7bf7fa4e0970d1
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x86_23418, Win7SP0x86, Win7SP1x86_24000, Win7SP1x86
                     AS Layer1 : IA32PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/venom/Downloads/5bd2510a83e82d271b7bf7fa4e0970d1)
                      PAE type : No PAE
                           DTB : 0x185000L
                          KDBG : 0x82920be8L
          Number of Processors : 1
     Image Type (Service Pack) : 0
                KPCR for CPU 0 : 0x82921c00L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2014-03-09 20:57:55 UTC+0000
     Image local date and time : 2014-03-09 13:57:55 -0700
root@Python:/home/venom/Downloads# 
```
<p>Sesuai challenge, kita diminta untuk memeriksa proses envoirment pada file dump, jadi kita analisa lagi dengan tool volatility parameter envoirment</p>

```console
root@Python:/home/venom/Downloads# ../Tools/volatility/vol.py --profile Win7SP0x86 envars -f 5bd2510a83e82d271b7bf7fa4e0970d1 | grep -i 'f l a g'
Volatility Foundation Volatility Framework 2.6.1
    1972 taskhost.exe         0x000d07f0 F l a g -                      66d7724d872da91af56907aea0f6bfb8
     216 dwm.exe              0x003e07f0 F l a g -                      66d7724d872da91af56907aea0f6bfb8
     284 explorer.exe         0x001aa330 F l a g -                      66d7724d872da91af56907aea0f6bfb8
    1336 VBoxTray.exe         0x004f07f0 F l a g -                      66d7724d872da91af56907aea0f6bfb8
    2528 notepad.exe          0x001807f0 F l a g -                      66d7724d872da91af56907aea0f6bfb8
    3488 DumpIt.exe           0x003a07f0 F l a g -                      66d7724d872da91af56907aea0f6bfb8
root@Python:/home/venom/Downloads# 
```
<p>Dan flag didapatkan pada proses task-manager, desktop windows manage(dwm), explorer dan DumpIt</p>
</b><h3>Flag</h3></b>
<pre>
Flag-66d7724d872da91af56907aea0f6bfb8
</pre>
