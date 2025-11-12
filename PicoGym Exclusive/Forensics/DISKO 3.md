<h1>DISKO 3</h1>
<h3>Description</h3>
<label>Can you find the flag in this disk image? This time, its not as plain as you think it is!
Download the disk image <a href='https://artifacts.picoctf.net/c/543/disko-3.dd.gz'>here</a>.</label>
<h3>Solution</h3>
<label>Tool The Sleuth Kit atau Mount disk</label>

```console
┌──(root㉿Venom)-[/home/venom/Downloads/PicoCTF]
└─# fls -r disko-3.dd
d/d 4:	log
+ d/d 22:	private
+ d/d 24:	sysstat
+ d/d 26:	stunnel4
++ r/r 70:	stunnel.log
+ d/d 28:	mysql
+ d/d 30:	inetsim
++ d/d 102:	report
+ d/d 32:	installer
++ d/d 134:	cdebconf
+++ r/r 150:	questions.dat
+++ r/r 152:	templates.dat
++ r/r 136:	Xorg.0.log
++ r/r 138:	partman
++ r/r 140:	syslog
++ r/r 143:	hardware-summary
++ r/r 145:	status
++ r/r 519091:	lsb-release
+ r/r 519123:	vmware-vmsvc-root.2.log
+ r/r 519125:	kern.log.4.gz
+ r/r 519127:	Xorg.0.log
+ r/r 519130:	vmware-network.4.log
+ r/r 519132:	boot.log
+ r/r 519134:	syslog.3.gz
+ r/r 519137:	vmware-vmtoolsd-root.log
+ r/r 522627:	daemon.log
+ r/r * 522628:	_lag.gz
+ r/r * 522629:	_ESSAGES
+ r/r 522632:	alternatives.log.2.gz
+ r/r 522634:	debug
+ d/d 522636:	lightdm
++ r/r 554806:	lightdm.log
++ r/r 554809:	lightdm.log.old
++ r/r 554811:	x-0.log
++ r/r 554813:	x-0.log.old
++ r/r 554816:	seat0-greeter.log
++ r/r 555203:	seat0-greeter.log.old
+ r/r 522639:	vmware-network.6.log
+ r/r 522642:	alternatives.log
+ r/r 555285:	vmware-vmsvc-root.1.log
+ r/r 555288:	Xorg.0.log.old
+ r/r 555291:	vmware-network.8.log
+ r/r 555294:	vmware-vmsvc-root.log
+ r/r 555297:	vmware-vmsvc-root.3.log
+ r/r 556259:	boot.log.6
+ r/r 556262:	vmware-network.5.log
+ r/r 556265:	macchanger.log.4.gz
+ d/d 556267:	apt
++ r/r 556550:	eipp.log.xz
++ r/r 556552:	history.log
++ r/r 556554:	term.log.2.gz
++ r/r 556557:	history.log.5.gz
++ r/r 556559:	term.log
++ r/r 556561:	term.log.1.gz
++ r/r 561588:	history.log.1.gz
++ r/r 561591:	history.log.2.gz
++ r/r 561593:	term.log.5.gz
++ r/r 561595:	term.log.4.gz
++ r/r 561598:	history.log.4.gz
++ r/r 561600:	term.log.3.gz
++ r/r 572451:	history.log.3.gz
+ r/r 556269:	dpkg.log.1
+ r/r 556271:	boot.log.5
+ r/r 556273:	wtmp
+ r/r 575571:	dpkg.log.5.gz
+ r/r 575573:	lastlog
+ r/r 575576:	vmware-network.3.log
+ r/r 575578:	syslog.4.gz
+ r/r 575580:	boot.log.1
+ r/r 575583:	vmware-network.2.log
+ r/r 575585:	faillog
+ r/r 603171:	kern.log.3.gz
+ r/r 603173:	dpkg.log.4.gz
+ r/r 603176:	vmware-network.1.log
+ r/r 603179:	vmware-network.7.log
+ d/d 603181:	journal
++ d/d 608872:	480afdbb61874a758c0b53617cfc8e8f
+++ r/r 608892:	system@7a442d5ca4df4e0f9507094c9269ca6a-0000000000005a8a-0006054ede6dfcb2.journal
+++ r/r 752228:	system@d902d27452664082ae8a9ac82cb69ba1-0000000000004b19-0006054ecec0fb53.journal
+++ r/r 752236:	system@b0aa03528b9c43dc896b9ab01ba4c893-00000000000042ae-0006054ec01755dc.journal
+++ r/r 1039652:	system@fe4e86893ffe4006869e03921f0c0c32-00000000000052d8-0006054edbce9160.journal
+++ r/r 1039660:	system@54b9f53d65d44041abdf784998995b81-000000000000624c-0006054ef1ae82cf.journal
+++ r/r 1324196:	system@185d88d5eb13416d80fa5cb1c5faf4d0-000000000000a97e-00062a2783e88318.journal
+++ r/r 1324199:	user-1000.journal
+++ r/r 1324207:	system@185d88d5eb13416d80fa5cb1c5faf4d0-000000000001feae-00062ba433aaa6e0.journal
+++ r/r 3225783:	system@d902d27452664082ae8a9ac82cb69ba1-00000000000050fb-0006054ed43fd222.journal
+++ r/r 3225791:	system@24d583de9c1a4252813ff1f373a8814d-0000000000006989-00060561dfa7e3c8.journal
+++ r/r 3225799:	system@185d88d5eb13416d80fa5cb1c5faf4d0-00000000000070c7-0006224d2862127d.journal
+++ r/r 3225807:	user-1000@d902d27452664082ae8a9ac82cb69ba1-00000000000050fa-0006054ed43ef163.journal
+++ r/r 3225815:	user-1000@94309907b19d4653afc79e24b6eec039-00000000000005b4-0005e76be8304b42.journal
+++ r/r 3225820:	system@0006054e6fd33237-813b83aec6062020.journal~
+++ r/r 3225828:	user-1000@185d88d5eb13416d80fa5cb1c5faf4d0-000000000002374d-00062eff8e6c0038.journal
+++ r/r 3225836:	system@fe4e86893ffe4006869e03921f0c0c32-00000000000058b3-0006054edc51935b.journal
+++ r/r 3225844:	user-1000@fe4e86893ffe4006869e03921f0c0c32-00000000000058b2-0006054edc4fe35c.journal
+++ r/r 3225849:	user-1000@0006054e70c65fc3-7af43b1c79f1269a.journal~
+++ r/r 3225857:	system@7a442d5ca4df4e0f9507094c9269ca6a-000000000000605c-0006054ee0dded41.journal
+ r/r 603184:	vmware-network.log
+ r/r 603186:	dpkg.log.2.gz
+ r/r 532020:	flag
v/v 3225859:	$MBR
v/v 3225860:	$FAT1
v/v 3225861:	$FAT2
V/V 3225862:	$OrphanFiles

┌──(root㉿Venom)-[/home/venom/Downloads/PicoCTF]
└─# fls -r disko-3.dd | grep -i 'flag'
+ r/r 532020:	flag
                                                                                                                                                                  
┌──(root㉿Venom)-[/home/venom/Downloads/PicoCTF]
└─# icat disko-3.dd 532020         
Here is your flag
picoCTF{n3v3r_z1p_2_h1d3_654235e0}
```
<h3>Flag</h3>
<pre>
picoCTF{n3v3r_z1p_2_h1d3_654235e0}
</pre>
