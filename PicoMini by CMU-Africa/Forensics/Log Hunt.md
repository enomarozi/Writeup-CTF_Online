<h1>Log Hunt</h1>
<h3>Description</h3>
<label>Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag? Download the <a href='https://challenge-files.picoctf.net/c_amiable_citadel/49cec6157142f24a599f4164d5b63322c2494f801390d6f22eb91b3aa592bc66/server.log'>logs</a> and figure out the full flag from the fragments.</label>
<h3>Solution</h3>
<label>command pipeline grep, head, awk dan tr</label>

```console
grep -iR "part" server.log | head -n 5 | awk -F ': ' '{print $2}' | tr -d '\n'
```
<h3>Flag</h3>
<pre>
picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}
</pre>
