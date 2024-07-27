<h1>First Find</h1>
<h3>Description</h3>
<p>Unzip this archive and find the file named 'uber-secret.txt'
<a href='https://artifacts.picoctf.net/c/500/files.zip'>Download zip file</a></p>
<h3>Solution</h3>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# unzip files.zip && cd files && grep -iR pico
   creating: files/acceptable_books/
   creating: files/acceptable_books/more_books/
  inflating: files/acceptable_books/more_books/40723.txt.utf-8  
  inflating: files/acceptable_books/17880.txt.utf-8  
  inflating: files/acceptable_books/17879.txt.utf-8  
  inflating: files/14789.txt.utf-8   
adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt:picoCTF{f1nd_15_f457_ab443fd1}
14789.txt.utf-8:brassa un picotin d'orge_. Comme depuis une demi-heure environ c'était
root@xisco-VirtualBox:/home/xisco/Downloads/files# 

<h3>Flag</h3>
<pre>
picoCTF{f1nd_15_f457_ab443fd1}
</pre>
