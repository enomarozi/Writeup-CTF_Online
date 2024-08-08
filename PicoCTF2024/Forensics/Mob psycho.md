<h1>Mob psycho</h1>

<h3>Description</h3>
<p>
Can you handle APKs?
Download the android apk.</p>
<a href='https://artifacts.picoctf.net/c_titan/143/mobpsycho.apk'>File</a>

<h3>Solution</h3>

```bash
#!/bin/bash

extract=$(unzip "mobpsycho.apk")
path=$(find . -iname "*.txt")
hex=$(cat $path)
hextotext=$(python3 -c "print(bytes.fromhex('"$hex"').decode('ascii'))")
echo $hextotext
```

```console
root@xisco-VirtualBox:/home/xisco/Downloads# ./script.sh 
picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_85dbd215}
```

<h3>Flag</h3>
<pre>picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_703dd9ef}
</pre>
