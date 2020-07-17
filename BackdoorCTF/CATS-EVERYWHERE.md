<h1><b>CATS-EVERYWHERE</b></h1>
<pre>
ssk497 is in love with cats and has lost his flag among them. 
He however remembers the location as <a href="https://drive.google.com/file/d/1hiRgH2IEUSUqzGpq5wLcYZDwT8F_K4hM">this</a> . 
Can you help him find the flag?
</pre>
<h3><b>Solution</h3></b>
<p>Decode file dan simpan ke format zip lalu ekstrak zip</p>

```console
root@Python:/home/venom/Downloads# cat challenge | base64 -d > file.zip
root@Python:/home/venom/Downloads# unzip file.zip 
Archive:  file.zip
  inflating: misc/1_24z2ltDIcYvnUOrwnlSWpQ.jpeg  
  inflating: misc/walk-3.gif         
  [+]........................[+]
  inflating: misc/.git/logs/HEAD     
  inflating: misc/.git/logs/refs/heads/master  
  inflating: misc/.git/logs/refs/heads/flag  
root@Python:/home/venom/Downloads# 
```
<p>Masuk ke direktori <b>.git/logs/refs/heads</b>, disana terdapat file flag dan master

```console
root@Python:/home/venom/Downloads/misc/.git/logs/refs/heads# cat master 
0000000000000000000000000000000000000000 4beefebc8bb3f6c244a9c3d9e1a421b0720ae9d2 Shubham Maheshwari <rmaheshwari05@gmail.com> 1520979615 +0530	commit (initial): Welcome
4beefebc8bb3f6c244a9c3d9e1a421b0720ae9d2 e137c2a57a87691dafb6ed25ee325c368d3fdb8e Shubham Maheshwari <rmaheshwari05@gmail.com> 1520979710 +0530	commit: to
e137c2a57a87691dafb6ed25ee325c368d3fdb8e 0fd58c79261fb2d7e416efd3b1bf64d143117191 Shubham Maheshwari <rmaheshwari05@gmail.com> 1520979771 +0530	commit: Backdoor
0fd58c79261fb2d7e416efd3b1bf64d143117191 959d9e12052dc17eaf813d97f357c57920824426 Shubham Maheshwari <rmaheshwari05@gmail.com> 1520979828 +0530	commit: CTF
959d9e12052dc17eaf813d97f357c57920824426 5f92b6942624f648581cf1b6ad549f1a653a5ffc Shubham Maheshwari <rmaheshwari05@gmail.com> 1520979892 +0530	commit: 2018
5f92b6942624f648581cf1b6ad549f1a653a5ffc 122ba9b6b90bae74847a418d9f402d4addd6a567 Shubham Maheshwari <rmaheshwari05@gmail.com> 1520979940 +0530	commit: .
122ba9b6b90bae74847a418d9f402d4addd6a567 6f6c3ccdebc718797cd32f23b837379080698d7b Shubham Maheshwari <rmaheshwari05@gmail.com> 1520979985 +0530	commit: LETS PLAY
root@Python:/home/venom/Downloads/misc/.git/logs/refs/heads# 
```
<p>Revert dan salin semua hasil revert git, disana terdapat total 6 part image</p> 

```python
import cv2

img_a = cv2.imread("a.jpg")
img_c = cv2.imread("c.jpg")
img_d = cv2.imread("d.jpg")
img_f = cv2.imread("f.jpg")
img_g = cv2.imread("g.jpg")
img_l = cv2.imread("b.jpg")
r_img = cv2.hconcat([img_a, img_c, img_d, img_f, img_l, img_g])
flip = cv2.flip(r_img,1)
cv2.imwrite("Solve_cat.jpg",flip)
```
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/Solve_cat.jpg">
</p>
<h3><b>Flag</h3></b>
<pre>
CTF{c0mm1t$_br1ng_b4ck_m3m0r1es}
</pre>
