<h1>vault-door-4</h1>
<h3>Description</h3>
<pre>
This vault uses ASCII encoding for the password. The source code for this vault is here: <a href='https://jupiter.challenges.picoctf.org/static/834acd392e0964a41f05790655a994b9/VaultDoor4.java'>VaultDoor4.java</a>
</pre>
<h3>Solution</h3>
<p>Program solved.py</p>

```python3
def desimal():
    part = '106,85,53,116,95,52,95,98'.split(',')
    result = ''.join([chr(int(i)) for i in part])
    return result

def hexadesimal():
    part = '0x55,0x6e,0x43,0x68,0x5f,0x30,0x66,0x5f'.split(',')
    result = ''.join([chr(int(i[2:],16)) for i in part])
    return result

def octadesimal():
    part = '0142,0131,0164,063,0163,0137,0146,064'.split(',')
    result = ''.join([chr(int(i[1:],8)) for i in part])
    return result

def string():
    part = ['a' , '8' , 'c' , 'd' , '8' , 'f' , '7' , 'e']
    result = ''.join(part)
    return result

def flag():
    print("picoCTF{"+desimal()+hexadesimal()+octadesimal()+string()+"}")
    
if __name__ == "__main__":
    flag()
```
<p>Eksekusi terminal</p>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# python3 solved.py 
picoCTF{jU5t_4_bUnCh_0f_bYt3s_f4a8cd8f7e}

┌──(root㉿Kali)-[/home/venom/Downloads]
└─# javac VaultDoor4.java              
                                                                                                                                                               
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# python3 solved.py | java VaultDoor4 
Enter vault password: Access granted.
```
<h3>Flag</h3>
<pre>
picoCTF{jU5t_4_bUnCh_0f_bYt3s_f4a8cd8f7e}
</pre>
