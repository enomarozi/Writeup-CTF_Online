<h1><b>Sniff my girl</h1></b>
<pre>
<a href="https://ringzer0ctf.com/files/55687ffa8730190e88655ca22bb9effa.zip">File</a>
</pre>
</b><h3>Solution</h3></b>
<p>Diberikan 1 file capture wireshark, dan setelah dianalisa semua capture berupa USB keyboard</p>
<p align='center'>
  <img src="https://github.com/enomarozi/RingZer0CTF/blob/master/Steganography/Image/Sniff%20my%20girl.jpg">
</p>
<p>Select salah satu packet yang length-nya 72, copy Field-name Leafover Capture Data dan paste pada field edit name column, Lalu select seluruh packet length 72, Eksport semuanya ke file text pada 
Jendela File --> Eksport Packet Dissections --> As PlainText --> beri nama dan Save</p>

```python
keyboard = {4:"a",5:"b",6:"c",7:"d",8:"e",9:"f",10:"g",11:"h",12:"i",13:"j",
            14:"k",15:"l",16:"m",17:"n",18:"o",19:"p",20:"q",21:"r",22:"s",23:"t",
            24:"u",25:"v",26:"w",27:"x",28:"y",29:"z",30:"1",31:"2",32:"3",33:"4",
            34:"5",35:"6",36:"7",37:"8",38:"9",39:"0",40:"<Enter>",41:"<Esc>",42:"<Del>",43:"<Tab>",
            44:"<Space>",45:"-",46:"=",47:"[",48:"]",49:"\\",50:" ",51:";",52:"'",53:"`",
            54:",",55:".",56:"//"}


    
with open("USB_packet.txt") as f:
    for i in f:
        i = i.strip("\n")
        if "Leftover Capture Data" in i:
            encode = int(i.split(":")[1][5:-10],16)
            if encode != 0:
                print(keyboard[encode],end="")
```
<p>Hasil Program</p>
<pre>

```
<Del><Del><Del>www.google.ca<Space><Enter>litlle<Space><Del><Del><Del>ca<Del><Del><Del><Del><Del><Del>litle<Space>cat
<Space>iin<Space>thee<Space>world<Enter>gmail//<Del>.coom<Enter>challenge2gmaail.coom<Enter>flag-11234eteh<Enter>hhi
<Space>mom,<Enter>i<Space>lovvee<Space>yoou<Space><Del>.<Enter>bbyee<Space><Enter>
```
</pre>
<p>Dari hasil ada beberapa dublikat string, termasuk ada pada flag</p> 
</b><h3>Flag</h3></b>
<pre>
flag-1234eteh
</pre>

