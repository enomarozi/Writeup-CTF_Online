<h1>Active Directory - GPO</h1>
<h3>Description</h3>
<label>During a security audit, the network traffic during the boot sequence of a workstation enrolled in an Active Directory was recorded. Analyze this capture and find the administrator’s password.
</label><a href='https://static.root-me.org/forensic/ch12/ch12.pcap'>File</a>
<h3>Solution</h3>
<label>Cari password administrator AD di capture wireshark, cek protokol SMB2</label>

```xml
<?xml version="1.0" encoding="utf-8"?>
<Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}">
  <User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" name="Helpdesk" image="2" changed="2015-05-06 05:50:08" uid="{43F9FF29-C120-48B6-8333-9402C927BE09}">
    <Properties action="U" newName="" fullName="" description="" cpassword="PsmtscOuXqUMW6KQzJR8RWxCuVNmBvRaDElCKH+FU+w" changeLogon="1" noChange="0" neverExpires="0" acctDisabled="0" userName="Helpdesk"/>
  </User>
  <User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" name="Administrateur" image="2" changed="2015-05-05 14:19:53" uid="{5E34317F-8726-4F7C-BF8B-91B2E52FB3F7}" userContext="0" removePolicy="0">
    <Properties action="U" newName="" fullName="Admin Local" description="" cpassword="LjFWQMzS3GWDeav7+0Q0oSoOM43VwD30YZDVaItj8e0" changeLogon="0" noChange="0" neverExpires="1" acctDisabled="0" subAuthority="" userName="Administrateur"/>
  </User>
</Groups>
```
<label>Hash Helpdesk dan Administrator</label>
<pre>
Helpdesk = PsmtscOuXqUMW6KQzJR8RWxCuVNmBvRaDElCKH+FU+w
Administrator = LjFWQMzS3GWDeav7+0Q0oSoOM43VwD30YZDVaItj8e0
</pre>

```python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def aes_decrypt(ciphertext_b64, key, iv):
    ciphertext = base64.b64decode(ciphertext_b64)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    return plaintext.decode('utf-8')

key = bytes.fromhex("4e9906e8fcb66cc9faf49310620ffee8f496e806cc057990209b09a433b66c1b")
iv  = b"\x00"*16
ciphertext_b64 = "LjFWQMzS3GWDeav7+0Q0oSoOM43VwD30YZDVaItj8e0="
hasil = aes_decrypt(ciphertext_b64, key, iv)
print("Hasil dekripsi:", hasil)

```
<label>Hasil</label>
<pre>
Helpdesk : R00tm333
Administrator : TuM@sTrouv3
</pre>
<h3>Flag</h3>
<pre>
TuM@sTrouv3
</pre>
