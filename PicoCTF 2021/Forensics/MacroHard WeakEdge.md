<h1>MacroHard WeakEdge</h1>
<h3>Description</h3>
<pre>
I've hidden a flag in this file. Can you find it?
<a href='https://challenge-files.picoctf.net/c_wily_courier/d78815176c19ddc85a1388233268d2f4c459fcbbaab197b4a29ebafc88294c54/Forensics_is_fun.pptm'>Forensics_is_fun.pptm</a>
</pre>
<h3>Solution</h3>
<label>pptm merupakan ppt macro, check file macro di .pptm</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# olevba Forensics_is_fun.pptm 
olevba 0.60.2 on Python 3.13.11 - http://decalage.info/python/oletools
===============================================================================
FILE: Forensics_is_fun.pptm
Type: OpenXML
WARNING  For now, VBA stomping cannot be detected for files in memory
-------------------------------------------------------------------------------
VBA MACRO Module1.bas 
in file: ppt/vbaProject.bin - OLE stream: 'VBA/Module1'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Sub not_flag()
    Dim not_flag As String
    not_flag = "sorry_but_this_isn't_it"
End Sub
No suspicious keyword or IOC found.
```
<label>Didapatkan "sorry_but_this_isn't_it", lanjut coba extract file pptm</label>
```console
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# unzip Forensics_is_fun.pptm -d isi_pptm
Archive:  Forensics_is_fun.pptm
  inflating: isi_pptm/[Content_Types].xml  
  inflating: isi_pptm/_rels/.rels    
  inflating: isi_pptm/ppt/presentation.xml  
  inflating: isi_pptm/ppt/slides/_rels/slide46.xml.rels  
  inflating: isi_pptm/ppt/slides/slide1.xml  
  inflating: isi_pptm/ppt/slides/slide2.xml  
  inflating: isi_pptm/ppt/slides/slide3.xml  
  inflating: isi_pptm/ppt/slides/slide4.xml  
  inflating: isi_pptm/ppt/slides/slide5.xml  
  inflating: isi_pptm/ppt/slides/slide6.xml  
  inflating: isi_pptm/ppt/slides/slide7.xml  
  inflating: isi_pptm/ppt/slides/slide8.xml  
  inflating: isi_pptm/ppt/slides/slide9.xml  
  inflating: isi_pptm/ppt/slides/slide10.xml  
  inflating: isi_pptm/ppt/slides/slide11.xml  
  inflating: isi_pptm/ppt/slides/slide12.xml  
  inflating: isi_pptm/ppt/slides/slide13.xml  
  inflating: isi_pptm/ppt/slides/slide14.xml  
  inflating: isi_pptm/ppt/slides/slide15.xml  
  inflating: isi_pptm/ppt/slides/slide16.xml  
  inflating: isi_pptm/ppt/slides/slide17.xml  
  inflating: isi_pptm/ppt/slides/slide18.xml  
  inflating: isi_pptm/ppt/slides/slide19.xml  
  inflating: isi_pptm/ppt/slides/slide20.xml  
  inflating: isi_pptm/ppt/slides/slide21.xml  
  inflating: isi_pptm/ppt/slides/slide22.xml  
  inflating: isi_pptm/ppt/slides/slide23.xml  
  inflating: isi_pptm/ppt/slides/slide24.xml  
  inflating: isi_pptm/ppt/slides/slide25.xml  
  inflating: isi_pptm/ppt/slides/slide26.xml  
  inflating: isi_pptm/ppt/slides/slide27.xml  
  inflating: isi_pptm/ppt/slides/slide28.xml  
  inflating: isi_pptm/ppt/slides/slide29.xml  
  inflating: isi_pptm/ppt/slides/slide30.xml  
  inflating: isi_pptm/ppt/slides/slide31.xml  
  inflating: isi_pptm/ppt/slides/slide32.xml  
  inflating: isi_pptm/ppt/slides/slide33.xml  
  inflating: isi_pptm/ppt/slides/slide34.xml  
  inflating: isi_pptm/ppt/slides/slide35.xml  
  inflating: isi_pptm/ppt/slides/slide36.xml  
  inflating: isi_pptm/ppt/slides/slide37.xml  
  inflating: isi_pptm/ppt/slides/slide38.xml  
  inflating: isi_pptm/ppt/slides/slide39.xml  
  inflating: isi_pptm/ppt/slides/slide40.xml  
  inflating: isi_pptm/ppt/slides/slide41.xml  
  inflating: isi_pptm/ppt/slides/slide42.xml  
  inflating: isi_pptm/ppt/slides/slide43.xml  
  inflating: isi_pptm/ppt/slides/slide44.xml  
  inflating: isi_pptm/ppt/slides/slide45.xml  
  inflating: isi_pptm/ppt/slides/slide46.xml  
  inflating: isi_pptm/ppt/slides/slide47.xml  
  inflating: isi_pptm/ppt/slides/slide48.xml  
  inflating: isi_pptm/ppt/slides/slide49.xml  
  inflating: isi_pptm/ppt/slides/slide50.xml  
  inflating: isi_pptm/ppt/slides/slide51.xml  
  inflating: isi_pptm/ppt/slides/slide52.xml  
  inflating: isi_pptm/ppt/slides/slide53.xml  
  inflating: isi_pptm/ppt/slides/slide54.xml  
  inflating: isi_pptm/ppt/slides/slide55.xml  
  inflating: isi_pptm/ppt/slides/slide56.xml  
  inflating: isi_pptm/ppt/slides/slide57.xml  
  inflating: isi_pptm/ppt/slides/slide58.xml  
  inflating: isi_pptm/ppt/slides/_rels/slide47.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide48.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide49.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide50.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide32.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide52.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide53.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide54.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide55.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide56.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide57.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide58.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide51.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide13.xml.rels  
  inflating: isi_pptm/ppt/_rels/presentation.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide1.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide2.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide3.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide4.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide5.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide6.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide7.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide8.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide9.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide10.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide11.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide12.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide14.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide15.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide16.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide17.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide18.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide19.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide20.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide21.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide22.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide23.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide24.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide25.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide26.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide27.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide28.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide29.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide30.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide31.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide33.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide34.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide35.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide36.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide37.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide38.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide39.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide40.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide41.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide42.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide43.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide44.xml.rels  
  inflating: isi_pptm/ppt/slides/_rels/slide45.xml.rels  
  inflating: isi_pptm/ppt/slideMasters/slideMaster1.xml  
  inflating: isi_pptm/ppt/slideLayouts/slideLayout1.xml  
  inflating: isi_pptm/ppt/slideLayouts/slideLayout2.xml  
  inflating: isi_pptm/ppt/slideLayouts/slideLayout3.xml  
  inflating: isi_pptm/ppt/slideLayouts/slideLayout4.xml  
  inflating: isi_pptm/ppt/slideLayouts/slideLayout5.xml  
  inflating: isi_pptm/ppt/slideLayouts/slideLayout6.xml  
  inflating: isi_pptm/ppt/slideLayouts/slideLayout7.xml  
  inflating: isi_pptm/ppt/slideLayouts/slideLayout8.xml  
  inflating: isi_pptm/ppt/slideLayouts/slideLayout9.xml  
  inflating: isi_pptm/ppt/slideLayouts/slideLayout10.xml  
  inflating: isi_pptm/ppt/slideLayouts/slideLayout11.xml  
  inflating: isi_pptm/ppt/slideMasters/_rels/slideMaster1.xml.rels  
  inflating: isi_pptm/ppt/slideLayouts/_rels/slideLayout1.xml.rels  
  inflating: isi_pptm/ppt/slideLayouts/_rels/slideLayout2.xml.rels  
  inflating: isi_pptm/ppt/slideLayouts/_rels/slideLayout3.xml.rels  
  inflating: isi_pptm/ppt/slideLayouts/_rels/slideLayout4.xml.rels  
  inflating: isi_pptm/ppt/slideLayouts/_rels/slideLayout5.xml.rels  
  inflating: isi_pptm/ppt/slideLayouts/_rels/slideLayout6.xml.rels  
  inflating: isi_pptm/ppt/slideLayouts/_rels/slideLayout7.xml.rels  
  inflating: isi_pptm/ppt/slideLayouts/_rels/slideLayout8.xml.rels  
  inflating: isi_pptm/ppt/slideLayouts/_rels/slideLayout9.xml.rels  
  inflating: isi_pptm/ppt/slideLayouts/_rels/slideLayout10.xml.rels  
  inflating: isi_pptm/ppt/slideLayouts/_rels/slideLayout11.xml.rels  
  inflating: isi_pptm/ppt/theme/theme1.xml  
 extracting: isi_pptm/docProps/thumbnail.jpeg  
  inflating: isi_pptm/ppt/vbaProject.bin  
  inflating: isi_pptm/ppt/presProps.xml  
  inflating: isi_pptm/ppt/viewProps.xml  
  inflating: isi_pptm/ppt/tableStyles.xml  
  inflating: isi_pptm/docProps/core.xml  
  inflating: isi_pptm/docProps/app.xml  
  inflating: isi_pptm/ppt/slideMasters/hidden  
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# cd isi_pptm                            
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads/isi_pptm]
└─# ls -iR | grep -Ev '\.'                 
1184071 docProps
1183916 ppt
1183914 _rels


1183994 _rels
1184043 slideLayouts
1184041 slideMasters
1183918 slides
1184069 theme


1184057 _rels


1184080 hidden
1184055 _rels


1183919 _rels



                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads/isi_pptm]
└─# ls -iR | grep -Ev '\.' -B 2
.:
1183906 [Content_Types].xml
1184071 docProps
1183916 ppt
1183914 _rels

--
1184077 core.xml
1184072 thumbnail.jpeg

--
1183917 presentation.xml
1184074 presProps.xml
1183994 _rels
1184043 slideLayouts
1184041 slideMasters
1183918 slides
1184076 tableStyles.xml
1184069 theme
1184073 vbaProject.bin
1184075 viewProps.xml

./ppt/_rels:
1183995 presentation.xml.rels

./ppt/slideLayouts:
1184057 _rels
--
1184051 slideLayout8.xml
1184052 slideLayout9.xml

--
1184065 slideLayout8.xml.rels
1184066 slideLayout9.xml.rels

./ppt/slideMasters:
1184080 hidden
1184055 _rels
1184042 slideMaster1.xml

./ppt/slideMasters/_rels:
1184056 slideMaster1.xml.rels

./ppt/slides:
1183919 _rels
--
1183928 slide8.xml
1183929 slide9.xml

--
1184004 slide8.xml.rels
1184005 slide9.xml.rels

./ppt/theme:
1184070 theme1.xml

                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads/isi_pptm]
└─# cat ppt/slideMasters/hidden 
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads/isi_pptm]
└─# cd ppt/slideMasters 
                                                                                
┌──(root㉿Kali)-[/home/…/Downloads/isi_pptm/ppt/slideMasters]
└─# cat hidden | tr -d ' ' | sed 's/$/==/' | base64 -d
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5} 
```
<h3>Flag</h3>
<pre>
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5} 
</pre>
