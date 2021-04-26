<h1><b>Apa itu Hacker</b></h1>
<pre>
saat ini, Penggunaan utama "peretAs" Sebagian besar mengacu pada penjahat komputer, karena penggunaan media massa dari kata tersebut sejak 1990-an.[2] ini Termasuk apa yang disebut pEretas gaul "script kiddies", orang-orang yang membobol komputer menggunakan program yang ditulis oleh orang lain, dengan sedikit pengetahuan tentang cara mereka bekerja. penggunaan ini telah menjadi begitu dominan sehingga masyarakat umum sebagian besar tidak menyadari bahwa ada makna yang berbeda.[3] sementara penunjukan diri para penghobi seBagai peretas pada umumnya diakui dan dIterima oleh peretas keamanaN komputer, orang-orang dari subkultur pemrograman menganggap penggunaan komputer terkait intrusi tidak benar, dan menekankan perbedaan antara keduanya dengan menyebut pembobol keamanan "Cracker" (analOg dengan safecracker). Maupun hacker atau cracker, mereka sangat menyukai teks qeJdZ4wM.
</pre>
<h3><b>Solution</b></h3>
<p>Diberikan sebuah text, kita diminta untuk mengambil setiap uppercase dari text, berikut programnya</p>

```python3
import requests

text = """saat ini, Penggunaan utama "peretAs" Sebagian besar mengacu pada penjahat komputer, karena penggunaan media massa dari kata tersebut sejak 1990-an.[2] ini Termasuk apa yang disebut pEretas gaul "script kiddies", orang-orang yang membobol komputer menggunakan program yang ditulis oleh orang lain, dengan sedikit pengetahuan tentang cara mereka bekerja. penggunaan ini telah menjadi begitu dominan sehingga masyarakat umum sebagian besar tidak menyadari bahwa ada makna yang berbeda.[3] sementara penunjukan diri para penghobi seBagai peretas pada umumnya diakui dan dIterima oleh peretas keamanaN komputer, orang-orang dari subkultur pemrograman menganggap penggunaan komputer terkait intrusi tidak benar, dan menekankan perbedaan antara keduanya dengan menyebut pembobol keamanan "Cracker" (analOg dengan safecracker). Maupun hacker atau cracker, mereka sangat menyukai teks qeJdZ4wM.""".split('teks')
hasil = ""
for i in text[0]:
    if i.isupper():
        hasil += i.lower()
        if hasil[-1] == "n":
            hasil += "."

hasil += "/raw/"+text[1][1:-1]
res = requests.get("https://"+hasil).text
print(res) #CTFR{f0cu5_1f_y0u_w4nt_w1n}
```
<h3><b>Flag</b></h3>
<pre>
CTFR{f0cu5_1f_y0u_w4nt_w1n}
</pre>
