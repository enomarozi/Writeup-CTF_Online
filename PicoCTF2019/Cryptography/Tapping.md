<h1>Tapping</h1>
<h3>Description</h3>
<pre>
Theres tapping coming in from the wires.
What's it saying nc fickle-tempest.picoctf.net 63197.
</pre>
<h3>Solution</h3>

```python3
from string import ascii_uppercase as letter
from string import digits as digits

morse = '.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ----- ....- ...-- .- ...-- ....- ..... ----- }'.split(' ')
_az = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split(' ')
_09 = '----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.'.split(' ')
for i in morse:
    if i in _az:
        print(letter[_az.index(i)],end='')
    elif i in _09:
        print(digits[_09.index(i)],end='')
    else:
        print(i,end='')
```
<h3>Flag</h3>
<pre>
PICOCTF{M0RS3C0D31SFUN043A3450}
</pre>
