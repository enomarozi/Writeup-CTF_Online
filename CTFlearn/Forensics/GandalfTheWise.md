<h1><b>GandalfTheWise
</h1></b>
<pre>
Extract the flag from the Gandalf.jpg file. 
You may need to write a quick script to solve this.

<a href="https://ctflearn.com/challenge/download/936">Gandalf.jpg</a> 
</pre>
</b><h3>Solution</h3></b>
<p>Eksekusi exiftool dan grep pada file</p>

```console
root@Python:/home/venom/Downloads# exiftool Gandalf.jpg -a | grep -i comment
Comment                         : Q1RGbGVhcm57eG9yX2lzX3lvdXJfZnJpZW5kfQo=.
Comment                         : xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p.
Comment                         : h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU.
root@Python:/home/venom/Downloads# echo "Q1RGbGVhcm57eG9yX2lzX3lvdXJfZnJpZW5kfQo=" | base64 -d
CTFlearn{xor_is_your_friend}
root@Python:/home/venom/Downloads# echo "xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p" | base64 -d
�>�|픬NR��:Z+�/�?�2O\�8�O�
root@Python:/home/venom/Downloads# echo "h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU" | base64 -d
�j���� )��T>`~M�mf�]�p.;�Q�<�
root@Python:/home/venom/Downloads# 
```
<p>Sesuai flag pertama itu merupakan clue, yaitu kita akan melakukan operasi XOR dari 2 encryptext yang didapatkan</p>

```python
import base64

encryptext_1 = base64.b64decode("xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p")
encryptext_2 = base64.b64decode("h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU")
for i,j in zip(encryptext_1,encryptext_2):
    print(chr(i^j),end='')
```

</b><h3>Flag</h3></b>
<pre>
CTFlearn{Gandalf.BilboBaggins}
</pre>
