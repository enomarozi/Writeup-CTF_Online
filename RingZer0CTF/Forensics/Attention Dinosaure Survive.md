<h1><b>Dinosaure Survive</h1></b>
<pre>
<a href="https://ringzer0ctf.com/files/c7afb12d982f3683cc3b27233869157d.zip">File</a>
</pre>
</b><h3>Solution</h3></b>
<p>Ekstrak file dengan binwalk lalu eksekusi perintah strings dan grep pada file</p>

```console
root@Python:/home/venom/Downloads# unzip c7afb12d982f3683cc3b27233869157d.zip 
Archive:  c7afb12d982f3683cc3b27233869157d.zip
  inflating: 0b02119984a7cee0ba83d55425b9491f.E01  
root@Python:/home/venom/Downloads# binwalk -e 0b02119984a7cee0ba83d55425b9491f.E01 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
89            0x59            Zlib compressed data, default compression
143974        0x23266         Zlib compressed data, default compression
144620        0x234EC         Zlib compressed data, default compression
145400        0x237F8         Zlib compressed data, default compression
157615        0x267AF         PDF document, version: "1.2"
[+].................................................................[+]
958853        0xEA185         Zlib compressed data, default compression

root@Python:/home/venom/Downloads# cd _0b02119984a7cee0ba83d55425b9491f.E01.extracted/
root@Python:/home/venom/Downloads/_0b02119984a7cee0ba83d55425b9491f.E01.extracted# strings -a * | grep -i flag
/Flags 262176
/Flags 262240
/Flags 96
/Flags 32
flag-pc
flag-6b96e212b3f85968db654f7892f06122
flag-6b96e212b3f85968db654f7892f06122
flag-6b96e212b3f85968db654f7892f06122
root@Python:/home/venom/Downloads/_0b02119984a7cee0ba83d55425b9491f.E01.extracted#

```
</b><h3>Flag</h3></b>
<pre>
flag-6b96e212b3f85968db654f7892f06122
</pre>
