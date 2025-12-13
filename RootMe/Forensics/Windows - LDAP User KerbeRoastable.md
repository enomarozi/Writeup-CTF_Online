<h1>Windows - LDAP User KerbeRoastable</h1>
<h3>Description</h3>
<label>During your investigations, you found a backup of the company’s KDAP made with ldap2json. Use the information in this dump to find the Kerberoastable user.

The flag is the email address of the Kerberoastable user.</label><a href='https://static.root-me.org/forensic/ch31/ch31.json'>File</a>
<h3>Solution</h3>
<label>Merupakan dump dari ldap2json</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# jq '.. | objects | select(.servicePrincipalName?) | "\(.mail)|\(.sAMAccountName)"' ch31.json
"null|krbtgt"
"alexandria.newton@rootme.local|a.newton"
"null|DC01$"
```
<h3>Flag</h3>
<pre>
alexandria.newton@rootme.local
</pre>
