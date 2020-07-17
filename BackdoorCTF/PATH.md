<h1><b>PATH</b></h1>
<pre>
The flag is somewhere on the domain flag.bckdr.in
</pre>
<h3><b>Solution</h3></b>
<p>Check TXT record domain pada https://dnschecker.org/ atau dengan tool dig pada terminal</p>

```console
root@Python:/home/venom/Downloads# dig -t txt flag.bckdr.in

; <<>> DiG 9.16.4-Debian <<>> -t txt flag.bckdr.in
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 13879
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;flag.bckdr.in.			IN	TXT

;; ANSWER SECTION:
flag.bckdr.in.		300	IN	TXT	"e4de7470b35f7b3627283a61a808d32b99f91d5a1092a892bdb5bcdb4af3b7ab"

;; Query time: 80 msec
;; SERVER: 192.168.100.1#53(192.168.100.1)
;; WHEN: Thu Jul 09 03:49:34 WIB 2020
;; MSG SIZE  rcvd: 119

root@Python:/home/venom/Downloads# 
```
<h3><b>Flag</h3></b>
<pre>
e4de7470b35f7b3627283a61a808d32b99f91d5a1092a892bdb5bcdb4af3b7ab
</pre>
