<h1>vault-door-7</h1>
<h3>Description</h3>
<pre>
This vault uses bit shifts to convert a password string into an array of integers. Hurry, agent, we are running out of time to stop Dr. Evil's nefarious plans! The source code for this vault is here: <a href='https://jupiter.challenges.picoctf.org/static/89b8065d19ee9830ae548d27a40ca757/VaultDoor7.java'>VaultDoor7.java</a>
</pre>
<p>Cek komentar pada source code</p>

```python3
bigInt = [1096770097,1952395366,1600270708,1601398833,1716808014,1734291511,960049251,1681089078]
result = 'picoCTF{'
for i in bigInt:
    com = bin(i)[2:].rjust(32,'0')
    result_split = [com[:split][-8:] for split in range(8,len(com)+8,8)]
    for j in result_split:
        result += chr(int(j,2))

print(result+'}')
```

```console
┌──(root㉿Python)-[/home/venom/Downloads]
└─# python3 solved.py                  
picoCTF{A_b1t_0f_b1t_sh1fTiNg_07990cd3b6}
                                                                                                                                          
┌──(root㉿Python)-[/home/venom/Downloads]
└─# javac VaultDoor7.java              
                                                                                                                                          
┌──(root㉿Python)-[/home/venom/Downloads]
└─# python3 solved.py | java VaultDoor7 
Enter vault password: Access granted.
```
<h3>Flag</h3>
<pre>
picoCTF{A_b1t_0f_b1t_sh1fTiNg_07990cd3b6}
</pre>
