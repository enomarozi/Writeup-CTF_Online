<h1>vault-door-1</h1>
<h3>Description</h3>
<pre>
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: <a href='https://jupiter.challenges.picoctf.org/static/29b91e638ccbd76aaa8c0462d1c64d8d/VaultDoor1.java'>VaultDoor1.java</a>
</pre>
<p>Cek Source code, berikut reverse dengan python</p>

```python3
index_ = [0,29,4,2,23,3,17,1,7,10,5,9,11,15,8,12,20,14,6,24,
          18,13,19,21,16,27,30,25,22,28,26,31]
char_ = 'd,3,r,5,r,c,4,3,b,_,4,3,t,c,l,H,c,_,m,5,r,3,4,T,H,f,b,_,3,6,f,0'.split(',')
result = "picoCTF{"
if len(index_) == len(char_):
    for i in range(len(index_)):
        result += char_[index_.index(i)]
print(result+'}')
```

```console
┌──(root㉿Python)-[/home/venom/Downloads]
└─# python3 solved.py                  
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0}
                                                                                
┌──(root㉿Python)-[/home/venom/Downloads]
└─# python3 solved.py | java VaultDoor1
Enter vault password: Access granted.
```
<h3>Flag</h3>
<pre>
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0}
</pre>
