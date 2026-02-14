<h1>droids1</h1>
<h3>Description</h3>
<pre>
Find the pass, get the flag. Check out this <a href='https://challenge-files.picoctf.net/c_fickle_tempest/0c0fee0ca27866e0888594bd0a00165097c35f4f9d0654d69c7a3f3b0283e615/one.apk'>file.</a>
</pre>
<h3>Solution</h3>
<label>Decompile dengan apktool</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# apktool d one.apk     
I: Using Apktool 2.7.0-dirty on one.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: /root/.local/share/apktool/framework/1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
```
<label>Check file string.xml di folder /res/values/res/values password = opossum</label>

```console
<string name="hint">brute force not required</string>
<string name="manatee">caribou</string>
<string name="myotis">jackrabbit</string>
<string name="password">opossum</string>
<string name="porcupine">blackbuck</string>
<string name="porpoise">mouflon</string>
<string name="search_menu_title">Search</string>
```
<label>Input password di emulator android studio</label>
<h3>Flag</h3>
<pre>
picoCTF{pining.for.the.jfords}
</pre>
