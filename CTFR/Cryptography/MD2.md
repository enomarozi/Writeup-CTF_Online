<h1><b>MD2</b></h1>
<pre>
Algoritma Message-Digest MD2 adalah fungsi hash kriptografi yang dikembangkan oleh Ronald Rivest pada tahun 1989. Algoritma ini dioptimalkan untuk komputer 8-bit. MD2 ditetapkan dalam RFC 1319.

Flag : CTFR{(MD2 dari "CTFR")}
</pre>
<h3><b>Solution</b></h3>
<p>Decrypt Hash MD2</p>

```python
from Crypto.Hash import MD2

init = MD2.new()
init.update('CTFR')
print('CTFR{'+init.hexdigest()+'}') #CTFR{9e873a7d36f0b41bf51ecc79289c8b7c}

```
<h3><b>Flag</b></h3>
<pre>
CTFR{9e873a7d36f0b41bf51ecc79289c8b7c}
</pre>
