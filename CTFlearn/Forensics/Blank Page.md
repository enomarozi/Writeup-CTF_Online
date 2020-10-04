<h1><b>Blank Page</h1></b>
<pre>
I've just graduated the Super Agent School. This is my first day as a spy. The Master-Mind sent me the secret message, but I don't remember how to read this. Help!

<a href='https://ctflearn.com/challenge/download/959'>TheMessage.txt</a>
</pre>
</b><h3>Solution</h3></b>
<p>Read file dengan looping python, dan perhatikan setiap output looping yang dihasilkan, yaitu 32 dan 8207. Karena hanya terdapat 2 angka saja, saya bisa menduga bahwa ini terkait dengan binary</p>
<p>Decode 32 menjadi 0, dan 8207 jadi 1. Seperti script dibawah</p>

```python3
file = open("TheMessage.txt","r").read()
hasil = ""
for i in file:
    if ord(i) == 32:
        hasil += "0"
    else:
        hasil += "1"
    
result = ''.join([chr(int(hasil[:i][-8:],2)) for i in range(8,len(hasil)+8,8)])
print(result)
```
<p>Output program</p>
<pre>
From The Global Anti-Terrorists Tactics

If you read this you passed. Congrats.
Your first task will come tomorrow.
Good luck.

CTFlearn{If_y0u_r3/\d_thi5_you_pa553d}
</pre>
</b><h3>Flag</h3></b>
<pre>
CTFlearn{If_y0u_r3/\d_thi5_you_pa553d}
</pre>
