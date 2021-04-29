<h1><b>Breakpoint #1</b></h1>
<pre>
Belum pernah mencoba breakpoint ? Oiya apa itu breakpoint, Breakpoint kurang lebih seperti instruksi break / stop pada address tertentu, karena breakpoint lah kita dapat mengetahui value dari register tersebut. Tapi mimin enggk terlalu bisa ngejelasin :( Maafkan yaaa

Hint: Breakpoint pada 0x135c, Kemudian ambil value dari address $rbp-0x94 menggunakan perintah x/100s. Ini command yang mimin pakai b *0x0000800135c, Tentunya ada beberapa karakter tidak sempura, tolong di imajinasikan yaa :D.

Challenge --> <a href='https://mega.nz/#!E9IGDRpQ!3CrLCsQZu_Sx6gNMoUF8SvAlvILNwsKXB7a2jSOkMcE'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Diberikan sebuah hint pada soal, tetapi disini kita akan coba cara lain, buka file dengan tool reverse ghidra, maka didapatkan pseudocode program seperti dibwah</p>

```c
while (local_9c < 0x1f) {
  if (local_9c % 10 == 0) {
    local_98[local_9c] = local_98[local_9c] + 4;
  }
  else {
    local_98[local_9c] = local_98[local_9c] + 5;
  }
  local_9c = local_9c + 1;
}
```
<p>Dan encrypt dari flag, sebagai berikut</p>
<pre>
0x3e,0x4f,0x41,0x4d,0x76,0x61,0x2c,0x6d,0x30,0x6f,0x5a,0x6f,0x2c,0x68,0x2e,0x5a,0x6f,0x2b,0x5a,0x5d,0x6d,0x2e,0x2f,0x66,0x6b,0x2b,0x2c,0x69,0x6f,0x3a,0x78
</pre>
<p align='justify'>Disana program terdapat komputasi iterasi dari encrypt flag, dan berikut penyelesaiannya</p>

```python3
flag = [0x3e,0x4f,0x41,0x4d,0x76,0x61,0x2c,0x6d,0x30,0x6f,0x5a,0x6f,0x2c,0x68,0x2e,0x5a,0x6f,0x2b,0x5a,0x5d,0x6d,0x2e,0x2f,0x66,0x6b,0x2b,0x2c,0x69,0x6f,0x3a,0x78]
for i in range(len(flag)):
    print(chr(flag[i]+5),end='')#CTFR{f1r5t_t1m3_t0_br34kp01nt?}
```
<h3><b>Flag</b></h3>
<pre>
CTFR{f1r5t_t1m3_t0_br34kp01nt?}
</pre>
