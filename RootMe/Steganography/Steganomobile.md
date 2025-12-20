<h1>Steganomobile</h1>
<h3>Description</h3>
<label>After extraction of mobile data, the searcher, investigator have got this sequence of numbers. Maybe a phone number ?</label>
<h3>Solution</h3>
<label>Key handphone lama</label>

```python3
char_ = {0:' 0',1:'.,?!1',2:'abc2',3:'def3',4:'ghi4',5:'jkl5',6:'mno6',7:'pqrs7',8:'tuv8',9:'wxyz9'}
key_phone = '222-33-555-555-7-44-666-66-33'.split('-')
for i in key_phone:
    len_key = len(i)-1
    key = int(i[0])
    print(char_[key][len_key],end='')

```
<h3>Flag</h3>
<pre>
cellphone
</pre>
