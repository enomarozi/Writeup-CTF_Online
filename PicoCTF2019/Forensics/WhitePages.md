<h1><b>WhitePages</h1></b>
<pre>
I stopped using YellowPages and moved onto WhitePages... but the <a href='https://2019shell1.picoctf.com/static/e134178261c6fa36e9058d5408118dd9/whitepages.txt'>page</a> they gave me is all blank!
</pre>
</b><h3>Solution</h3></b>
<p>eksekusi xxd pada file</p>

```console
root@Python:/home/venom/Downloads# xxd whitepages.txt | head -n 10
00000000: e280 83e2 8083 e280 83e2 8083 20e2 8083  ............ ...
00000010: 20e2 8083 e280 83e2 8083 e280 83e2 8083   ...............
00000020: 20e2 8083 e280 8320 e280 83e2 8083 e280   ...... ........
00000030: 83e2 8083 20e2 8083 e280 8320 e280 8320  .... ...... ... 
00000040: 2020 e280 83e2 8083 e280 83e2 8083 e280    ..............
00000050: 8320 20e2 8083 20e2 8083 e280 8320 e280  .  ... ...... ..
00000060: 8320 20e2 8083 e280 83e2 8083 2020 e280  .  .........  ..
00000070: 8320 20e2 8083 2020 2020 e280 8320 e280  .  ...    ... ..
00000080: 83e2 8083 e280 83e2 8083 2020 e280 8320  ..........  ... 
00000090: e280 8320 e280 8320 e280 83e2 8083 e280  ... ... ........
root@Python:/home/venom/Downloads# 
```
<p>Disana terdapat beberapa macam nilai hexa ea 80 80 20, dan raw bytes hanya terdapat titik dan space, karena melampaui ascii 127</p>
<p>Convert hexa = 20 --> 1</p>
<p>Convert hexa > 20 --> 0</p>

```python
file = open("whitepages.txt").read()
flag = ""
for i in file:
    if ord(i) == 32:
        flag += "1"
    elif ord(i) > 32:
        flag += "0"
result = ''.join([chr(int(flag[:i][-8:],2)) for i in range(8,len(flag)+8,8)])
print(result)
```
<p>Hasil Program</a>
<pre>

		picoCTF

		SEE PUBLIC RECORDS & BACKGROUND REPORT
		5000 Forbes Ave, Pittsburgh, PA 15213
		picoCTF{not_all_spaces_are_created_equal_dd5c2e2f77f89f3051c82bfee7d996ef}

</pre>
</b><h3>Flag</h3></b>
<pre>
picoCTF{not_all_spaces_are_created_equal_dd5c2e2f77f89f3051c82bfee7d996ef}
</pre>
