<h1><b>you can't see me</h1></b>
<pre>
'...reading transmission... Y.O.U. .C.A.N.'.T. .S.E.E. .M.E. ...transmission ended...' 
Maybe something lies in /problems/you-can-t-see-me_3_1a39ec6c80b3f3a18610074f68acfe69.
</pre>
</b><h3>Solution</h3></b>
<p>Connect terminal dan cat file</p>

```console
xvenom@pico-2018-shell:/problems/you-can-t-see-me_3_1a39ec6c80b3f3a18610074f68acfe69$ ls -al                  
total 60                                                                                                      
drwxr-xr-x   2 root       root        4096 Mar 25  2019 
-rw-rw-r--   1 hacksports hacksports    57 Mar 25  2019 .                                                     
drwxr-x--x 556 root       root       53248 Mar 25  2019 
xvenom@pico-2018-shell:/problems/you-can-t-see-me_3_1a39ec6c80b3f3a18610074f68acfe69$ cat .*                  
cat: .: Is a directory     
picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_cf5156ef}                                                      
cat: .: Is a directory                                                                                        
xvenom@pico-2018-shell:/problems/you-can-t-see-me_3_1a39ec6c80b3f3a18610074f68acfe69$
```
</b><h3>Flag</h3></b>
<pre>
picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_cf5156ef} 
</pre>
