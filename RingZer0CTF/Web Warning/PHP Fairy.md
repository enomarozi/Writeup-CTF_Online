<h1>PHP Fairy</h1>
<h3>Description</h3>
<label>https://ringzer0ctf.com/challenges/254</label>
<h3>Solution</h3>
<label>Source codenya</label>

```php
<?php
$output = "";
if (isset($_GET['code'])) {
  $content = file_get_contents(__FILE__);
  $content = preg_replace('/FLAG\-[0-9a-zA-Z_?!.,]+/i', 'FLAG-XXXXXXXXXXXXXXXXXXXXXXX', $content);
  echo '<div class="code-highlight">';
  highlight_string($content);
  echo '</div>';
}

if (isset($_GET['pass'])) {
  if(!preg_match('/^[^\W_]+$/', $_GET['pass'])) {
    $output = "Don't hack me please :(";
  } else {

    $pass = md5("admin1674227342");
    if ((((((((($_GET['pass'] == $pass)))) && (((($pass !== $_GET['pass']))))) || ((((($pass == $_GET['pass'])))) && ((($_GET['pass'] !== $pass)))))))) { // Trolling u lisp masta
      if (strlen($pass) == strlen($_GET['pass'])) {
        $output = "<div class='alert alert-success'>FLAG-XXXXXXXXXXXXXXXXXXXXXXX</div>";
      } else {
        $output = "<div class='alert alert-danger'>Wrong password</div>";
      }
    } else {
      $output = "<div class='alert alert-danger'>Wrong password</div>";
    }
  }
}
?>
```
<label>$pass = md5(admin1674227342) yaitu --> 0e463854177790028825434984462555</label>
<pre>
== bertipe longgar (jika input type string dan berkemungkinan integer akan dianggap integer)
=== identik (jika tipe data dan content sama)
</pre>
<label>Payload : 00000000000000000000000000000000</label>
<h3>Flag</h3>
<pre>
FLAG-K7PY48gt02T1yvoO9jzP694FztgR1jIS
</pre>
