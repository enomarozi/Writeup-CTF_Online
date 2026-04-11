<h1>Weird File</h1>
<h3>Description</h3>
<pre>
What could go wrong if we let Word documents run programs? (aka "in-the-clear").
<a href='https://challenge-files.picoctf.net/c_wily_courier/b5eb3574e45fb177ab55cdfa3cf81c79bfc87319bb87bec1cffe5fdd17b8fca9/weird.docm'>weird.docm</a>
</pre>
<h3>Solution</h3>
<label>File docm biasanya berisi macro di filenya, check dengan olevba</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# olevba weird.docm
olevba 0.60.2 on Python 3.13.12 - http://decalage.info/python/oletools
===============================================================================
FILE: weird.docm
Type: OpenXML
WARNING  For now, VBA stomping cannot be detected for files in memory
-------------------------------------------------------------------------------
VBA MACRO ThisDocument.cls 
in file: word/vbaProject.bin - OLE stream: 'VBA/ThisDocument'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Sub AutoOpen()
    MsgBox "Macros can run any program", 0, "Title"
    Signature

End Sub
 
 Sub Signature()
    Selection.TypeText Text:="some text"
    Selection.TypeParagraph
    
 End Sub
 
 Sub runpython()

Dim Ret_Val
Args = """" '"""
Ret_Val = Shell("python -c 'print(\"cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9\")'" & " " & Args, vbNormalFocus)
If Ret_Val = 0 Then
   MsgBox "Couldn't run python script!", vbOKOnly
End If
End Sub
+----------+--------------------+---------------------------------------------+
|Type      |Keyword             |Description                                  |
+----------+--------------------+---------------------------------------------+
|AutoExec  |AutoOpen            |Runs when the Word document is opened        |
|Suspicious|Shell               |May run an executable file or a system       |
|          |                    |command                                      |
|Suspicious|vbNormalFocus       |May run an executable file or a system       |
|          |                    |command                                      |
|Suspicious|run                 |May run an executable file or a system       |
|          |                    |command                                      |
+----------+--------------------+---------------------------------------------+

                                                                                                                                            
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# echo "cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9" | base64 -d
picoCTF{m4cr0s_r_d4ng3r0us}     
```
<h3>Flag</h3>
<pre>
picoCTF{m4cr0s_r_d4ng3r0us}    
</pre>
