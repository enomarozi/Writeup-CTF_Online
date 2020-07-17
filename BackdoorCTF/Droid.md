<h1><b>Droid</b></h1>
<pre>
n00b found this apk in the wild. Find the flag.
http://static.beast.sdslabs.co/static/DROID/n00bCTF.apk
</pre>
<h3><b>Solution</b></h3>
<p>Decompile apk dengan apktool, dan periksa fungsi MainActivity apk</p> 

```console
root@Python:/home/venom/Downloads# apktool d n00bCTF.apk 
I: Using Apktool 2.4.1-dirty on n00bCTF.apk
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
root@Python:/home/venom/Downloads# cd n00bCTF/smali/com/sdsinfosec/n00bctf/
root@Python:/home/venom/Downloads/n00bCTF/smali/com/sdsinfosec/n00bctf# ls
 BuildConfig.smali       MainActivity.smali  'R$attr.smali'  'R$color.smali'  'R$drawable.smali'  'R$integer.smali'  'R$mipmap.smali'  'R$styleable.smali'   R.smali
'MainActivity$1.smali'  'R$anim.smali'       'R$bool.smali'  'R$dimen.smali'  'R$id.smali'        'R$layout.smali'   'R$string.smali'  'R$style.smali'
root@Python:/home/venom/Downloads/n00bCTF/smali/com/sdsinfosec/n00bctf# strings -a MainActivity.smali | head -n 25
.class public Lcom/sdsinfosec/n00bctf/MainActivity;
.super Landroid/support/v7/app/AppCompatActivity;
.source "MainActivity.java"
# instance fields
.field ENCRYPTED_FLAG:Ljava/lang/String;
.field ENCRYPTED_KEY:Ljava/lang/String;
.field flagText:Landroid/widget/TextView;
.field keyInput:Landroid/widget/EditText;
.field submitBtn:Landroid/widget/Button;
# direct methods
.method public constructor <init>()V
    .locals 1
    .prologue
    .line 13
    invoke-direct {p0}, Landroid/support/v7/app/AppCompatActivity;-><init>()V
    .line 19
    const-string v0, "i~lQcubkpunoiegzcfcdmuyacffpppW"
    iput-object v0, p0, Lcom/sdsinfosec/n00bctf/MainActivity;->ENCRYPTED_FLAG:Ljava/lang/String;
    .line 20
    const-string v0, "a1d0c6e83f027327d8461063f4ac58a6"
    iput-object v0, p0, Lcom/sdsinfosec/n00bctf/MainActivity;->ENCRYPTED_KEY:Ljava/lang/String;
    return-void
.end method
# virtual methods
.method decrypt(I)Ljava/lang/String;
```
<p>Seperti dari decompile fungsi main apk, disana terdapa proses encrypt pada variabel ENCRYPTED_FLAG dan ENCRYPTED_KEY</p>
<pre>
ENCRYPTED_FLAG = i~lQcubkpunoiegzcfcdmuyacffpppW
ENCRYPTED_KEY = a1d0c6e83f027327d8461063f4ac58a6
</pre>
<p> variabel ENCRYPTED_KEY itu merupakan integer 42 dari decrypt MD5hash, dan akan kita coba decrypt dengan metode xor</p>

```python
encode = "i~lQcubkpunoiegzcfcdmuyacffpppW"
for i in encode:
    print(chr(ord(i)^42),end="")
```
<h3><b>Flag</b></h3>
<pre>
CTF{I_HAZ_DECOMPILING_SKILLZZZ}
</pre>
