<h1>PNG - Least Significant Bit</h1>
<h3>Description</h3>
<label>Uncle Scrooge does not only love gold, seems he also likes secrets. Find what is hidden in the image.</label><a href='https://static.root-me.org/steganographie/ch9/ch9.png'>File</a>
<h3>Solution</h3>
<label>Salah satu teknik steganography LSB</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# stegolsb -v extract ch9.png --column-step 2 --rows 1 --columns 128
                          _                   _     _
                      ___| |_ ___  __ _  ___ | |___| |__
                     / __| __/ _ \/ _` |/ _ \| / __| '_ \
                     \__ \ ||  __/ (_| | (_) | \__ \ |_) |
                     |___/\__\___|\__, |\___/|_|___/_.__/
                                  |___/


 
07:34:49 [DEBUG] Image size: 225x225
07:34:49 [DEBUG] Bits [0], channels RGB, column step 2, row step 1
07:34:49 [INFO] Hidden data:
16:TFdmMDdyc01iaUE2ÿúÿÿ
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# echo 'TFdmMDdyc01iaUE2' | base64 -d
LWf07rsMbiA6 
```
<h3>Flag</h3>
<pre>
LWf07rsMbiA6
</pre>
