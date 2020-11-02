<h1><b>Admin Portal</h1></b>
<pre>
Diberikan sebuah password form dan source code
</pre>
</b><h3>Solution</h3></b>
<p>Dibawah source codenya</p>

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
<p align='justify'>Pada source code diatas Flag bisa didapatkan jika kita me-set password tanpa syntax SQL, selanjutnya terdapat variabel $pass = md5(admin1674227342) yaitu --> 0e463854177790028825434984462555
Dan selanjutnya jika kita set password == variabel $pass && variabel $pass !== set password</p>
<p align='justify'>Disini kita hanya perlu mengetahui perbedaan == dan ===, jika == tidak akan membedakan tipe data, dan === itu artinya akan membedakan sampai ke type data.
Pada soal terdapat variabel $pass yang hasil MD5nya --> 0e463854177790028825434984462555, diketahui persamaan matematika pada program huruf 'e' itu artinya exponen
dan pada MD5 tersebut 0e4638..... artinya 0 pangkat 4638..... = 0</p>
<p align='justify'>Jadi cara kita membypass statment pertama dengan input dengan string 0, selanjutnya statment panjangan kita hanya perlu membuat 0 hingga panjangannya 32 character
yang sama dengan panjang MD5</p>
<pre>
input password --> 00000000000000000000000000000000
</pre>
</b><h3>Flag</h3></b>
<pre>
FLAG-K7PY48gt02T1yvoO9jzP694FztgR1jIS
</pre>
