<h1>droids2</h1>
<h3>Description</h3>
<pre>
Find the pass, get the flag. Check out this <a href='https://challenge-files.picoctf.net/c_fickle_tempest/a16f42ed8f9e92de13d5140a90ba1b9b3e719500265e0b96f8553a59a5e07881/two.apk'>file</a>.
</pre>
<h3>Solution</h3>
<label>Decompile dengan apktool</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# apktool d two.apk         
I: Using Apktool 2.7.0-dirty on two.apk
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
<label>Check file FlagstaffHill.smali dan reverse di directory smali/com/hellocmu/picoctf</label>

```python3
list_ = ["weatherwax","ogg","garlick","nitt","aching","dismass"]
v1 = 0x3
v2 = v1 - v1
v3 = v1 // v1
v4 = v3 + v3 - v2
v5 = v1 + v4
v6 = v5 + v2 - v3
list_v = [v1,v2,v3,v4,v5,v6]
print(f"{list_[v5]}.{list_[v3]}.{list_[v2]}.{list_[v6]}.{list_[v1]}.{list_[v4]}") #dismass.ogg.weatherwax.aching.nitt.garlick
```
<label>Eksekusi string dismass.ogg.weatherwax.aching.nitt.garlick ke file apk yg dijalankan di device android studio</label>
<h3>Flag</h3>
<pre>
picoCTF{what.is.your.favourite.colour}
</pre>
