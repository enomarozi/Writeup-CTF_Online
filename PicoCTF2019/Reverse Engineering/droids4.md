<h1>droids4</h1>
<h3>Description</h3>
<pre>
Reverse the pass, patch the file, get the flag. Check out this <a href='https://challenge-files.picoctf.net/c_fickle_tempest/d2dc0e603476e05c950d1ab52e214d574dabaa18875fbc211ae5e653fb9dea5b/four.apk'>file</a>.
</pre>
<h3>Solution</h3>
<label>Decompile dengan jadx dan check source code FlagstaffHill</label>

```java
package com.hellocmu.picoctf;

import android.content.Context;

/* loaded from: classes.dex */
public class FlagstaffHill {
    public static native String cardamom(String str);

    public static String getFlag(String input, Context ctx) {
        StringBuilder ace = new StringBuilder("aaa");
        StringBuilder jack = new StringBuilder("aaa");
        StringBuilder queen = new StringBuilder("aaa");
        StringBuilder king = new StringBuilder("aaa");
        ace.setCharAt(0, (char) (ace.charAt(0) + 4));
        ace.setCharAt(1, (char) (ace.charAt(1) + 19));
        ace.setCharAt(2, (char) (ace.charAt(2) + 18));
        jack.setCharAt(0, (char) (jack.charAt(0) + 7));
        jack.setCharAt(1, (char) (jack.charAt(1) + 0));
        jack.setCharAt(2, (char) (jack.charAt(2) + 1));
        queen.setCharAt(0, (char) (queen.charAt(0) + 0));
        queen.setCharAt(1, (char) (queen.charAt(1) + 11));
        queen.setCharAt(2, (char) (queen.charAt(2) + 15));
        king.setCharAt(0, (char) (king.charAt(0) + 14));
        king.setCharAt(1, (char) (king.charAt(1) + 20));
        king.setCharAt(2, (char) (king.charAt(2) + 15));
        String password = "".concat(queen.toString()).concat(jack.toString()).concat(ace.toString()).concat(king.toString());
        return input.equals(password) ? "call it" : "NOPE";
    }
}
```
<label>Persamaan dengan python</label>
```python3
ace = "aaa"
jack = "aaa"
queen = "aaa"
king = "aaa"
ace_ = ""
jack_ = ""
queen_ = ""
king_ = ""
ace_ += chr(ord(ace[0])+4)
ace_ += chr(ord(ace[1])+19)
ace_ += chr(ord(ace[2])+18)
jack_ += chr(ord(jack[0])+7)
jack_ += chr(ord(jack[1])+0)
jack_ += chr(ord(jack[2])+1)
queen_ += chr(ord(queen[0])+0)
queen_ += chr(ord(queen[1])+11)
queen_ += chr(ord(queen[2])+15)
king_ += chr(ord(queen[0])+14)
king_ += chr(ord(queen[1])+20)
king_ += chr(ord(queen[2])+15)
print(queen_+jack_+ace_+king_) #alphabetsoup
```
<label>Setelah dieksekusi tidak mendapatkan flag, karna fungsi flag tidak di panggil pada fungsi cardamom<label><br>
<label>Decompile dengan apktool untuk menghasilkan file smali, dan edit return FlagstaffHill.smalli ke fungsi cardamom</label><br>

```smali
const-string v5, "call it"

return-object v5
```
<label>Jadi</label>

```smali
invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->cardamom(Ljava/lang/String;)Ljava/lang/String;

move-result-object v0

return-object v0
```
<label>Lanjut build apk baru dan sign apk, dan lanjut install di device manager, teakhir input password alphabetsoup</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# apktool b four -o recompiled_four.apk 
I: Using Apktool 2.9.3
I: Checking whether sources has changed...
I: Smaling smali folder into classes.dex...
I: Checking whether resources has changed...
I: Copying raw resources...
I: Copying libs... (/lib)
I: Building apk file...
I: Copying unknown files/dir...
I: Built apk into: recompiled_four.apk                                                                                                                                                             
                                                                                                                                                                        
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# java -jar uber-apk-signer-1.1.0.jar --apks recompiled_four.apk 

source:
	/home/venom/Downloads
zipalign location: BUILT_IN 
	/tmp/uapksigner-13471814061288407204/linux-zipalign-29_0_210723901357729540863.tmp
keystore:
	[0] 161a0018 /tmp/temp_15021120647748477323_debug.keystore (DEBUG_EMBEDDED)

01. recompiled_four.apk

	SIGN
	file: /home/venom/Downloads/recompiled_four.apk (1.49 MiB)
	checksum: 8f6c4f7f98a11ad34551e601f17aa54890286a670341ccdb8f84838f40a903a2 (sha256)
	- zipalign success
	- sign success

	VERIFY
	file: /home/venom/Downloads/recompiled_four-aligned-debugSigned.apk (1.52 MiB)
	checksum: 13a93fee6e92b110e7cf544e5b993dce58cf32aeaa12ecbc40b2cb5e643e01df (sha256)
	- zipalign verified
	- signature verified [v1, v2, v3] 
		Subject: CN=Android Debug, OU=Android, O=US, L=US, ST=US, C=US
		SHA256: 1e08a903aef9c3a721510b64ec764d01d3d094eb954161b62544ea8f187b5953 / SHA256withRSA
		Expires: Fri Mar 11 03:10:05 WIB 2044

[Mon Feb 16 19:43:04 WIB 2026][v1.1.0]
Successfully processed 1 APKs and 0 errors in 1.03 seconds.
```
<h3>Flag</h3>
<pre>
picoCTF{not.particularly.silly}
</pre>
