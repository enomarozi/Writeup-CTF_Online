<h1><b>Tututututut</b></h1>
<pre>
Ini ada file musik, tapi bener bener gak bisa dipahamin suaranya. Bisa bantu dibacain kagakk

Challenge --> <a href='https://mega.nz/#!8poxmCoD!-0R7_PdgIvUcAgmpQGFARNjrsEINZvWoie9OH8LzpMs'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Diberikan sebuah file audio ekstensi WAV, lihat wavelength dari masing-masing amplitudo dengan tool audacity atau dengan jalankan script dibawah</p>

```python
import librosa.display
import matplotlib.pyplot as plt

audio_data = 'tutut.wav'
x, sr = librosa.load(audio_data)
plt.figure(figsize=(14, 5))
librosa.display.waveplot(x, sr=sr)
plt.show()
```
<p>Output Program</p>
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFR/Image/audio_analys.png'>
</p>
<p align='justify'>Dari ciri wavelength dan amplitude berupa bentuk encode morse code</p>
<pre>
-.-. ----- -. --. .-. ....- - ... -.-- ----- ..- ..-. .---- -. -.. -- ...--
</pre>
<p>Decode morse tersebut pada URL <a href='https://morsedecoder.com/'>Morse_Decode</a>, atau dengan scipt dibawah</p>

```python3
morse ={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.",
        "H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.",
        "O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-",
        "V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","1":".----",
        "2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...",
        "8":"---..","9":"----.","0":"-----","(":"-.--.",")":"-.--.-"}

encode = '-.-. ----- -. --. .-. ....- - ... -.-- ----- ..- ..-. .---- -. -.. -- ...--'.split(' ')
for i in encode:
    for k,j in morse.items():
        if i == j:
            print(k,end='')#C0NGR4TSY0UF1NDM3
```
<h3><b>Flag</b></h3>
<pre>
CTFR{C0NGR4TSY0UF1NDM3}
</pre>
