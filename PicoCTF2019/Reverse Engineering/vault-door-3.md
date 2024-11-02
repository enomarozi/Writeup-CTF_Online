<h1>vault-door-3</h1>
<h3>Description</h3>
<pre>
This vault uses for-loops and byte arrays. The source code for this vault is here: <a href='https://jupiter.challenges.picoctf.org/static/a4018cec1446761cb2e8cce05db925fa/VaultDoor3.java'>VaultDoor3.java</a>
</pre>
<h3>Solution</h3>
<p>Cek source code program</p>

```python3
password = 'jU5t_a_sna_3lpm12g94c_u_4_m7ra41'
result = ['']*len(password)

for i in range(8):
    result[i] = password[i]
for i in range(8,16):
    result[i] = password[23-i]
for i in range(16,32,2):
    result[i] = password[46-i]
for i in range(31,15,-2):
    result[i] = password[i]
print('picoCTF{'+''.join(result)+"}")
```

```console
┌──(root㉿Python)-[/home/venom/Downloads]
└─# python3 solved.py              
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21}
                                                                                
┌──(root㉿Python)-[/home/venom/Downloads]
└─# python3 solved.py | java VaultDoor3 
Enter vault password: Access granted.
```
