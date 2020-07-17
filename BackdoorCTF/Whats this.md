<h1><b>Whats this</b></h1>
<pre>
A n00b sent me this zip on a discord server, EZest challenge ever

<a href="http://static.beast.sdslabs.co/static/What's%20this%3F/UwU.zip">UwU.zip</a>
</pre>
<h3><b>Solution</b></h3>
<p>Unzip file, maka didapatkan banyak file, lalu eksekusi perintah grep dan output ke file text. pada file text cari flag dengan CTRL+F flag{</p>

```console
root@Python:/home/venom/Downloads# unzip UwU.zip 
Archive:  UwU.zip
  inflating: word/numbering.xml      
  inflating: word/settings.xml       
  inflating: word/fontTable.xml      
  inflating: word/styles.xml         
  inflating: word/document.xml       
  inflating: word/_rels/document.xml.rels  
  inflating: _rels/.rels             
  inflating: word/media/image2.png   
  inflating: word/theme/theme1.xml   
  inflating: word/media/image1.png   
  inflating: [Content_Types].xml     
root@Python:/home/venom/Downloads# grep -iR "flag{" >> file.txt
grep: input file ‘file.txt’ is also the output
root@Python:/home/venom/Downloads# leafpad file.txt 

```
<h3><b>Solution</b></h3>
<pre>
flag{OWO_wh4t5_th15???}
</pre>
