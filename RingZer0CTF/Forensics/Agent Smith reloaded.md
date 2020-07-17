<h1><b>Agent Smith reloaded</h1></b>
<pre>
<a href="https://ringzer0ctf.com/files/2b4d08e1a1eac8a8c9034036d420bd88.zip">File</a>
</pre>
</b><h3>Solution</h3></b>
<p>File merupakan extended file system3 linux, ekstrak file dengan perintah foremost lalu tuju file zip, dan ekstrak file zip. Disana file zip meminta passsword untuk ekstrak.</p>

```console
root@Python:/home/venom/Downloads# file BK 
BK: Linux rev 1.0 ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1c9a80
root@Python:/home/venom/Downloads# foremost BK
Processing: BK
|foundat=mimetypeapplication/vnd.oasis.opendocument.graphicsPK
foundat=meta.xml���n�0��}
��
6���D���"��T�m��ld��}��6�]E{�������Ǯ�޸6B�
�	�T1!�
�z~���}��T//�r�:.m�qK"'�O�
�Z��qL��D������2z��A��b���I
�;�֔gזz͍�r]��f]K)u2�e�
*|
root@Python:/home/venom/Downloads# cd output/
root@Python:/home/venom/Downloads/output# cd zip/
root@Python:/home/venom/Downloads/output/zip# unzip 00002456.zip 
Archive:  00002456.zip
warning [00002456.zip]:  1024 extra bytes at beginning or within zipfile
  (attempting to process anyway)
[00002456.zip] secret.txt password: 
```
<p>Dan sudah dicari-cari password pada file challenge, tidak didapatkan juga. Tetapi kita medapatkan clue, yaitu ekstrak file dengan binwalk terlebih dahulu, lihat file TODO.me hasil ekstrak</p>

```console
root@Python:/home/venom/Downloads# binwalk -e BK 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Linux EXT filesystem, blocks count: 5120, image size: 5242880, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c

root@Python:/home/venom/Downloads# cd _BK.extracted/
root@Python:/home/venom/Downloads/_BK.extracted# cd ext-root/
root@Python:/home/venom/Downloads/_BK.extracted/ext-root# strings TODO.me 
-cryt my password file with Secret Vault Encrypt  
-bring back milk 
-buy flower for my love ! 
-restric my my little brother permission to delete file. 
root@Python:/home/venom/Downloads/_BK.extracted/ext-root# 
```
<p>Disana dia bilang bahwa file diencrypt dengan password yang lemah, jadi kita diminta untuk bruteforce file zip</p>

```python
import zipfile

with zipfile.ZipFile("file.zip","r") as zip_ref:
    file = open("/home/venom/CreateWordlist/rockyou.txt")
    for i in file:
        password = i.strip("\n")
        try:
            zip_ref.extractall(pwd=password.encode('utf8'))
            print("[+]Password Found -->",password)
            break
        except:
            pass
```
<p>Hasil Bruteforce password dengan wordlist rockyou.txt</p>
<pre>
[+]Password Found --> 12345
</pre>
<p>File secret.txt sudah didapatkan, dan lihat flag pada file tersebut</p>

```console
root@Python:/home/venom/Downloads# cat secret.txt 
FLAG-menummenum
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
FLAG-menummenum
</pre>
