<h1>Command & Control - level 3</h1>
<h3>Description</h3>
<label>Berthier, the antivirus software didn’t find anything. It’s up to you now. Try to find the malware in the memory dump. The validation flag is the md5 checksum of the full path of the executable.

The uncompressed memory dump md5 hash is e3a902d4d44e0f7bd9cb29865e0a15de</label><a href='https://static.root-me.org/forensic/ch2/ch2.tbz2'>File</a>
<h3>Solution</h3>
<label>Check aplikasi yang berjalan</label>

```console
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# vol -f ch2.dmp windows.cmdline                                                                   
Volatility 3 Framework 2.27.0
Progress:  100.00		PDB scanning finished                        
PID	Process	Args

4	System	-
308	smss.exe	\SystemRoot\System32\smss.exe
404	csrss.exe	%SystemRoot%\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,12288,512 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=winsrv:ConServerDllInitialization,2 ServerDll=sxssrv,4 ProfileControl=Off MaxRequestThreads=16
456	wininit.exe	-
468	csrss.exe	%SystemRoot%\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,12288,512 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=winsrv:ConServerDllInitialization,2 ServerDll=sxssrv,4 ProfileControl=Off MaxRequestThreads=16
500	winlogon.exe	-
560	services.exe	C:\Windows\system32\services.exe
576	lsass.exe	C:\Windows\system32\lsass.exe
584	lsm.exe	C:\Windows\system32\lsm.exe
692	svchost.exe	C:\Windows\system32\svchost.exe -k DcomLaunch
764	svchost.exe	C:\Windows\system32\svchost.exe -k RPCSS
832	svchost.exe	C:\Windows\System32\svchost.exe -k LocalServiceNetworkRestricted
904	svchost.exe	C:\Windows\System32\svchost.exe -k LocalSystemNetworkRestricted
928	svchost.exe	C:\Windows\system32\svchost.exe -k netsvcs
1084	svchost.exe	C:\Windows\system32\svchost.exe -k LocalService
1172	svchost.exe	C:\Windows\system32\svchost.exe -k NetworkService
1220	AvastSvc.exe	"C:\Program Files\AVAST Software\Avast\AvastSvc.exe"
1712	spoolsv.exe	C:\Windows\System32\spoolsv.exe
1748	svchost.exe	C:\Windows\system32\svchost.exe -k LocalServiceNoNetwork
1872	sppsvc.exe	-
1968	vmtoolsd.exe	"C:\Program Files\VMware\VMware Tools\vmtoolsd.exe"
336	wlms.exe	-
448	VMUpgradeHelpe	-
1612	TPAutoConnSvc.	"C:\Program Files\VMware\VMware Tools\TPAutoConnSvc.exe"
2352	taskhost.exe	"taskhost.exe"
2496	dwm.exe	"C:\Windows\system32\Dwm.exe"
2548	explorer.exe	C:\Windows\Explorer.EXE
2568	TPAutoConnect.	TPAutoConnect.exe -q -i vmware -a COM1 -F 30
2600	conhost.exe	-
2660	VMwareTray.exe	"C:\Program Files\VMware\VMware Tools\VMwareTray.exe" 
2676	VMwareUser.exe	"C:\Program Files\VMware\VMware Tools\VMwareUser.exe" 
2720	AvastUI.exe	"C:\Program Files\AVAST Software\Avast\AvastUI.exe" /nogui
2744	StikyNot.exe	"C:\Windows\System32\StikyNot.exe" 
2772	iexplore.exe	"C:\Users\John Doe\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\iexplore.exe" 
2900	SearchIndexer.	C:\Windows\system32\SearchIndexer.exe /Embedding
3176	wmpnetwk.exe	"C:\Program Files\Windows Media Player\wmpnetwk.exe"
3352	svchost.exe	C:\Windows\system32\svchost.exe -k LocalServiceAndNoImpersonation
3452	swriter.exe	-
3512	soffice.exe	-
3556	soffice.bin	-
3564	soffice.bin	"C:\Program Files\LibreOffice 3.6\program\swriter.exe" "-o" "C:\Users\John Doe\Documents\Procedure Winpmemdump.odt" "--writer" "-env:OOO_CWD=2C:\\Users\\John Doe\\Documents"
3624	svchost.exe	C:\Windows\System32\svchost.exe -k secsvcs
1232	taskmgr.exe	"C:\Windows\system32\taskmgr.exe" /4
3152	cmd.exe	"C:\Windows\system32\cmd.exe" 
3228	conhost.exe	-
1616	cmd.exe	cmd.exe
2168	conhost.exe	\??\C:\Windows\system32\conhost.exe
1136	iexplore.exe	"C:\Program Files\Internet Explorer\iexplore.exe" 
3044	iexplore.exe	"C:\Program Files\Internet Explorer\iexplore.exe" SCODEF:1136 CREDAT:71937
1720	audiodg.exe	C:\Windows\system32\AUDIODG.EXE 0x298
3144	winpmem-1.3.1.	winpmem-1.3.1.exe  ram.dmp
                                                                                                                                                                                                                                 
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# vol -f ch2.dmp windows.cmdline | grep -i 'iexplore'
2772ressiexplore.exe	"C:\Users\John Doe\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\iexplore.exe" 
1136	iexplore.exe	"C:\Program Files\Internet Explorer\iexplore.exe" 
3044	iexplore.exe	"C:\Program Files\Internet Explorer\iexplore.exe" SCODEF:1136 CREDAT:71937
```
<label>Ada aplikasi ressiexplore.exe</label>

<h3>Flag</h3>
<pre>
49979149632639432397b3a1df8cb43d
</pre>
