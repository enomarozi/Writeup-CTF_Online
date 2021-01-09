<h1><b>Bahasa Bayi</b></h1>
<pre>
Bahasa Bayi kira kria nya seperti ini kan ababaabababab, Nah jika sudah tau coba translate Bahasa Bayi yang satu ini

Flag : aaaba baabb aabab baaab aaaab babaa ababa aaaaa abbab aaaab aaaaa aabbb aaaaa baaba aaaaa aaaab aaaaa bbaaa abaaa
</pre>
<h3><b>Solution</b></h3>
<p>Merupakan encryption baconian, Decrypt pada website <a href='http://rumkin.com/tools/cipher/baconian.php'>Baconian Cipher</a>, atau dengan script dibawah</p>

```python
baconianDistric = {"A":"AAAAA","B":"AAAAB","C":"AAABA","D":"AAABB","E":"AABAA","F":"AABAB"
                   ,"G":"AABBA","H":"AABBB","I":"ABAAA","J":"ABAAB","K":"ABABA","L":"ABABB"
                   ,"M":"ABBAA","N":"ABBAB","O":"ABBBA","P":"ABBBB","Q":"BAAAA","R":"BAAAB"
                   ,"S":"BAABA","T":"BAABB","U":"BABAA","V":"BABAB","W":"BABBA","X":"BABBB"
                   ,"Y":"BBAAA","Z":"BBAAB"}

text = "aaaba baabb aabab baaab aaaab babaa ababa aaaaa abbab aaaab aaaaa aabbb aaaaa baaba aaaaa aaaab aaaaa bbaaa abaaa".upper().split(' ')
result_allDistric = ""
for i in text:
    for j in baconianDistric.keys():
        if i == baconianDistric[j]:
            result_allDistric += j
print("baconDistric --> "+result_allDistric)

```
<p>Output Program</p>
<pre>
baconDistric --> CTFRBUKANBAHASABAYI
</pre>
<h3><b>Flag</b></h3>
<pre>
CTFR{bukanbahasabayi}
</pre>
