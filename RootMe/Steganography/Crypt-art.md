<h1>Crypt-art</h1>
<h3>Description</h3>
<label>A police unit intercepted a message from a terrorist group. This message may contain a secret key used to encrypt other communications. They need you to decrypt it !</label>
<h3>Solution</h3>
<label>File ppm seperti npiet, eksekusi strings command</label>
  
```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# ls
ch8.ppm
                                                                                                                        
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# strings -a ch8.ppm 
70 50
  Hi! Welcome to  
esoteric programming!
The encrypted pass is:  
EPCQFBXKWURQCTXOIPMNV
 Bienvenue a la program
mation esoterique!
Le pass encrypte est
EPCQFBXKWURQCTXOIPMNV
```
<label>Seperti crypto classic vigenere,dan key-nya execute file ppm ke https://www.bertnase.de/npiet/npiet-execute.php yang merupakan esolang programming</label>

<pre>
Message Enc = EPCQFBXKWURQCTXOIPMNV
Key = EYJFRGTT
</pre>
<label>Decrypt pesan + key di https://rumkin.com/tools/cipher/vigenere/</label> 
<h3>Flag</h3>
<pre>
ARTLOVERSWILLNEVERDIE
</pre>
