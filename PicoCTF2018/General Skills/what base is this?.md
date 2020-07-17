<h1><b>what base is this?</h1></b>
<pre>
To be successful on your mission, you must be able read data represented in different ways, such as hexadecimal or binary. 
Can you get the flag from this program to prove you are ready? 
Connect with nc 2018shell.picoctf.com 15853.
</pre>
</b><h3>Solution</h3></b>
<p>Connect netcat, dan input semua pertanyaan pada script dan jawab</p>

```python
###Binary
binary = input("Input Binary : ")
result = ''.join([chr(int(i,2)) for i in binary.split(" ")])
print(result)
###Hexa
hexa = input("Input Hexa : ")
print(bytearray.fromhex(hexa))
###Octal
octal = input("Input Octal : ")
result = ''.join([chr(int(i,8)) for i in octal.split(" ")])
print(result)
```

```console
root@Python:/home/venom/Downloads# nc 2018shell.picoctf.com 15853
We are going to start at the very beginning and make sure you understand how data is stored.
plug
Please give me the 01110000 01101100 01110101 01100111 as a word.
To make things interesting, you have 30 seconds.
Input:
plug
Please give me the 7461626c65 as a word.
Input:
table
Please give me the  163 164 151 164 143 150 as a word.
Input:
stitch
You got it! You're super quick!
Flag: picoCTF{delusions_about_finding_values_3cc386de}
```

</b><h3>Flag</h3></b>
<pre>
picoCTF{delusions_about_finding_values_3cc386de}
</pre>
