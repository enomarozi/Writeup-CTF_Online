<h1><b>3-3 Suspicious account password?</h1></b>
<pre>
<a href="3 / 3 Suspicious account password?">File</a>
</pre>
</b><h3>Solution</h3></b>
<p>Hasil identifikasi file merupakan filedump Windows 7 SP0 x86</p>

```console
root@Python:/home/venom/Downloads# ./../Tools/volatility/vol.py imageinfo -f 5bd2510a83e82d271b7bf7fa4e0970d1 
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
<p>Sesuai challenge, kita diminta mencari password pada filedump, eksekusi tool volatility dengan argument hashdump</p>

```console
root@Python:/home/venom/Downloads# ./../Tools/volatility/vol.py --profile Win7SP0x86 hashdump -f 5bd2510a83e82d271b7bf7fa4e0970d1 
Volatility Foundation Volatility Framework 2.6.1
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
flag:1000:aad3b435b51404eeaad3b435b51404ee:3008c87294511142799dca1191e69a0f:::
root@Python:/home/venom/Downloads# 
```
<p>Didapatkan 3 user dari hasil hashdump, yang kita butuhkan hanyalah user flag, decrypt NTLM flag yaitu 3008c87294511142799dca1191e69a0f</p>
<p>Disini saya mendecrypt dengan serangan bruteforce tool hashcat</p>

```console
root@Python:/home/venom/Downloads# hashcat -m 1000 -O -a3 -i 3008c87294511142799dca1191e69a0f

3008c87294511142799dca1191e69a0f:admin123        
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Name........: NTLM
Hash.Target......: 3008c87294511142799dca1191e69a0f
Time.Started.....: Fri Jul 17 00:13:51 2020 (43 secs)
Time.Estimated...: Fri Jul 17 00:14:34 2020 (0 secs)
Guess.Mask.......: ?1?2?2?2?2?2?2?3 [8]
Guess.Charset....: -1 ?l?d?u, -2 ?l?d, -3 ?l?d*!$@_, -4 Undefined 
Guess.Queue......: 8/15 (53.33%)
Speed.#1.........: 19260.8 MH/s (13.00ms) @ Accel:64 Loops:256 Thr:1024 Vec:1
Recovered........: 1/1 (100.00%) Digests
Progress.........: 818868649984/5533380698112 (14.80%)
Rejected.........: 0/818868649984 (0.00%)
Restore.Point....: 366215168/2479113216 (14.77%)
Restore.Sub.#1...: Salt:0 Amplifier:768-1024 Iteration:0-256
Candidates.#1....: vcbf9123 -> 6g2x5w23
Hardware.Mon.#1..: Temp: 62c Fan: 66% Util: 99% Core:1815MHz Mem:4001MHz Bus:16

Started: Fri Jul 17 00:13:42 2020
Stopped: Fri Jul 17 00:14:34 2020
root@Python:/home/venom/Downloads# 
```
<p>Dan passwordnya didapatkan, yaitu admin123</p>
</b><h3>Flag</h3></b>
<pre>
admin123
</pre>
