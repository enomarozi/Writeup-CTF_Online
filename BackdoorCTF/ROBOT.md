<h1><b>ROBOT</b></h1>
<pre>
Sopan got hold of a flag. Fearing google's robot, he hid the flag somewhere on <a href="http://static.beast.sdslabs.co/static/ROBOT/index.html">this</a> link. 
Now, Sopan is nowhere to be found. Recover the flag before someone else does!
</pre>

<h3><b>Solution</b></h3>
<p>file robots.txt ini biasanya basic web di CTF, untuk penjelasaan baca <a href="https://en.wikipedia.org/wiki/Robots_exclusion_standard">disini</a></p>

```console
root@Python:/home/venom/Downloads# curl http://static.beast.sdslabs.co/static/ROBOT/index.html 
Sorry you're at the wrong place. You'll get nothing here. Go back.
root@Python:/home/venom/Downloads# curl http://static.beast.sdslabs.co/static/ROBOT/robots.txt
User-agent: *
Disallow: /euhfy20hwyeuhs.html
root@Python:/home/venom/Downloads# curl http://static.beast.sdslabs.co/static/ROBOT/euhfy20hwyeuhs.html
dc2e771d12d019fd30f9c133c2e7d2fd02fa67d03962ff6c2a6c20f7340a5267
root@Python:/home/venom/Downloads# 
```
<h3><b>Flag</b></h3>
<pre>
dc2e771d12d019fd30f9c133c2e7d2fd02fa67d03962ff6c2a6c20f7340a5267
</pre>
