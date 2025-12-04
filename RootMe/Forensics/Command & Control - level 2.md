<h1>Command & Control - level 2</h1>
<h3>Description</h3>
<label>Congratulations Berthier, thanks to your help the computer has been identified. You have requested a memory dump but before starting your analysis you wanted to take a look at the antivirus’ logs. Unfortunately, you forgot to write down the workstation’s hostname. But since you have its memory dump you should be able to get it back!

The validation flag is the workstation’s hostname.

The uncompressed memory dump md5 hash is e3a902d4d44e0f7bd9cb29865e0a15de</label>
<a href='https://static.root-me.org/forensic/ch2/ch2.tbz2'>File</a>
<h3>Solution</h3>
<label>Memory dump Windows 7</label>

```console
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# vol -f ch2.dmp windows.info                         

Volatility 3 Framework 2.27.0
Progress:  100.00		PDB scanning finished                        
Variable	Value

Kernel Base	0x82801000
DTB	0x185000
Symbols	file:///root/volatility3/volatility3/symbols/windows/ntkrpamp.pdb/5B308B4ED6464159B87117C711E7340C-2.json.xz
Is64Bit	False
IsPAE	True
layer_name	0 WindowsIntelPAE
memory_layer	1 FileLayer
KdDebuggerDataBlock	0x82929be8
NTBuildLab	7600.16385.x86fre.win7_rtm.09071
CSDVersion	0
KdVersionBlock	0x82929bc0
Major/Minor	15.7600
MachineType	332
KeNumberProcessors	1
SystemTime	2013-01-12 16:59:18+00:00
NtSystemRoot	C:\Windows
NtProductType	NtProductWinNt
NtMajorVersion	6
NtMinorVersion	1
PE MajorOperatingSystemVersion	6
PE MinorOperatingSystemVersion	1
PE Machine	332
PE TimeDateStamp	Mon Jul 13 23:15:19 2009

```
<label>Hostname check di environment variable</label>

```console
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# vol -f ch2.dmp windows.envars | grep -i 'USERDOMAIN'        

692gresssvchost.exe	0x2c0ff0PDB scanUSERDOMAIN	WORKGROUP
764	svchost.exe	0x2b1070	USERDOMAIN	WORKGROUP
832	svchost.exe	0x301068	USERDOMAIN	NT AUTHORITY
904	svchost.exe	0x140ff0	USERDOMAIN	WORKGROUP
928	svchost.exe	0x5c0ff0	USERDOMAIN	WORKGROUP
1084	svchost.exe	0x131068	USERDOMAIN	NT AUTHORITY
1172	svchost.exe	0xb1070	USERDOMAIN	WORKGROUP
1220	AvastSvc.exe	0x520ff0	USERDOMAIN	WORKGROUP
1712	spoolsv.exe	0x670ff0	USERDOMAIN	WORKGROUP
1748	svchost.exe	0x171068	USERDOMAIN	NT AUTHORITY
1968	vmtoolsd.exe	0x220ff0	USERDOMAIN	WORKGROUP
1612	TPAutoConnSvc.	0x2f0ff0	USERDOMAIN	WORKGROUP
2352	taskhost.exe	0x341038	USERDOMAIN	WIN-ETSA91RKCFP
2496	dwm.exe	0x171038	USERDOMAIN	WIN-ETSA91RKCFP
2548	explorer.exe	0x2e1060	USERDOMAIN	WIN-ETSA91RKCFP
2568	TPAutoConnect.	0x670ff0	USERDOMAIN	WORKGROUP
2660	VMwareTray.exe	0x2610b0	USERDOMAIN	WIN-ETSA91RKCFP
2676	VMwareUser.exe	0x2f10c0	USERDOMAIN	WIN-ETSA91RKCFP
2720	AvastUI.exe	0x2710c0	USERDOMAIN	WIN-ETSA91RKCFP
2744	StikyNot.exe	0x331070	USERDOMAIN	WIN-ETSA91RKCFP
2772	iexplore.exe	0x2c10b8	USERDOMAIN	WIN-ETSA91RKCFP
2900	SearchIndexer.	0x280ff0	USERDOMAIN	WORKGROUP
3352	svchost.exe	0x5f1068	USERDOMAIN	NT AUTHORITY
3564	soffice.bin	0xc91108	USERDOMAIN	WIN-ETSA91RKCFP
3624	svchost.exe	0x5b0ff0	USERDOMAIN	WORKGROUP
1232	taskmgr.exe	0x1c1070	USERDOMAIN	WIN-ETSA91RKCFP
3152	cmd.exe	0x441038	USERDOMAIN	WIN-ETSA91RKCFP
1616	cmd.exe	0x3110b8	USERDOMAIN	WIN-ETSA91RKCFP
1136	iexplore.exe	0x3c10b8	USERDOMAIN	WIN-ETSA91RKCFP
3044	iexplore.exe	0x4510b8	USERDOMAIN	WIN-ETSA91RKCFP
3144	winpmem-1.3.1.	0x3c10b8	USERDOMAIN	WIN-ETSA91RKCFP                                                           
```
<h3>Flag</h3>
<pre>
WIN-ETSA91RKCFP
</pre>
