<h1><b>Rev-Land</b></h3>
<pre>
gr33n5h4d0w made an APK and hide private message in it.
Somehow dr3dd get APK file and easily find his private message. 
Can you find it too?

Note: The format of flag for this challenge is n00bCTF{flag}

<a href="http://static.beast.sdslabs.co/static/rev-land/rev-land.apk">APK</a>
</pre>
<h3><b>Solution</b></h3>
<p>Decompiler file apk, lalu periksa fungsi MainActivity apk</p>

```console
root@Python:/home/venom/Downloads# apktool d rev-land.apk 
I: Using Apktool 2.4.1-dirty on rev-land.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: /root/.local/share/apktool/framework/1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Baksmaling classes2.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
root@Python:/home/venom/Downloads# cd rev-land/smali/in/bckdr/hack/android/revland/
root@Python:/home/venom/Downloads/rev-land/smali/in/bckdr/hack/android/revland# strings MainActivity.smali | tail -n 10
    const-string v0, "MainActivity"
    const-string v1, "There are 4 parts of the flag. All of equal length !!!"
    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I
    .line 14
    const-string v0, "MainActivity"
    const-string v1, "flag format: n00bCTF{secret_flag_here}"
    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I
    .line 16
    return-void 
```
<p>Disana terdapat clue, yaitu flag terdiri dari 4 part masing-masing sama panjang dan format n00bCTF{secret_flag_here}</p>
<p><b>Flag Part-1</b> Baik disini kita mulai mencari flag part-1. part-1 terdapat pada file MainActivity, yaitu terdapat operasi decrypt yang mana kuncinya tidak diketahui. Kita akan coba bruteforce dengan operasi xor</p>

```python
def part_1_xor(n):
    part1_flag = [0x44, 0x1a, 0x1a, 0x48, 0x69, 0x7e, 0x6c,
                  0x51, 0x58, 0x4f,0x5c, 0x4f, 0x58, 0x59]
    flag = ""
    for i in part1_flag:
        flag += chr(i^n)
    if "n00b" in flag:
        print(flag)
for j in range(100):
    part_1_xor(j)
```
<p>Sesuai format, flag part-1 didapatkan yaitu <b>n00bCTF{revers</b></p>
<p><b>Flag Part-2</b> Lanjut ke flag part-2, disini kita akan mencari dengan perintah grep</p>

```console
root@Python:/home/venom/Downloads# grep -iR flagparttwo
Binary file rev-land.apk matches
rev-land/smali/in/bckdr/hack/android/revland/R$string.smali:.field public static final flagPartTwo:I = 0x7f0b0021
rev-land/res/values/strings.xml:    <string name="flagPartTwo">ing_is_fun_aft</string>
rev-land/res/values/public.xml:    <public type="string" name="flagPartTwo" id="0x7f0b0021" />
root@Python:/home/venom/Downloads# 
```
<p>Sesuai format panjang flag, flag part-2 sudah didapatkan pada file rev-land/res/values/strings.xml yaitu <b>ing_is_fun_aft</b></p>
<p><b>Flag Part-3</b> Untuk part-3 kita gunakan lagi perintah grep</p>

```console
root@Python:/home/venom/Downloads# grep -iR flagpartthree
Binary file rev-land.apk matches
rev-land/smali/in/bckdr/hack/android/revland/R$id.smali:.field public static final flagPartThree:I = 0x7f070035
rev-land/res/values/ids.xml:    <item type="id" name="flagPartThree" />
rev-land/res/values/public.xml:    <public type="id" name="flagPartThree" id="0x7f070035" />
rev-land/res/layout/activity_another_class.xml:    <TextView android:textSize="30.0sp" android:id="@id/flagPartThree" android:padding="1.0sp" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="er_all_s0mer4n" android:singleLine="false" android:textAllCaps="false" android:fontFamily="monospace" android:textAlignment="center" app:layout_constraintBottom_toBottomOf="parent" app:layout_constraintLeft_toLeftOf="parent" app:layout_constraintRight_toRightOf="parent" app:layout_constraintTop_toTopOf="parent" />
root@Python:/home/venom/Downloads# 
```
<p>Kita mendapatkannya lagi, sesuai format panjang flag pada direktori rev-land/res/layout/activity_another_class.xml yaitu <b>er_all_s0mer4n</b></p>
<p><b>Flag Part-4</b> Untuk terakhir kita gunakan lagi perintah grep</p>

```console
root@Python:/home/venom/Downloads# grep -iR flagpartfour
rev-land/smali/in/bckdr/hack/android/revland/AnotherClass.smali:    const-string v3, "flagPartFour is: d0m_"
root@Python:/home/venom/Downloads# 
```
<p>Kita mendapatkannya yaitu <b>d0m_</b> tetapi formatnya tidak sesuai, mari kita periksa pada file direktori rev-land/smali/in/bckdr/hack/android/revland/AnotherClass.smali
<p>Jika kita perhatikan pada file disana terdapat class <b>guestSecret()</b> dan <b>checkSecret()</b>. pada <b>guestSecret()</b> terdapat operasi semacam bruteforce range integer 0x1 hingga 0x3b9ac9ff.
dan pada class <b>checkSecret()</b> terdapat operasi penambahan list untuk string "d0m_", string(integer) dan "}" lalu dilakukan pengecekan MD5hash yaitu 1c661ac2b84593142f719f5a3e09f16d, 
jika kita lihat sesuai clue, yaitu panjang flag semuanya sama, berarti flag part-4 <b>d0m_xxxxxxxxx}</b>, dan xxxxxxxxx itu merupakan nilai integer, baik kita akan coba bruteforce sesuai program sekaligus pengecekan MD5hash</p>

```python
for i in range(100000000,999999999):
    part4 = "d0m_"+str(i)+"}"
    text = hashlib.md5(part4.encode('utf8')).hexdigest()
    if text == "1c661ac2b84593142f719f5a3e09f16d":
        print(part4)
```
<p>Dan flag part-4 didapatkan yaitu <b>d0m_100328327}</b>, Satukan seluruh flag <b>n00bCTF{reversing_is_fun_after_all_s0mer4nd0m_100328327}</b></p>
<h3><b>Flag</b></h3>
<pre>
n00bCTF{reversing_is_fun_after_all_s0mer4nd0m_100328327}
</pre>
