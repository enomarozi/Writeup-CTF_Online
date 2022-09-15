<h1>Easy1</h1>
<p>The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a <a href='https://jupiter.challenges.picoctf.org/static/1fd21547c154c678d2dab145c29f1d79/table.txt'>table</a> to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this table to solve it?.</p>
<p>Hint :</p>
<ul>
  <li>Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.</li>
  <li>Please use all caps for the message.</li>
</ul>
<h3>Solution</h3>
<p>Merupakan Vigenere Cipher</p>

```python3
import string

letter = string.ascii_lowercase

def decrypt():
    text = "UFJKXQZQUNB".lower()
    key = "SOLVECRYPTO".lower()
    if len(key) < len(text):
        key = (key*len(text))[:len(text)]
    result_text = [j for i in text for j in range(len(letter)) if i == letter[j]]
    result_key = [j for i in key for j in range(len(letter)) if i == letter[j]]
    process = [letter[(result_text[j]-result_key[i])%26] for i in range(len(result_key)) for j in range(len(result_text)) if i == j]
    encrypt = "".join(process)
    print('picoCTF{'+encrypt.upper()+'}')
decrypt()

```
<h3>Flag</h3>
<p>picoCTF{CRYPTOISFUN}</p>
