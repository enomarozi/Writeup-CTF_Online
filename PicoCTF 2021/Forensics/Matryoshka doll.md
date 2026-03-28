<h1>Matryoshka doll</h1>
<h3>Description</h3>
<pre>
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one?
Image: <a href='https://challenge-files.picoctf.net/c_wily_courier/9bf118825bda566d4622b19d243e75877e2c17db745281bc5b0d11efd2278161/dolls.jpg'>dolls.jpg</a>
</pre>
<h3>Solution</h3>
<label>Recovery file di dalam file hingga mendapatkan flag.txt</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# foremost dolls.jpg   
Processing: dolls.jpg
|foundat=base_images/2_c.jpgUT	
*|

┌──(root㉿Kali)-[/home/venom/Downloads]
└─# cd output 
                   
┌──(root㉿Kali)-[/home/venom/Downloads/output]
└─# ls
audit.txt  png  zip
                                                                                                                                                         
┌──(root㉿Kali)-[/home/venom/Downloads/output]
└─# cd zip 
                                                                                                                                                         
┌──(root㉿Kali)-[/home/venom/Downloads/output/zip]
└─# ls
00000532.zip
                                                                                                                                                         
┌──(root㉿Kali)-[/home/venom/Downloads/output/zip]
└─# unzip 00000532.zip                     
Archive:  00000532.zip
  inflating: base_images/2_c.jpg     
                                                                                                                                                         
┌──(root㉿Kali)-[/home/venom/Downloads/output/zip]
└─# foremost base_images/2_c.jpg 
Processing: base_images/2_c.jpg
|foundat=base_images/3_c.jpgUT	
*|
                                                                                                                                                         
┌──(root㉿Kali)-[/home/venom/Downloads/output/zip]
└─# ls             
00000532.zip  base_images  output
                                                                                                                                                         
┌──(root㉿Kali)-[/home/venom/Downloads/output/zip]
└─# cd output/zip 
                                                                                                                                                         
┌──(root㉿Kali)-[/home/…/output/zip/output/zip]
└─# ls
00000366.zip
                                                                                                                                                         
┌──(root㉿Kali)-[/home/…/output/zip/output/zip]
└─# unzip 00000366.zip            
Archive:  00000366.zip
  inflating: base_images/3_c.jpg     
                                                                                                                                                         
┌──(root㉿Kali)-[/home/…/output/zip/output/zip]
└─# foremost base_images/3_c.jpg 
Processing: base_images/3_c.jpg
|foundat=base_images/4_c.jpgUT	
*|
                                                                                                                                                         
┌──(root㉿Kali)-[/home/…/output/zip/output/zip]
└─# cd output/zip 
                                                                                                                                                         
┌──(root㉿Kali)-[/home/…/output/zip/output/zip]
└─# unzip 00000241.zip 
Archive:  00000241.zip
  inflating: base_images/4_c.jpg     
                                                                                                                                                         
┌──(root㉿Kali)-[/home/…/output/zip/output/zip]
└─# foremost base_images/4_c.jpg 
Processing: base_images/4_c.jpg
|foundat=flag.txtUT	
*|
                                                                                                                                                         
┌──(root㉿Kali)-[/home/…/output/zip/output/zip]
└─# cd output/zip 
                                                                                                                                                         
┌──(root㉿Kali)-[/home/…/output/zip/output/zip]
└─# ls              
00000155.zip
                                                                                                                                                         
┌──(root㉿Kali)-[/home/…/output/zip/output/zip]
└─# unzip 00000155.zip 
Archive:  00000155.zip
 extracting: flag.txt                
                                                                                                                                                         
┌──(root㉿Kali)-[/home/…/output/zip/output/zip]
└─# cat flag.txt    
picoCTF{LL9lb1dR4QbGe4l4iWCvGq9pdtwt7392}
```
<h3>Flag</h3>
<pre>
picoCTF{LL9lb1dR4QbGe4l4iWCvGq9pdtwt7392}
</pre>

