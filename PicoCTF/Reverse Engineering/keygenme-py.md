<h1>keygenme-py</h1>
<p><a href='https://mercury.picoctf.net/static/9055e7d35f5f4646338a1734aea0dda5/keygenme-trial.py'>keygenme-trial.py</a></p>
<h3>Solution</h3>
<p>Periksa semua flow program dan fungsinya, disana terdapat pengecekan keygen dari variabel 'key_full_template_trial' atau difungsi 'check_key'</p>
<p>Dari fungsi terdapat pengecekan juga yaitu key terdapat dari masing-masing index sha256 variabel username='FRASER', yaitu index [4,5,3,6,2,7,1,8].
  dan berikut characternya sekaligus serial-key(flag)</p>
  
  ```python3
  import hashlib

key = [4,5,3,6,2,7,1,8]
name = b'FRASER'
hash_name = hashlib.sha256(name).hexdigest()
print('picoCTF{1n_7h3_|<3y_of_',end='')
for i in key:
    print(hash_name[i],end='')
print('}')

  ```
  <h3>Flag</h3>
  <p>picoCTF{1n_7h3_|<3y_of_ac73dc29}</p>
