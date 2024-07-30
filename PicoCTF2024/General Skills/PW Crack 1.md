<h1>PW Crack 1</h1>
<h3>Can you crack the password to get the flag?
Download the password checker <a href='https://artifacts.picoctf.net/c/11/level1.py'>here and you'll need the encrypted <a href='https://artifacts.picoctf.net/c/11/level1.flag.txt.enc'>flag</a> in the same directory too.</h3>
<h3>Solution</h3>
<p>input password sesuai if, atau tambah manual pada code</p>

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


flag_enc = open('level1.flag.txt.enc', 'rb').read()



def level_1_pw_check():
    user_pw = "1e1a"
    if( user_pw == "1e1a"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_1_pw_check()

```

<h3>Flag</h3>
<pre>
picoCTF{545h_r1ng1ng_fa343060}
</pre>
