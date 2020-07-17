<h1><b>Who I am?</h1></b>
<pre>I'm looking for information about me! The website...
</pre>
</b><h3>Solution</h3></b>
<p>Check domain record txt</p>

```console
root@Python:/home/venom/Downloads# dig ringzer0ctf.com txt | grep -i flag
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 2, ADDITIONAL: 1
; EDNS: version: 0, flags:; udp: 4096
ringzer0ctf.com.	3600	IN	TXT	"FLAG-305l9RR202HG695t6Y8ZU77xyq"
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
FLAG-305l9RR202HG695t6Y8ZU77xyq
</pre>
