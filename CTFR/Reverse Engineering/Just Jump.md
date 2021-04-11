<h1><b>Just Jump</b></h1>
<pre>
Arti dari Title diatas "Hanya Lompat" Mksdnya apaan yaa ? Coba deh di cari sendiri maksudnya dan coba Selesaikan selesaikan challenge dibawah ini.

Challenge --> <a href='https://mega.nz/#!UtQCUBZS!CUccRHYu_lpWsfs0aLLqql0eNsd0n1Hv_cSP5wl2ezA'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p align='justify'>Decompile file dengan tool ghidra dan lihat pada fungsi flag() disana terdapat string acak <b>?PBNwsdu[j//`[`/_,il-h/n[sd/j[u,q[_0j[fqily</b>
yang melakukan operasi penambahan +4 untuk mendapatkan flag</p>

```python3
enc_flag = "?PBNwsdu[j//`[`/_,il-h/n[sd/j[u,q[_0j[fqily"
for i in enc_flag:
    print(chr(ord(i)+4),end='')#CTFR{why_n33d_d3c0mp1l3r_wh3n_y0u_c4n_jump}
```
<h3><b>Flag</b></h3>
<pre>
CTFR{why_n33d_d3c0mp1l3r_wh3n_y0u_c4n_jump}
</pre>
