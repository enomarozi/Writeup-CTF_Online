<h1><b>TIM</b></h1>
<pre>
Visit https://github.com/backdoor-ctf/TIM to get the flag.
</pre>
<h3><b>Solution</b></h3>
<p>Kita diminta untuk mencari flag pada link git repositori, setelah saya buka commit branch master disana terdapat nilai hexa yang dapat mencetak character ASCII, 
awalnya saya anggap itu flag dan setelah saya eksekusi</p>

```python
hexa = [0x47,0x41,0x4c,0x46,0x20,0x31,0x61,0x68,0x73,0x20,0x74,0x69,0x6d,0x6d,
        0x6f,0x63,0x20,0x68,0x63,0x61,0x65,0x20,0x66,0x6f,0x20,0x73,0x72,0x65,
        0x74,0x63,0x61,0x72,0x61,0x68,0x63,0x20,0x6f,0x77,0x74,0x20,0x74,0x73,
        0x72,0x69,0x66,0x20,0x6e,0x69,0x6f,0x4a]
flag = ""
for i in hexa:
    flag += chr(i)
print(flag[::-1])
```
<p>Dan hasilnya</p>
<pre>
Join first two characters of each commit sha1 FLAG
</pre>
<p> itu merupakan sebuah clue untuk mendapatkan flag, yaitu terdapat pada 2 string awal dari commit git. disini saya akan mencoba download repository</p>

```console
root@Python:/home/venom/Downloads# git clone https://github.com/backdoor-ctf/TIM
Cloning into 'TIM'...
remote: Enumerating objects: 202, done.
remote: Total 202 (delta 0), reused 0 (delta 0), pack-reused 202
Receiving objects: 100% (202/202), 202.01 KiB | 277.00 KiB/s, done.
Resolving deltas: 100% (48/48), done.
root@Python:/home/venom/Downloads# 
```
<p>Selanjutnya lihat seluruh commit sha1 dan export</p>

```console
root@Python:/home/venom/Downloads# cd TIM/.git/
root@Python:/home/venom/Downloads/TIM/.git# git rev-list --all
d444f3227636477902c4badc8e35a27cadab456c
009d01e1b04bf2bf2d9bebd666e8d167fae1dc1a
006d89cdd1a4ea3620bc6d4f865a2e341f5ee79a
00df98e1685e093c643657c6b68d31b9948927aa
00205355b3137a80aed60557a7ac6c208e7b5f5b
009d48a58a4a1e5e5f8b90ded89647a30fb8d94b
0082d99fe162d478070ce38f464691d28498675f
00de5fd5f77ea6f5b1ada422db6cef99ba5d3854
0046d01579b59ef375efb527f793742bda0eeaa4
00d3be57b5291c68585e8eaadc8c159bbfe7d8e9
05928975ce6acd49c30a5314fa4019d73046ec84
676c0278c6602ca337e0666347eed1c62b1e5e27
dd75fd89fe6584f7e5d231a3ae63bce5abdeb0b0
f161a85dd594c818598300a3865d967146e63257
ee11996003d7b7d4ec82966f78e5766c3531ca43
e7e9098b9033c65904d2ea2a96854508b92dc6b2
5fc82b179697691220015a690bc4462b46b36651
1abb199ea8cde78dd9828f16128d520c7e3d628d
d563953b2006e3c933be9bbb31bb3656c0dd6565
8e3f259067e5c2af568a8b9610053307175281d2
e722f52fee8e9e19ac5c0fdcad127c61c2121c86
5ff8ede60a7a484a1fc65e3412781ca13248af4b
cb36286b4a7cced8194b005ef163f4376ba0263b
94763df5b6cbbd493c13033b18e271f8f38b43c6
120817977b312fbf2d8ca67cc663c856bad57427
374c0c65122bec69e0f5347b8ec1fc134ae77e3b
1e97cecc69e81ffee10dcd51ae3141387226eca8
d96e3bb88eb51623ab69f642aa5887104ce6ec15
8d156110162d6a206306d34e2a01df1a5bad5965
edc07354036ced04650047b51dcc5cfcf2d6c814
f2c2f0b9cced296a780fcc43b7048dc604f5b020
1dafac2b3f7bcd0611e5378005584ebfd155adf5
b0d0958ff37242adf7d18d0cb885cdf23e48de00
4bf2ee5453905bff33ed5f3cafa6e57459bf82fe
f4ee637574d1432cd18aa1121312a2e895acf652
80e65a28363e0c6c68a8b9cf57087380fb33c05f
fcab38040f5dc78762e230abc5f10f89eade39eb
8b96e9a576fdc1f979df6d63321d7fac91eb782c
8632c5252037e75a9feffeac84846dfd36a97b68
0a3cf4d266187272dd064aa480547dba835b05a5
9f8ef8c5a9039a9c149fb50c5750183e70cac7e2
75ae4979ffbb663dbc665495cf892e108114adcd
0068a486c186d9e38e51f87720a0dd65c3e8384d
0084948308ac5f84d2f15df4010926968d4ea4fb
000bd360dd30bef0952dc5e78d0552acbb77cc28
003cd8f7c9f44e5ef914a23b89683381261aeb1a
00a0913f7281b805f14f220d422e253ad5e17d91
004c8ec471a5e9f8177eac3cabea75b6a1b34d60
009daea0f203c4c5e968cf4f4dd0b30cd241105c
00ba12f761b4b630edd4b09ebf28a5f4b0bf00ac
0075376f5b95ab02608746da37cd7bfa54ccbc89
root@Python:/home/venom/Downloads/TIM/.git# git rev-list --all > commit_git.log
```
<p>Selanjutnya ambil 2 string dari setiap commit sesuai yang diminta clue</p>

```python
git_log = open("git.log")
flag = ""
for i in git_log:
    i = i.strip("\n")
    flag += i[:2][::-1]
print(flag[::-1])
```
<p>Hasilnya</p>
<pre>
000000000000000000759f0a868bfc80f44bb01df2ed8dd91e371294cb5fe78ed51a5fe7eef1dd6705000000000000000000d4
</pre>

<h3><b>Flag</b></h3>
<pre>
759f0a868bfc80f44bb01df2ed8dd91e371294cb5fe78ed51a5fe7eef1dd6705
</pre>
