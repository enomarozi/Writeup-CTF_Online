<h1><b>BIN-EASY</b></h1>
<pre>
n00b hid a flag somewhere in <a href="">this</a> binary. Can you find it?
</pre>
<h3><b>Solution</b></h3>
<p>Eksekusi printah strings pada file</p>

```console
root@Python:/home/venom/Downloads# strings -a bin-easy | grep -x '.\{63,64\}'
f16dd0f8d26ba93fcc427f9c95594d03f7068d6d5c32ea4915300a4a86708001
root@Python:/home/venom/Downloads# 
```
<h3><b>Flag</b></h3>
<pre>
f16dd0f8d26ba93fcc427f9c95594d03f7068d6d5c32ea4915300a4a86708001
</pre>
