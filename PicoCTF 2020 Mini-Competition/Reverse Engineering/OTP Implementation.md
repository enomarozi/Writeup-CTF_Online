<h1>OTP Implementation</h1>
<h3>Description</h3>
<pre>
Relevant files: <a href='https://challenge-files.picoctf.net/c_shape_facility/10cfca369f18d767122a8172313f7d55f335814cef84073eeb3d22ad6c9d721b/otp'>otp</a> <a href='https://challenge-files.picoctf.net/c_shape_facility/10cfca369f18d767122a8172313f7d55f335814cef84073eeb3d22ad6c9d721b/enc_flag.txt'>enc_flag.txt</a>
</pre>
<h3>Solution</h3>
<label>Diminta mencari key untuk xor flag_enc, Uji ltrace program</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads/OTP_Implementation]
└─# ltrace -s 1000 ./otp aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
strncpy(0x7ffd394a5160, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 100) = 0x7ffd394a5160
strncmp("fkpejodinchmbglafkpejodinchmbglafkpejodinchmbglafkpejodinchmbglafkpejodinchmbglafkpejodinchmbglafkpe", "pnbopoejdmapflhkefabijeajpcijdniefahigichdmhekgohnhdkfdjbgapnhndlcbeglloaogkokbiffbhomgpminjpgieieme", 100) = -10
puts("Invalid key!"Invalid key!
)                             = 13
+++ exited (status 1) +++
┌──(root㉿Kali)-[/home/venom/Downloads/OTP_Implementation]
└─# ltrace -s 1000 ./otp faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
strncpy(0x7ffe38222520, "faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 100) = 0x7ffe38222520
strncmp("pejodinchmbglafkpejodinchmbglafkpejodinchmbglafkpejodinchmbglafkpejodinchmbglafkpejodinchmbglafkpejo", "pnbopoejdmapflhkefabijeajpcijdniefahigichdmhekgohnhdkfdjbgapnhndlcbeglloaogkokbiffbhomgpminjpgieieme", 100) = -9
puts("Invalid key!"Invalid key!
)                             = 13
+++ exited (status 1) +++
```
<label>Di ltrace diminta untuk mencari nilai xor jika di-xor strncmp = pnbopoejdmapflhkefabijeajpcijdniefahigichdmhekgohnhdkfdjbgapnhndlcbeglloaogkokbiffbhomgpminjpgieieme atau bisa cek dengan ghidra, berikut script bruteforce per character</label>

```python3
import subprocess

hexa_ = "0123456789abcdef"
text = "pnbopoejdmapflhkefabijeajpcijdniefahigichdmhekgohnhdkfdjbgapnhndlcbeglloaogkokbiffbhomgpminjpgieieme"
j = 0
hasil = ''
for check in range(100):
    for i in hexa_:
        param = hasil+i+"a"*(99-j)
        data = subprocess.check_output(["ltrace","-s","1000","./otp",param],
                                       stderr=subprocess.STDOUT)
        true = data.split(b'strncmp("')[1].split(b'",')[0].decode()
        if text[check] == true[check]:
            hasil += i
            print(i,end='')
            j += 1
            break
```
<label>Hasilnya</label>
<pre>
f72e8f3a5c2f336958d8b8d6c393855d68db8715a6cde364c356bd734a5f75334bf91a09174226bbe063b75ce6a63b162644
</pre>
```console
┌──(root㉿Kali)-[/home/venom/Downloads/OTP_Implementation]
└─# ltrace -s 1000 ./otp f72e8f3a5c2f336958d8b8d6c393855d68db8715a6cde364c356bd734a5f75334bf91a09174226bbe063b75ce6a63b162644
strncpy(0x7fff255c05e0, "f72e8f3a5c2f336958d8b8d6c393855d68db8715a6cde364c356bd734a5f75334bf91a09174226bbe063b75ce6a63b162644", 100) = 0x7fff255c05e0
strncmp("pnbopoejdmapflhkefabijeajpcijdniefahigichdmhekgohnhdkfdjbgapnhndlcbeglloaogkokbiffbhomgpminjpgieieme", "pnbopoejdmapflhkefabijeajpcijdniefahigichdmhekgohnhdkfdjbgapnhndlcbeglloaogkokbiffbhomgpminjpgieieme", 100) = 0
puts("You got the key, congrats! Now xor it with the flag!"You got the key, congrats! Now xor it with the flag!
) = 53
+++ exited (status 0) +++
```
<label>XOR enc_flag dengan key</label>
```python3
key = bytes.fromhex('f72e8f3a5c2f336958d8b8d6c393855d68db8715a6cde364c356bd734a5f75334bf91a09174226bbe063b75ce6a63b162644')
file = bytes.fromhex(open('enc_flag.txt','r').read())
for i,j in zip(key,file):
    print(chr(i^j),end='')
```
<h3>Flag</h3>
<pre>
picoCTF{cust0m_jumbl3s_4r3nt_4_g0Od_1d3A_e34c865a}
</pre>
