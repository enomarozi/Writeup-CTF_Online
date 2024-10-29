<h1>First Find</h1>
<h3>Description</h3>
<pre>
Unzip this archive and find the file named 'uber-secret.txt'
<a href='https://artifacts.picoctf.net/c/500/files.zip'>Download zip file</a>
</pre>
<h3>Solution</h3>
<p>Unzip,grep dan cat</p>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# unzip -l files.zip | grep -i 'uber-secret.txt'              
       31  2022-05-13 16:17   files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
                                                                                                                                                                                  
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# unzip files.zip                               
Archive:  files.zip
   creating: files/
   creating: files/satisfactory_books/
   creating: files/satisfactory_books/more_books/
  inflating: files/satisfactory_books/more_books/37121.txt.utf-8  
  inflating: files/satisfactory_books/23765.txt.utf-8  
  inflating: files/satisfactory_books/16021.txt.utf-8  
  inflating: files/13771.txt.utf-8   
   creating: files/adequate_books/
   creating: files/adequate_books/more_books/
   creating: files/adequate_books/more_books/.secret/
   creating: files/adequate_books/more_books/.secret/deeper_secrets/
   creating: files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/
 extracting: files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt  
  inflating: files/adequate_books/more_books/1023.txt.utf-8  
  inflating: files/adequate_books/46804-0.txt  
  inflating: files/adequate_books/44578.txt.utf-8  
   creating: files/acceptable_books/
   creating: files/acceptable_books/more_books/
  inflating: files/acceptable_books/more_books/40723.txt.utf-8  
  inflating: files/acceptable_books/17880.txt.utf-8  
  inflating: files/acceptable_books/17879.txt.utf-8  
  inflating: files/14789.txt.utf-8   
                                                                                                                                                                                  
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# cat files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
picoCTF{f1nd_15_f457_ab443fd1}
```
<h3>Flag</h3>
<pre>
picoCTF{f1nd_15_f457_ab443fd1}
</pre>
