<h1>Secret of the Polyglot</h1>
<h3>Description</h3>
<p>The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file?
Download the suspicious file</p>
<a href='https://artifacts.picoctf.net/c_titan/99/flag2of2-final.pdf'>File</a>
<h3>Solution</h3>
<p>Identifikasi file, ganti format ke PNG dan ternyata ada binary pdf pada PNG</p>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# file flag2of2-final.pdf 
flag2of2-final.pdf: PNG image data, 50 x 50, 8-bit/color RGBA, non-interlaced
root@xisco-VirtualBox:/home/xisco/Downloads# mv flag2of2-final.pdf flag.png
root@xisco-VirtualBox:/home/xisco/Downloads# binwalk flag.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 50 x 50, 8-bit/color RGBA, non-interlaced
914           0x392           PDF document, version: "1.4"
1149          0x47D           Zlib compressed data, default compression

root@xisco-VirtualBox:/home/xisco/Downloads# 
```
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/PicoCTF2024/Forensics/Images/flag.png'>
</p>
<p>Dari PNG : picoCTF{f1u3n7_1n_</p>
<p>Extract File PDF</p>

```python3
with open('flag.png','rb') as f:
    f.seek(914)
    binary_data = f.read()
    with open("file.pdf",'wb') as pdf:
        pdf.write(binary_data)
```
<p>dari PDF : 1n_pn9_&_pdf_2a6a1ea8}</p>

<h3>Flag</h3>
<pre>picoCTF{f1u3n7_1n_pn9_&_pdf_2a6a1ea8}</pre>
