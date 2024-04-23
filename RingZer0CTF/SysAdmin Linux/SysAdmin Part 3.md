<h1>SysAdmin Part 3</h1>
<p>Dig for flag.

User: architect<br>
Password: FLAG-232f99b4178bdc7fef7eb1f0f78831f9
<br>
Host: architect@ringzer0ctf.com -p 10152</p>
<h3>Deskription</h3>

```console
architect@sysadmin-track:/var/www$ cat index.php 
$mysqlDatabaseName ="arch";
$mysqlUserName ="arch";
$mysqlPassword ="asdftgTst5sdf6309sdsdff9lsdftz";
$mysqlHostName ="127.0.0.1";
$mysqlExportPath ="/var/tmp/ar.sql";
architect@sysadmin-track:/var/www$
mysql> select * from arch.flag 
    -> ;
+---------------------------------------+
| flag                                  |
+---------------------------------------+
| FLAG-55548fdb24a6ef248d8fdfde2720f6bd |
+---------------------------------------+
1 row in set (0.01 sec)

```
<p>Check index.php disana terdapat login mysql arch:asdftgTst5sdf6309sdsdff9lsdftz, dan select flag pada arch.flag</p>
<h3>Flag</h3>
<pre>FLAG-55548fdb24a6ef248d8fdfde2720f6bd</pre>
