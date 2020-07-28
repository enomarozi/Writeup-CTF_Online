<h1><b>HailCaesar!</h1></b>
<pre>
You might need to write some Python to solve this challenge. 
Some encryption may be involved. Good Luck!

<a href='https://ctflearn.com/challenge/download/952'>HailCaesar.jpg</a> 
</pre>
</b><h3>Solution</h3></b>
<p>Eksekusi exiftool dan grep pada file</p>

```console
root@Python:/home/venom/Downloads# exiftool HailCaesar.jpg -a | grep -i comment
Comment                         : CTFlearn{Hail_Caesar!!!}.CTFlearn{Airplanes_Sometimes_Cause_Inflight_Incidents}.CTFlearn{Flight_32_Leaves_soon_from_gate_126}..
Comment                         : /<V5;)j}j6\<Y)8><\9Fbu,Hy4ONC}pxP"4st12wn`?@O$6BgQo7i#gtD|s>3lf=
Comment                         : SWYgeW91IGFyZSBoYXZpbmcgdHJvdWJsZSBzb2x2aW5nIHRoaXMgY2hhbGxlbmdlLCBwbGVhc2Ug.c29sdmUgbXkgb3RoZXIKY2hhbGxlbmdlcyBmaXJzdDoKUnViYmVyRHVjawpTbm93Ym9hcmQKUGlr.ZXNQZWFrCkdhbmRhbGZUaGVXaXNlCgpUaGUgY2hhbGxlbmdlcyBhcmUgZGVzaWduZWQgdG8gYmUg.aW5jcmVhc2luZyBpbiBkaWZmaWN1bHR5IGFuZCB0aGlzIEhhaWxDYWVzYXIgY2hhbGxlbmdlIGlz.IHRoZSBuZXh0CmNoYWxsZW5nZSBpbiB0aGUgc2VyaWVzLgoKTXkgVHdpdHRlciBETSBpcyBvcGVu.IEBrY2Jvd2h1bnRlciBidXQgcGxlYXNlIG9ubHkgcGluZyBtZSBpZiB5b3UgaGF2ZSBzb2x2ZWQg.dGhlIGFib3ZlIGNoYWxsZW5nZXMgZmlyc3QuCgpJZiB5b3UgYXJlIG5ldyB0byB0aGUganBlZyBm.aWxlIGZvcm1hdCBwbGVhc2UgcmVhZCB0aGlzOgpodHRwczovL2Rldi5leGl2Mi5vcmcvcHJvamVj.dHMvZXhpdjIvd2lraS9UaGVfTWV0YWRhdGFfaW5fSlBFR19maWxlcwoKSWYgeW91IGFyZSBuZXcg.dG8gaGFja2luZyBhbmQgYXJlIHN0aWxsIGxlYXJuaW5nIGFib3V0IGJpdHMgYW5kIGJ5dGVzIHBs.ZWFzZSB3YXRjaCB0aGlzIHZpZGVvOgpodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PXRM.ZHZFT2FtM3NrCgp4b3JwZCBoYXMgYSBsb3Qgb2YgZnJlZSB2aWRlb3MgdGhhdCB0ZWFjaCBpbXBv.cnRhbnQgY29tcHV0ZXIgc2NpZW5jZSAvIGhhY2tpbmcgY29uY2VwdHMuCgpOb3RlIHRoYXQgb2Z0.ZW4gbXkgY2hhbGxlbmdlcyBjb21iaW5lIGZvcmVuc2ljcyBhbmQgc29tZSBhc3BlY3Qgb2YgY3J5.cHRvZ3JhcGh5LgoKSGF2ZSBmdW4hCmtjYm93aHVudGVyCgoK.
Comment                         : 2m{y!"%w2'z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0.
```
<p>Disana terdapat flag palsu yang merupakan clue, dan 2 text encrypt ascii dan 1 text encode base64</p>
<p>Clue lain terdapat pada encode base64</p>

```console
root@Python:/home/venom/Downloads# echo 'SWYgeW91IGFyZSBoYXZpbmcgdHJvdWJsZSBzb2x2aW5nIHRoaXMgY2hhbGxlbmdlLCBwbGVhc2Ugc29sdmUgbXkgb3RoZXIKY2hhbGxlbmdlcyBmaXJzdDoKUnViYmVyRHVjawpTbm93Ym9hcmQKUGlrZXNQZWFrCkdhbmRhbGZUaGVXaXNlCgpUaGUgY2hhbGxlbmdlcyBhcmUgZGVzaWduZWQgdG8gYmUgaW5jcmVhc2luZyBpbiBkaWZmaWN1bHR5IGFuZCB0aGlzIEhhaWxDYWVzYXIgY2hhbGxlbmdlIGlzIHRoZSBuZXh0CmNoYWxsZW5nZSBpbiB0aGUgc2VyaWVzLgoKTXkgVHdpdHRlciBETSBpcyBvcGVuIEBrY2Jvd2h1bnRlciBidXQgcGxlYXNlIG9ubHkgcGluZyBtZSBpZiB5b3UgaGF2ZSBzb2x2ZWQgdGhlIGFib3ZlIGNoYWxsZW5nZXMgZmlyc3QuCgpJZiB5b3UgYXJlIG5ldyB0byB0aGUganBlZyBmaWxlIGZvcm1hdCBwbGVhc2UgcmVhZCB0aGlzOgpodHRwczovL2Rldi5leGl2Mi5vcmcvcHJvamVjdHMvZXhpdjIvd2lraS9UaGVfTWV0YWRhdGFfaW5fSlBFR19maWxlcwoKSWYgeW91IGFyZSBuZXcgdG8gaGFja2luZyBhbmQgYXJlIHN0aWxsIGxlYXJuaW5nIGFib3V0IGJpdHMgYW5kIGJ5dGVzIHBsZWFzZSB3YXRjaCB0aGlzIHZpZGVvOgpodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PXRMZHZFT2FtM3NrCgp4b3JwZCBoYXMgYSBsb3Qgb2YgZnJlZSB2aWRlb3MgdGhhdCB0ZWFjaCBpbXBvcnRhbnQgY29tcHV0ZXIgc2NpZW5jZSAvIGhhY2tpbmcgY29uY2VwdHMuCgpOb3RlIHRoYXQgb2Z0ZW4gbXkgY2hhbGxlbmdlcyBjb21iaW5lIGZvcmVuc2ljcyBhbmQgc29tZSBhc3BlY3Qgb2YgY3J5cHRvZ3JhcGh5LgoKSGF2ZSBmdW4hCmtjYm93aHVudGVyCgoK. ' | base64 -d
If you are having trouble solving this challenge, please solve my other
challenges first:
RubberDuck
Snowboard
PikesPeak
GandalfTheWise

The challenges are designed to be increasing in difficulty and this HailCaesar challenge is the next
challenge in the series.

My Twitter DM is open @kcbowhunter but please only ping me if you have solved the above challenges first.

If you are new to the jpeg file format please read this:
https://dev.exiv2.org/projects/exiv2/wiki/The_Metadata_in_JPEG_files

If you are new to hacking and are still learning about bits and bytes please watch this video:
https://www.youtube.com/watch?v=tLdvEOam3sk

xorpd has a lot of free videos that teach important computer science / hacking concepts.

Note that often my challenges combine forensics and some aspect of cryptography.

Have fun!
kcbowhunter


root@Python:/home/venom/Downloads# 
```
<p>Sepertinya clue yang jelas terdapat pada flag palsu diatas, yaitu 32 dan 126 itu merupakan ascii yang memuat text readable</p>
<p>Disini kita akan melakukan bruteforce string ascii 32(space) s/d 126(~) dari encrypt text </p>

```python
def brute(n):
    text = '''2m{y!"%w2'z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0'''
    flag = ''
    for i in text:
        ascii_str = ord(i)+n
        if ascii_str > 126:
            flag += chr((ascii_str%127)+32)
        elif ascii_str < 33:
            flag += chr(ascii_str+33)
        else:
            flag += chr(ascii_str)
    if "CTFlearn" in flag:
        print(n,flag)
for j in range(200):
    brute(j)

```
<p>Output Program</p>
<pre>
77  [ignore this] CTFlearn{Maximus.Decimus.Meridius}
</pre>

</b><h3>Flag</h3></b>
<pre>
CTFlearn{Maximus.Decimus.Meridius}
</pre>
