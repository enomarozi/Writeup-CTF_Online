<h1><b>Binwalk</h1></b>
<pre>
Here is a file with another file hidden inside it. Can you extract it? 
https://mega.nz/#!qbpUTYiK!-deNdQJxsQS8bTSMxeUOtpEclCI-zpK7tbJiKV0tXYY
</pre>
</b><h3>Solution</h3></b>
<p>Diberikan 1 file image JPEG yang aslinya merupakan file PNG, identifikasi dengan binwalk tool ternyata pada file image juga terdapat file image PNG, ekstrak file dengan foremost dan buka file PNG</p>

```console
root@Python:/home/venom/Downloads# ls
PurpleThing.jpeg
root@Python:/home/venom/Downloads# file PurpleThing.jpeg 
PurpleThing.jpeg: PNG image data, 780 x 720, 8-bit/color RGBA, non-interlaced 
root@Python:/home/venom/Downloads# binwalk PurpleThing.jpeg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 780 x 720, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, best compression
153493        0x25795         PNG image, 802 x 118, 8-bit/color RGBA, non-interlaced

root@Python:/home/venom/Downloads# foremost PurpleThing.jpeg 
Processing: PurpleThing.jpeg
|*|
root@Python:/home/venom/Downloads# cd output/png/
root@Python:/home/venom/Downloads/output/png# ls
00000000.png  00000299.png
root@Python:/home/venom/Downloads/output/png# eog *
```
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/00000299.png'>
</p>
</b><h3>Flag</h3></b>
<pre>
ABCTF{b1nw4lk_is_us3ful}
</pre>
