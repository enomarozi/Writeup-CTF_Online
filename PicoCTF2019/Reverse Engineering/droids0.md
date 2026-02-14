<h1>droids0</h1>
<h3>Description</h3>
<pre>
Where do droid logs go. Check out this <a href='https://challenge-files.picoctf.net/c_fickle_tempest/8a5028cf509544247e42398da9ffaa69a93225064a331dbf5a31066d44157f3f/zero.apk'>file.</a>
</pre>
<h3>Solution</h3>
<label>Install apk device manager android studio dan Check file FlagstaffHill.smali lalu reverse code, di folder smali/com/hellocmu/picoctf</label>

```android
.line 11
invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->paprika(Ljava/lang/String;)Ljava/lang/String;

move-result-object v0

const-string v1, "PICO"

invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

.line 12
const-string v0, "Not Today..."

return-object v0
```
<label>Input PICO di apk, dan check di adb log</label>

```console
┌──(root㉿Kali)-[/home/…/smali/com/hellocmu/picoctf]
└─# adb logcat | grep PICO
02-14 23:08:06.729  6237  6237 I PICO    : picoCTF{a.moose.once.bit.my.sister}
```
<h3>Flag</h3>
<pre>
picoCTF{a.moose.once.bit.my.sister}
</pre>
