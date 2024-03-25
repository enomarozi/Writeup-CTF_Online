<h1>Collaborative Development</h1>
<h3>Description</h3>
<p>My team has been working very hard on new features for our flag printing program! I wonder how they'll work together?
You can download the challenge files here:</p>
<a href='https://artifacts.picoctf.net/c_titan/179/challenge.zip'>File</a>
<h3>Solution</h3>
<p>git checkout</p>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# cd drop-in/
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# git branch
  feature/part-1
  feature/part-2
  feature/part-3
* main
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# git checkout feature/part-1
Switched to branch 'feature/part-1'
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# cat flag.py 
print("Printing the flag...")
print("picoCTF{t3@mw0rk_", end='')
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# git checkout feature/part-2
Switched to branch 'feature/part-2'
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# cat flag.py 
print("Printing the flag...")

print("m@k3s_th3_dr3@m_", end='')
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# git checkout feature/part-3
Switched to branch 'feature/part-3'
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# cat flag.py 
print("Printing the flag...")

print("w0rk_798f9981}")
root@xisco-VirtualBox:/home/xisco/Downloads/drop-in# 
```

```python3
print("Printing the flag...")

print("picoCTF{t3@mw0rk_", end='')
print("m@k3s_th3_dr3@m_", end='')
print("w0rk_798f9981}")
```
<h3>Flag</h3>
<pre>picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_798f9981}</pre>
