<h1><b>Taking LS</h1></b>
<pre>
Just take the Ls. Check out this zip file and I be the flag will remain hidden. 
https://mega.nz/#!mCgBjZgB!_FtmAm8s_mpsHr7KWv8GYUzhbThNn0I8cHMBi4fJQp8
</pre>
</b><h3>Solution</h3></b>
<p>Terdapat 1 file PDF berpassword, cari password pada hidden direktori .ThePassword/</p>

```console
root@Python:/home/venom/Downloads# ls
'The Flag.zip'
root@Python:/home/venom/Downloads# unzip The\ Flag.zip 
Archive:  The Flag.zip
   creating: The Flag/
  inflating: The Flag/.DS_Store      
   creating: __MACOSX/
   creating: __MACOSX/The Flag/
  inflating: __MACOSX/The Flag/._.DS_Store  
   creating: The Flag/.ThePassword/
  inflating: The Flag/.ThePassword/ThePassword.txt  
  inflating: The Flag/The Flag.pdf   
  inflating: __MACOSX/The Flag/._The Flag.pdf  
root@Python:/home/venom/Downloads# cd The\ Flag/.ThePassword/
root@Python:/home/venom/Downloads/The Flag/.ThePassword# ls
ThePassword.txt
root@Python:/home/venom/Downloads/The Flag/.ThePassword# cat ThePassword.txt 
Nice Job!  The Password is "Im The Flag".
root@Python:/home/venom/Downloads/The Flag/.ThePassword# cd ..
root@Python:/home/venom/Downloads/The Flag# ls
'The Flag.pdf'
root@Python:/home/venom/Downloads/The Flag# xdg-open 
.DS_Store     The Flag.pdf  .ThePassword/ 
root@Python:/home/venom/Downloads/The Flag# xdg-open The\ Flag.pdf 
```
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/Taking%20LS.jpg'>
</p>
</b><h3>Flag</h3></b>
<pre>
ABCTF{T3Rm1n4l_is_C00l}
</pre>
