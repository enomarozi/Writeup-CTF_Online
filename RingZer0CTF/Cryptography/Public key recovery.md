<h1><b>Public key recovery</h1></b>
<pre>
-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQDwkrxVrZ+KCl1cX27SHDI7EfgnFJZ0qTHUD6uEeSoZsiVkcu0/
XOPbz1RtpK7xxpKMSnH6uDc5On1IEw3A127wW4Y3Lqqwcuhgypd3Sf/bH3z4tC25
eqr5gA1sCwSaEw+yBxdnElBNOXxOQsST7aZGDyIUtmpouI1IXqxjrDx2SQIDAQAB
AoGBAOwd6PFitnpiz90w4XEhMX/elCOvRjh8M6bCNoKP9W1A9whO8GJHRnDgXio6
/2XXktBU5OfCVJk7uei6or4J9BvXRxQpn1GvOYRwwQa9E54GS0Yu1XxTPtnBlqKZ
KRbmVNpv7eZyZfYG+V+/f53cgu6M4U3SE+9VTlggfZ8iSqGBAkEA/XvFz7Nb7mIC
qzQpNmpKeN4PBVRJBXqHTj0FcqQ5POZTX6scgE3LrxVKSICmm6ungenPXQrdEQ27
yNQsfASFGQJBAPL2JsjakvTVUIe2JyP99CxF5WuK2e0y6N2sU3n9t0lde9DRFs1r
mhbIyIGZ0fIkuwZSOqVGb0K4W1KWypCd8LECQQCRKIIc8R9iIepZVGONb8z57mA3
sw6l/obhfPxTrEvC3js8e+a0atiLiOujHVlLqD8inFxNcd0q2OyCk05uLsBxAkEA
vWkRC3z7HExAn8xt7y1Ickt7c7+n7bfGuyphWbVmcpeis0SOVk8QrbqSNhdJCVGB
TIhGmBq1GnrHFzffa6b1wQJAR7d8hFRtp7uFx5GFFEpFIJvs/SlnXPvOIBmzBvjU
yGglag8za2A8ArHZwA1jXcFPawuJEmeZWo+5/MWp0j+yzQ==
-----END RSA PRIVATE KEY-----

</br>
Public key = md5(base64 blob only) MD5 2 first bytes are 0x42f5
</pre>
</b><h3>Solution</h3></b>
<p>Merupakan RSA private-key, salin semua private-key pada soal dari BEGIN s/d END dan simpan pada file text. Lanjut, ektrak public-key dengan tool openssl</p>

```console
root@Python:/home/venom/Downloads/flag# openssl rsa -in private.pem -out pubkey -pubout
writing RSA key
root@Python:/home/venom/Downloads/flag# cat pubkey 
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDwkrxVrZ+KCl1cX27SHDI7Efgn
FJZ0qTHUD6uEeSoZsiVkcu0/XOPbz1RtpK7xxpKMSnH6uDc5On1IEw3A127wW4Y3
Lqqwcuhgypd3Sf/bH3z4tC25eqr5gA1sCwSaEw+yBxdnElBNOXxOQsST7aZGDyIU
tmpouI1IXqxjrDx2SQIDAQAB
-----END PUBLIC KEY-----
root@Python:/home/venom/Downloads/flag# strings pubkey | tail -n 5 | head -n 4
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDwkrxVrZ+KCl1cX27SHDI7Efgn
FJZ0qTHUD6uEeSoZsiVkcu0/XOPbz1RtpK7xxpKMSnH6uDc5On1IEw3A127wW4Y3
Lqqwcuhgypd3Sf/bH3z4tC25eqr5gA1sCwSaEw+yBxdnElBNOXxOQsST7aZGDyIU
tmpouI1IXqxjrDx2SQIDAQAB
root@Python:/home/venom/Downloads/flag# strings pubkey | tail -n 5 | head -n 4 | tr -d '\n' | md5sum
42f51df8b6a2bafa824c179a38066e5d  -
```
</b><h3>Flag</h3></b>
<pre>
FLAG-9869O2dQ43d1r116kfD0Sj5n
</pre>
