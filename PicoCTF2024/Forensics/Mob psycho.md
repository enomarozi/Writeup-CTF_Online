<h1>Mob psycho</h1>

<h3>Description</h3>
<p>
Can you handle APKs?
Download the android apk.</p>
<a href='https://artifacts.picoctf.net/c_titan/143/mobpsycho.apk'>File</a>

<h3>Solution</h3>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# unzip mobpsycho.apk | grep -i flag
  inflating: res/color/flag.txt      
root@xisco-VirtualBox:/home/xisco/Downloads# cat res/color/flag.txt 
7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f37303364643965667d

```

```python
file = open('res/color/flag.txt','r').read()
print(bytes.fromhex(file).decode('ascii'))
```

<h3>Flag</h3>
<pre>picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_703dd9ef}</pre>
