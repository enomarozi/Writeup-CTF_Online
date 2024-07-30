<h1>PW Crack 3</h1>
<h3>Description</h3>
<p>Can you crack the password to get the flag?
Download the password checker <a href='https://artifacts.picoctf.net/c/17/level3.py'>here</a> and you'll need the encrypted <a href='https://artifacts.picoctf.net/c/17/level3.flag.txt.enc'>flag</a> and the <a href='https://artifacts.picoctf.net/c/17/level3.hash.bin'>hash</a> in the same directory too.
There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.</p>
<h3>Solution</h3>
<p>Ganti beberapa baris code di python password checker</p>

```python3
import hashlib

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

flag_enc = open('level3.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level3.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]

def level_3_pw_check():
    for i in pos_pw_list:
        user_pw = i
        user_pw_hash = hash_pw(user_pw)
        
        if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), user_pw)
            print(decryption,"And Password is "+i)
            return
        print("That password is incorrect")



level_3_pw_check()
```
<h3>Flag</h3>
<pre>
picoCTF{m45h_fl1ng1ng_cd6ed2eb}
</pre>
