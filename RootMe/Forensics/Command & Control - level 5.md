<h1>Command & Control - level 5</h1>
<h3>Description</h3>
<label>Berthier, the malware seems to be manually maintened on the workstations. Therefore it’s likely that the hackers have found all of the computers’ passwords.
Since ACME’s computer fleet seems to be up to date, it’s probably only due to password weakness. John, the system administrator doesn’t believe you. Prove him wrong!

Find john password.

The uncompressed memory dump md5 hash is e3a902d4d44e0f7bd9cb29865e0a15de</label>
<a href='https://static.root-me.org/forensic/ch2/ch2.tbz2'>File</a>
<h3>Solution</h3>
<label>Hashdump dari memory dump</label>

```console
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# vol -f ch2.dmp windows.hashdump
Volatility 3 Framework 2.27.0
/root/volatility3/volatility3/framework/deprecation.py:28: FutureWarning: This API (volatility3.plugins.windows.registry.hashdump.Hashdump.run) will be removed in the first release after 2026-09-25. This plugin has been renamed, please call volatility3.plugins.windows.registry.hashdump.Hashdump rather than volatility3.plugins.windows.hashdump.Hashdump.
  warnings.warn(

User	rid	lmhash	nthash
/root/volatility3/volatility3/framework/deprecation.py:105: FutureWarning: This plugin (volatility3.plugins.windows.hashdump.Hashdump) has been renamed and will be removed in the first release after 2026-09-25. Please ensure all method calls to this plugin are replaced with calls to volatility3.plugins.windows.registry.hashdump.Hashdump
  warnings.warn(

Administrator	500	aad3b435b51404eeaad3b435b51404ee	31d6cfe0d16ae931b73c59d7e0c089c0
Guest	501	aad3b435b51404eeaad3b435b51404ee	31d6cfe0d16ae931b73c59d7e0c089c0
John Doe	1000	aad3b435b51404eeaad3b435b51404ee	b9f917853e3dbf6e6831ecce60725930
                                                                                                                                                                                  
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# nano windows_hash

┌──(root㉿Venom)-[/home/venom/Downloads]
└─# cat windows_hash 
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
John Doe:1000:aad3b435b51404eeaad3b435b51404ee:b9f917853e3dbf6e6831ecce60725930:::
                                                                                                                                                                                  
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# john --wordlist=/usr/share/wordlists/rockyou.txt --format=NT windows_hash 
Created directory: /root/.john
Using default input encoding: UTF-8
Loaded 2 password hashes with no different salts (NT [MD4 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=12
Press 'q' or Ctrl-C to abort, almost any other key for status
passw0rd         (John Doe)     
                 (Administrator)     
2g 0:00:00:00 DONE (2025-12-04 03:31) 100.0g/s 240000p/s 240000c/s 307200C/s Liverpool..525252
Warning: passwords printed above might not be all those cracked
Use the "--show --format=NT" options to display all of the cracked passwords reliably
Session completed.                                                                                                                                                                           
```
<h3>Flag</h3>
<pre>
passw0rd
</pre>
