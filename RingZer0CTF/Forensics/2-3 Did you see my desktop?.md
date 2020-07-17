<h1><b>2-3 Did you see my desktop?</h1></b>
<pre>
<a href="https://ringzer0ctf.com/files/b64021d477b2505fcb37e6b46701bb5a.zip">File</a>
</pre>
</b><h3>Solution</h3></b>
<p>Identifikasi file dengan tool volatility</p>

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
<p>Didapatkan kalo itu merupakan dumpfile Windows 7 SP0 x86, lanjut sesuai challenge kita diminta melihat desktop pada dumpfile dan eksekusi tool volatility dengan argument windows</p>

```console
root@Python:/home/venom/Downloads# ../Tools/volatility/vol.py --profile Win7SP0x86 windows -f 5bd2510a83e82d271b7bf7fa4e0970d1 | egrep -iw 'F|L|A|G-'
Volatility Foundation Volatility Framework 2.6.1
Window Handle: #1012e at 0xfe80dc28, Name: F$L%A^G-5bd2510a83e82d271b7bf7fa4e0970d1 - Notepad
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
FLAG-5bd2510a83e82d271b7bf7fa4e0970d1
</pre>
