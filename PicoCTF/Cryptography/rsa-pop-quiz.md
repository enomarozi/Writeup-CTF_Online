<h1>rsa-pop-quiz</h1>
<p>Class, take your seats! It's PRIME-time for a quiz... nc jupiter.challenges.picoctf.org 18821</p>
<h3>Solution</h3>
<p>Quiz Basic RSA</p>

```python3
from pwn import *
import gmpy2

#Question 1
r = remote("jupiter.challenges.picoctf.org",18821)
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
q = int(lines.decode('ascii').split('\n')[5][-5:])
p = int(lines.decode('ascii').split('\n')[6][-5:])
r.sendline("Y")
print(r.recvuntil('n:'))
r.sendline(str(int(q)*int(p)))
#Question 2
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
p = int(lines.decode('ascii').split('\n')[4][-5:])
n = int(lines.decode('ascii').split('\n')[5][-11:])
r.sendline("Y")
print(r.recvuntil('q:'))
r.sendline(str(int(n)//int(p)))
#Question 3
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
r.sendline("N")
#Question 4
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
q = int(lines.decode('ascii').split('\n')[4][-5:])
p = int(lines.decode('ascii').split('\n')[5][-5:])
r.sendline("Y")
print(r.recvuntil('totient(n):'))
r.sendline(str((p-1)*(q-1)))
#Question 5
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
m = int(lines.decode('ascii').split('\n')[4][11:])
e = int(lines.decode('ascii').split('\n')[5][3:])
n = int(lines.decode('ascii').split('\n')[6][3:])
r.sendline("Y")
print(r.recvuntil("ciphertext:"))
r.sendline(str(pow(m,e,n)))
#Question 6
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
r.sendline("N")
#Question 7
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
q = int(lines.decode('ascii').split('\n')[4][3:])
p = int(lines.decode('ascii').split('\n')[5][3:])
e = int(lines.decode('ascii').split('\n')[6][3:])
r.sendline("Y")
print(r.recvuntil("d:"))
d = gmpy2.invert(e,(p-1)*(q-1))
r.sendline(str(d))
#Question 8
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
p = int(lines.decode('ascii').split('\n')[4][3:])
c = int(lines.decode('ascii').split('\n')[5][12:])
e = int(lines.decode('ascii').split('\n')[6][3:])
n = int(lines.decode('ascii').split('\n')[7][3:])
r.sendline("Y")
print(r.recvuntil("plaintext:"))
q = (n//p)
d = gmpy2.invert(e,(p-1)*(q-1))
answer = pow(c,d,n)
r.sendline(bytes.fromhex(hex(answer)[2:]).decode('ascii'))
print("Your Flag : ",bytes.fromhex(hex(answer)[2:]).decode('ascii'))

```

<h3>Flag</h3>
<p>picoCTF{wA8_th4t$_ill3aGal..oa2d2239b}</p>
