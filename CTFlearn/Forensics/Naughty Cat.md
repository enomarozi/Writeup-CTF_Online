<h1><b>Naughty Cat</h1></b>
<pre>
I think my cat is hiding something...

<a href='https://ctflearn.com/challenge/download/890'>cut3_c4t.png</a>
</pre>
</b><h3>Solution</h3></b>
<p>Seperti biasa jika file PNG pertama-tama lakukan analisa dengan tool zsteg, kemudian binwalk atau foremost</p>

```console
root@Python:/home/venom/Downloads# zsteg cut3_c4t.png 
[?] 75618 bytes of extra data after image end (IEND), offset = 0x28e4b
extradata:0         .. file: RAR archive data, v5
    00000000: 52 61 72 21 1a 07 01 00  08 50 ee 43 0c 01 05 08  |Rar!.....P.C....|
    00000010: 00 07 01 01 87 ce 84 80  00 ec 80 04 54 29 02 03  |............T)..|
    00000020: 0b 8a cb 04 04 d1 85 05  20 67 59 20 ba 80 03 00  |........ gY ....|
    00000030: 0b 70 75 72 72 72 5f 32  2e 6d 70 33 0a 03 02 09  |.purrr_2.mp3....|
    00000040: eb 59 24 12 01 d6 01 8c  0b 9f 42 67 05 44 54 22  |.Y$.......Bg.DT"|
    00000050: 75 67 70 44 66 d9 6e 8c  04 80 80 d1 69 30 1a 5a  |ugpDf.n.....i0.Z|
    00000060: 52 c5 17 92 da 5b 4c 04  98 05 12 8c 22 97 13 03  |R....[L....."...|
    00000070: a8 98 0d 2e 20 20 97 10  12 d2 59 40 42 ba fa f3  |....  ....Y@B...|
    00000080: 9d d0 bc e7 7f fb f1 ff  f3 fe f4 34 d6 ea 4d ee  |...........4..M.|
    00000090: aa 77 33 a8 98 dc 5a 99  2b d3 1a 8b 13 11 31 6f  |.w3...Z.+.....1o|
    000000a0: 5f 35 33 11 d7 53 e9 69  4e 08 78 24 07 7d 01 9b  |_53..S.iN.x$.}..|
    000000b0: 2c 2a 25 1d 77 f2 11 77  fb 6b 74 06 c6 0d c5 8d  |,*%.w..w.kt.....|
    000000c0: d1 d1 e1 c1 cd 98 1b 53  3b 9b 3f 98 0f f7 ff ff  |.......S;.?.....|
    000000d0: ef d0 dd 91 cc df ff d6  45 b6 bf 53 4f ec 3b fe  |........E..SO.;.|
    000000e0: 5d 00 20 77 30 00 98 a8  b8 c8 e0 f9 11 21 31 41  |]. w0........!1A|
    000000f0: 51 59 69 87 8c cc d4 e0  e8 f7 c8 84 89 e6 48 4a  |QYi...........HJ|
imagedata           .. file: 64-bit XCOFF executable or object module not stripped
b2,r,lsb,xy         .. text: ["U" repeated 24 times]
b2,b,lsb,xy         .. text: ["U" repeated 24 times]
b2,rgb,lsb,xy       .. text: ["U" repeated 12 times]
b2,rgba,lsb,xy      .. text: ["W" repeated 16 times]
b4,r,lsb,xy         .. text: ["w" repeated 8 times]
b4,rgb,lsb,xy       .. text: ["w" repeated 24 times]
root@Python:/home/venom/Downloads# binwalk -e cut3_c4t.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 640 x 448, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
167499        0x28E4B         RAR archive data, version 5.x

root@Python:/home/venom/Downloads# cd _cut3_c4t.png.extracted/
root@Python:/home/venom/Downloads/_cut3_c4t.png.extracted# ls
28E4B.rar  29  29.zlib  purrr_2.mp3  y0u_4r3_cl0s3.rar
root@Python:/home/venom/Downloads/_cut3_c4t.png.extracted# file y0u_4r3_cl0s3.rar 
y0u_4r3_cl0s3.rar: data
```
<p>Dari hasil diatas saya mendapatkan file.Rar yang tertanam pada file.png, dan hasilnya sudah saya ekstrak mendapatkan 2 file lagi yaitu file.mp3 dan file.rar</p>
<p>Selanjutnya jika file rar diekstrak maka akan muncul error <b>is not RAR archive</b>, yang sepertinya ada kesalahan pada header</p>

```console
root@Python:/home/venom/Downloads/_cut3_c4t.png.extracted# xxd y0u_4r3_cl0s3.rar 
00000000: 4361 7421 1a07 0100 3392 b5e5 0a01 0506  Cat!....3.......
00000010: 0005 0101 8080 007c bc22 8d58 0203 3c90  .......|.".X..<.
00000020: 0104 c102 2067 b83d 0880 0300 0b66 316e  .... g.=.....f1n
00000030: 346c 6c79 2e74 7874 3001 0003 0f67 c16b  4lly.txt0....g.k
00000040: 5eea ad33 4801 8fe1 06a1 a1b4 9cd8 7130  ^..3H.........q0
00000050: d73e 873b f253 bf05 2444 2af9 7806 4f48  .>.;.S..$D*.x.OH
00000060: 7a08 9021 dcde 2e38 b30a 0302 7d84 a466  z..!...8....}..f
00000070: 0f01 d601 1485 be3b 2d96 5f8c 4f57 4711  .......;-._.OWG.
00000080: b087 2992 f043 d1ee ab9a 4f1a 3408 dc6a  ..)..C....O.4..j
00000090: fd43 2438 9f7c c279 9461 8767 409d 196d  .C$8.|.y.a.g@..m
000000a0: f2b3 4377 9aa9 f326 ba94 fa90 88e7 e1f3  ..Cw...&........
000000b0: 3f4f ca1b 9ccb 4b5f 566b 915a 0f03 7572  ?O....K_Vk.Z..ur
000000c0: 9c39 4967 f1c7 1499 10b4 78cf 6cbb eae9  .9Ig......x.l...
000000d0: 9035 eb88 bcff 9ae3 2d2e eab2 2cdc c281  .5......-...,...
000000e0: 8fde 1db7 a8ab ea0d 8863 8e80 0ee3 1c37  .........c.....7
000000f0: 9205 0565 28b2 cb2b d9fb 67d0 6263 bbe7  ...e(..+..g.bc..
00000100: be57 694a 1d77 5651 0305 0400            .WiJ.wVQ....
```
<p>Dan hasilnya ternyata benar, header file yaitu Cat! bukan Rar!. Ganti headernya ke Rar! dan jika berhasil, lanjut ekstrak file.rar</p>
<p>Tetapi ketika ekstrak file kita diminta untuk memasukan password rar. Selanjutnya analisa file.mp3 dan check spectogram dengan audacity tool</p>
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/Naughty_CAT.jpg'>
</p>
<p>Dan password didapatkan yaitu "sp3ctrum_1s_y0ur_fr13nd", lanjut ekstrak file rar dengan passwordnya. Maka didapatkan file f1n4lly.txt dan buka lalu decode base64 didalamnya</p>

```console
root@Python:/home/venom/Downloads/_cut3_c4t.png.extracted# strings -a f1n4lly.txt 
            __/| 
            \o.O|
       _____(___)______ 
      |       U        |________    __
      |ZjByM241MWNzX21h|        |__|  |_________
      |________________|NXQzcg==|::|  |        /
      |                \._______|::|__|       <
      |                         \::/  \._______\
      |	
      |	
root@Python:/home/venom/Downloads/_cut3_c4t.png.extracted# echo "ZjByM241MWNzX21hNXQzcg==" | base64 -d
f0r3n51cs_ma5t3r
root@Python:/home/venom/Downloads/_cut3_c4t.png.extracted# 
```
</b><h3>Flag</h3></b>
<pre>
CTFlearn{f0r3n51cs_ma5t3r}
</pre>
