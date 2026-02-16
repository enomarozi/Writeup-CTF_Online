<h1>droids3</h1>
<h3>Description</h3>
<pre>
Find the pass, get the flag. Check out this <a href='https://challenge-files.picoctf.net/c_fickle_tempest/1d3186493afd7eebcdf8f75ef28be676c7b13eda44e235f67de7ece2d180158f/three.apk'>file.</a>
</pre>
<h3>Solution</h3>
<label>decompile dengan apktool dan cek file FlagstaffHill.smali</label>

```java
.method public static getFlag(Ljava/lang/String;Landroid/content/Context;)Ljava/lang/String;
    .locals 1
    .param p0, "input"    # Ljava/lang/String;
    .param p1, "ctx"    # Landroid/content/Context;

    .line 19
    invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->nope(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v0

    .line 20
    .local v0, "flag":Ljava/lang/String;
    return-object v0
.end method

.method public static nope(Ljava/lang/String;)Ljava/lang/String;
    .locals 1
    .param p0, "input"    # Ljava/lang/String;

    .line 11
    const-string v0, "don\'t wanna"

    return-object v0
.end method

.method public static yep(Ljava/lang/String;)Ljava/lang/String;
    .locals 1
    .param p0, "input"    # Ljava/lang/String;

    .line 15
    invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->cilantro(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    return-object v0
.end method
```
<label>Fungsi getFlag() tidak akan pernah mendapatkan flag karna memanggil fungsi nope(), dan fungsi yep() memanggil fungsi cilantro() yang mungkin fungsi untuk memperoleh flag, ganti fungsi nope() ke fungsi cilantro() pada fungsi getFlag().<label>
<br>
<label>Jalankan command</label>
```console
apktool d three.apk --no-res
```
<label>lalu edit fungsi</label>
<pre>
invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->nope(Ljava/lang/String;)Ljava/lang/String;
</pre>
<label>Jadi</label>
<pre>
invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->cilantro(Ljava/lang/String;)Ljava/lang/String;
</pre>
<label>dan rebuild apk</label>
```console
apktool b three -o recompiled_three.apk
```
<label>lalu sign apk</label>
```console
 wget https://github.com/patrickfav/uber-apk-signer/releases/download/v1.1.0/uber-apk-signer-1.1.0.jar
 java -jar uber-apk-signer-1.1.0.jar --apks recompiled_three.apk
```
<label>Dan install di device manager android, eksekusi sembarang input<label>
<h3>Flag</h3>
<pre>
picoCTF{tis.but.a.scratch}
</pre>
