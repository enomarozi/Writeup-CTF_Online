<h1><b>FIESTA</b></h1>
<pre>
Shishir just bought a new Ford Fiesta but naughty n00b just locked his door and challenged him to unlock it.
n00b gave shishir the following 2 files:
ciphertext: http://static.beast.sdslabs.co/static/FIESTA/ciphertext
fiesta.py: http://static.beast.sdslabs.co/static/FIESTA/fiesta.py
</pre>
<h3><b>Solution</b></h3>
<p>Disini kita diminta menjadi cryptanalys untuk me-reversing chipertext ke plaintext tanpa key, disini kita hanya dimodali program proses encrypt-nya</p>

```python
from base64 import b64encode

(a,b,c,d) = (10979532922714726005950999456852628059532311148206783766093435123197232647457984708147232760389536909544842840637467696937247459692963867502414810678283883,\
		 11016056395188421557504812643924110754613022033438352774235720751108752406710922147713801605550783526394303466164956199373182495367988753890137739783998143,\
		 11705303629766926756962115878148813784738656130121062206508648548600939875290939376784022191357893940268634609309770116427301779332901287292278132375644469,\
		 12146675268984268926692535405591086289578472817949676001189738433298651131667956807702171430844914392838506834908686053308289180788419151330429940895945011)

def F(x):
	return (a*x*x + b*x + c)%d

def G(message):
	n = len(message)
	L = message[0:(n/2)]
	R = message[(n/2):n]
	L = int(L.encode("hex"), 16)
	R = int(R.encode("hex"), 16)

	return (L,R)

def fiestel(L, R):
	rounds = 4
	for i in xrange(rounds):
		(L,R) = (R, L^F(R))
	L = hex(L).replace("0x", "").replace("L", "")
	R = hex(R).replace("0x", "").replace("L", "")
	return R+L

FLAG = "CTF{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}"	# REDACT THIS THING
(L, R) = G(FLAG)
print b64encode(fiestel(L, R).decode("hex"))
```
<p>Flag Encrypt</p>
<pre>
T/whKxFufFpn8ZMNJGInScjtJBgUefZYSx7BXizd50ged7QNqmHm49+3V0msMCQgJYVV6eH8xqfYDSguMKmIFiL4RVV1gdUm92gWBcDRG8TLymjbG1/8TSdNEEtaQLJ9+tn6C2gnmEgkgop/EAF8NY1kB99f1SuGOGOGjDKhSUQ=
</pre>
<p>Pada program diatas kita hanya perlu tau bagaimana operasi pada fungsi fiestel yang menukar letak L dan R disetiap iterasi dengan fungsi xor sehingga menghasilkan Flag Encrypt</p>
<p>Dan berikut program me-reversing(decrypt) dari ciphertext yang dihasilkan oleh program diatas</p>

```python
import base64

(a,b,c,d) = (10979532922714726005950999456852628059532311148206783766093435123197232647457984708147232760389536909544842840637467696937247459692963867502414810678283883,\
		 11016056395188421557504812643924110754613022033438352774235720751108752406710922147713801605550783526394303466164956199373182495367988753890137739783998143,\
		 11705303629766926756962115878148813784738656130121062206508648548600939875290939376784022191357893940268634609309770116427301779332901287292278132375644469,\
		 12146675268984268926692535405591086289578472817949676001189738433298651131667956807702171430844914392838506834908686053308289180788419151330429940895945011)

def F(x):
	return (a*x*x + b*x + c)%d

enc = "T/whKxFufFpn8ZMNJGInScjtJBgUefZYSx7BXizd50ged7QNqmHm49+3V0msMCQgJYVV6eH8xqfYDSguMKmIFiL4RVV1gdUm92gWBcDRG8TLymjbG1/8TSdNEEtaQLJ9+tn6C2gnmEgkgop/EAF8NY1kB99f1SuGOGOGjDKhSUQ="
text = base64.b64decode(enc)
result = "".join([hex(i)[2:].rjust(2,"0") for i in text])
R = int(result[128:],16)
L = int(result[:128],16)
for i in range(4):
    (L,R) = (R, F(R) ^ L)
print(bytes.fromhex(hex(R)[2:])+bytes.fromhex(hex(L)[2:]))
```
<h3><b>Flag</b></h3>
<pre>
CTF{why_ar3_y0u_guys_s0_n00b_that_w3_have_to_giv3_y0u_such_3asy_chall3ng3}
</pre>
