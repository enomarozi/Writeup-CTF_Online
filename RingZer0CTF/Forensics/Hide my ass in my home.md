<h1><b>Hide my ass in my home</h1></b>
<pre>
<a href="https://ringzer0ctf.com/files/68789bfba0a2a675cab56db26e5d5bba.zip">File</a>
</pre>
</b><h3>Solution</h3></b>
<p>Ekstrak file</p>

```console
root@Python:/home/venom/Downloads# unzip 68789bfba0a2a675cab56db26e5d5bba.zip 
Archive:  68789bfba0a2a675cab56db26e5d5bba.zip
  inflating: .viminfo                
  inflating: .bash_profile           
 extracting: bob.tar.gz              
  inflating: .bashrc                 
 extracting: .bash_logout            
   creating: .mozilla/
   creating: .mozilla/extensions/
   creating: .mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/
  inflating: .mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/.fedora-langpack-install  
   creating: .mozilla/plugins/
  inflating: index.html              
  inflating: .bash_history           
  inflating: 1601066_559677267463652_942103441_n.jpg  
  inflating: Electro - Swing || Jamie Berry Ft. Octavia Rose - Delight.mp3  
   creating: .gnome2/
  inflating: you                     
  inflating: .me.swp    
```
<p>Disana terdapat file hidden mencurigakan yaitu<b> .me.swp</b>, eksekusi perintah strings pada file</p>

```console
root@Python:/home/venom/Downloads# strings -a .me.swp 
b0VIM 7.2
test
grosse-marde
~test/me
utf-8
U3210
#"! 
Flag-1s4g76jk89f
full of full 
and sunfull and 
i'm beautifull 
root@Python:/home/venom/Downloads# 
```
<p>Dan flag terdapat pada file hidden tersebut</p>
</b><h3>Flag</h3></b>
<pre>
Flag-1s4g76jk89f
</pre>
