<h1>PNG - Pixel Indicator Technique</h1>
<h3>Description</h3>
<label>Find the hidden message in this image.

SHA1 hash: 52062f33b7a58050c082a5f677a1ae626da32d88</label><a href='https://static.root-me.org/steganographie/ch13/ch13.png'>File</a>
<h3>Solution</h3>
<label>Salah satu teknik steganography pada PNG</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# stegopit -v -i G ch13.png  
                          _                         _ _
                      ___| |_ ___  __ _  ___  _ __ (_) |_
                     / __| __/ _ \/ _` |/ _ \| '_ \| | __|
                     \__ \ ||  __/ (_| | (_) | |_) | | |_
                     |___/\__\___|\__, |\___/| .__/|_|\__|
                                  |___/      |_|


 
07:15:54 [DEBUG] Image size: 1000x1000
07:15:54 [DEBUG] RMS:        8296
07:15:54 [DEBUG] N other:    IC=G
07:15:54 [DEBUG] Channels:   GBR
07:15:54 [INFO] Hidden data:
Image based steganography utilize the images as cover media to hide secret data. The common technique used in this field replaces the least significant bits (LSB) of image pixels with intended secret bits. Several improvements to enhance the security of the LSB method have been presented earlier. This paper proposed a new improved technique that takes the advantage of the 24 bits in each pixel in the RGB images using the two least significant bits of one channel to indicate existence of data in the other two channels. The stego method does not depend on a separate key to take out the key management overhead. !!! The flag for this challenge is : "PiTiSAls0aSteg4n0gr4ph1eM3thod". Instead, it is using the size of the secret data as selection criteria for the first indicator channel to insert security randomness. Our proposed technique is analyzed using security and capacity measures and compared to two other similar work. This proposed pixel indicator technique for RGB image steganography showed interesting promising result.
```
<h3>Flag</h3>
<pre>
PiTiSAls0aSteg4n0gr4ph1eM3thod
</pre>
