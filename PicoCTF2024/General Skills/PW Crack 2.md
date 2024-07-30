<h1>PW Crack 2</h1>
<h3>Description</h3>
<p>Can you crack the password to get the flag?
Download the password <a href='https://artifacts.picoctf.net/c/13/level2.py'>checker</a> here and you'll need the encrypted <a href='https://artifacts.picoctf.net/c/13/level2.flag.txt.enc'>flag</a> in the same directory too.</p>
<h3>Solution</h3>
<p>Ganti dan Tambah beberapa baris code</p>

```python3
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level2.flag.txt.enc', 'rb').read()



def level_2_pw_check(password):
    user_pw = password
    if( user_pw == chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")

password = chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36)
print("Password is :",password)

level_2_pw_check(password)
```
<h3>Flag</h3>
<pre>
picoCTF{tr45h_51ng1ng_489dea9a}
</pre>
