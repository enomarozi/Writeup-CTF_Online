<h1>PDF - Embedded</h1>
<h3>Description</h3>
<label>Find the hidden information in this PDF file.</label>
<h3>Solution</h3>
<label>Analisa file pdf</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# strings -a epreuve_BAC_2004.pdf
....................
....................
endstream
endobj
78 0 obj
<< /F (Hidden_b33rs.txt)
/Type /Filespec
/EF << /F 77 0 R >> >>
endobj
xref
0 79
....................
....................

┌──(root㉿Kali)-[/home/venom/Downloads]
└─# binwalk -e epreuve_BAC_2004.pdf --run-as=root

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
73            0x49            Zlib compressed data, default compression
261           0x105           Zlib compressed data, default compression
451           0x1C3           Zlib compressed data, default compression
641           0x281           Zlib compressed data, default compression
831           0x33F           Zlib compressed data, default compression
1021          0x3FD           Zlib compressed data, default compression
1211          0x4BB           Zlib compressed data, default compression
1401          0x579           Zlib compressed data, default compression
1591          0x637           Zlib compressed data, default compression
1781          0x6F5           Zlib compressed data, default compression
1971          0x7B3           Zlib compressed data, default compression
2161          0x871           Zlib compressed data, default compression
5021          0x139D          Zlib compressed data, default compression
260496        0x3F990         Zlib compressed data, default compression
540256        0x83E60         Zlib compressed data, default compression
683550        0xA6E1E         Zlib compressed data, default compression
899938        0xDBB62         Zlib compressed data, default compression
1095225       0x10B639        Zlib compressed data, default compression
1205948       0x1266BC        Zlib compressed data, default compression
1334697       0x145DA9        Zlib compressed data, default compression
1528474       0x17529A        Zlib compressed data, default compression
1651840       0x193480        Zlib compressed data, default compression
1923915       0x1D5B4B        Zlib compressed data, default compression
2167502       0x2112CE        Zlib compressed data, default compression
2306578       0x233212        Zlib compressed data, default compression

WARNING: One or more files failed to extract: either no utility was found or it's unimplemented
                                   
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# cd _epreuve_BAC_2004.pdf.extracted 
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads/_epreuve_BAC_2004.pdf.extracted]
└─# file *                            
1C3:         ASCII text
1C3.zlib:    zlib compressed data
1D5B4B:      data
1D5B4B.zlib: zlib compressed data
3F990:       data
3F990.zlib:  zlib compressed data
3FD:         ASCII text
3FD.zlib:    zlib compressed data
4BB:         ASCII text
4BB.zlib:    zlib compressed data
6F5:         ASCII text
6F5.zlib:    zlib compressed data
7B3:         ASCII text
7B3.zlib:    zlib compressed data
10B639:      data
10B639.zlib: zlib compressed data
33F:         ASCII text
33F.zlib:    zlib compressed data
49:          ASCII text
49.zlib:     zlib compressed data
83E60:       data
83E60.zlib:  zlib compressed data
105:         ASCII text
105.zlib:    zlib compressed data
139D:        data
139D.zlib:   zlib compressed data
145DA9:      data
145DA9.zlib: zlib compressed data
281:         ASCII text
281.zlib:    zlib compressed data
579:         ASCII text
579.zlib:    zlib compressed data
637:         ASCII text
637.zlib:    zlib compressed data
871:         ASCII text
871.zlib:    zlib compressed data
1266BC:      data
1266BC.zlib: zlib compressed data
2112CE:      data
2112CE.zlib: zlib compressed data
17529A:      data
17529A.zlib: zlib compressed data
193480:      data
193480.zlib: zlib compressed data
233212:      ASCII text
233212.zlib: zlib compressed data
A6E1E:       data
A6E1E.zlib:  zlib compressed data
DBB62:       data
DBB62.zlib:  zlib compressed data
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads/_epreuve_BAC_2004.pdf.extracted]
└─# cat 233212 | base64 -d | head -n 2
����JFIF``��<CREATOR: gd-jpeg v1.0 (using IJG JPEG v62), quality = 95
��C
        	
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads/_epreuve_BAC_2004.pdf.extracted]
└─# cat 233212 | base64 -d > image.jpg

```
<h3>Flag</h3>
<pre>
Hidden_embedded_Fil3
</pre>
