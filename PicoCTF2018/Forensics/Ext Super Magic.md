<h1><b>Ext Super Magic</h1></b>
<pre>
We salvaged a ruined Ext SuperMagic II-class mech recently and pulled the <a href="https://2018shell.picoctf.com/static/9f563e291d847c30879277c3b6c16260/ext-super-magic.img">filesystem</a> out of the black box. 
It looks a bit corrupted, but maybe there's something interesting in there. 
You can also find it in /problems/ext-super-magic_2_5e1f8bfb15060228f577045924e4fca8 on the shell server.
</pre>
</b><h3>Solution</h3></b>
<p>ext (<a href="https://en.m.wikipedia.org/wiki/Extended_file_system">extended file system</a>) merupakan file system berbasis linux. terdapat data corrupt pada file 
yang diberikan dari hasil identifikasi file</p>

```console
root@Python:/home/venom/Downloads# file ext-super-magic.img 
ext-super-magic.img: data
root@Python:/home/venom/Downloads# debugfs ext-super-magic.img 
debugfs 1.45.6 (20-Mar-2020)
debugfs: Bad magic number in super-block while trying to open ext-super-magic.img
```
<p>Sesuai identifikasi, data corrupt terdapat pada magic number super-block, magic-number merupakan salah satu signature dari ext2 yang biasanya berada pada posisi 1080-1081 dengan value 0x53 dan 0xef</p>
<p>Ganti value pada index 1080-1081 menjadi 0x53 0xef dengan hex-editor</p>
<p>Sebelum diganti</p>
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/PicoCTF2018/Forensics/Images/Ext%20Super%20Magic2.jpg">
</p>
<p>Sesudah diganti</p>
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/PicoCTF2018/Forensics/Images/Ext%20Super%20Magic1.jpg">
</p>
<p>Identifikasi file kembali, dan jika sudah fix. ekstrak file dengan binwalk dan buka file image flag.jpg</p>

```console
root@Python:/home/venom/Downloads# file ext-super-magic.img 
ext-super-magic.img: Linux rev 1.0 ext2 filesystem data, UUID=14573d1a-d758-4679-afdc-c5ac87c10185 (large files)
root@Python:/home/venom/Downloads# binwalk -e ext-super-magic.img 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Linux EXT filesystem, blocks count: 5120, image size: 5242880, rev 1.0, ext2 filesystem data, UUID=14573d1a-d758-4679-afdc-c5ac87c187c1

root@Python:/home/venom/Downloads# cd _ext-super-magic.img.extracted/ext-root/
root@Python:/home/venom/Downloads/_ext-super-magic.img.extracted/ext-root# eog flag.jpg 
```
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/PicoCTF2018/Forensics/Images/flag.jpg">
</p>
</b><h3>Flag</h3></b>
<pre>
picoCTF{ab0CD63BC762514ea2f4fc9eDEC8cb1E}
</pre>
