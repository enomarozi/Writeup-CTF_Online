<h1>EXIF - Thumbnail</h1>
<h3>Description</h3>
<label>Find the password hidden in this image in JPG format.</label><a href='https://static.root-me.org/steganographie/ch10/ch10.jpg'>File</a>
<h3>Solution</h3>
<label>Thumbnail image, extract 2 tingkat thumbnail image</label>

```console
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# exiftool ch10.jpg| grep Thumbnail                                                           
Thumbnail Offset                : 202
Thumbnail Length                : 41506
Thumbnail Image                 : (Binary data 41506 bytes, use -b option to extract)

┌──(root㉿Venom)-[/home/venom/Downloads]
└─# exiftool -b -ThumbnailImage ch10.jpg > tingkat1.jpg 
                                                                                                                                                                
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# eog tingkat1.jpg                                   

┌──(root㉿Venom)-[/home/venom/Downloads]
└─# exiftool tingkat1.jpg| grep Thumbnail 
Thumbnail Offset                : 202
Thumbnail Length                : 15957
Thumbnail Image                 : (Binary data 15957 bytes, use -b option to extract)
                                                                                                                                                              
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# exiftool -b -ThumbnailImage tingkat1.jpg > tingkat2.jpg

┌──(root㉿Venom)-[/home/venom/Downloads]
└─# eog tingkat2.jpg  
```
<h3>Flag</h3>
<pre>
B33r1sG00d!
</pre>
