<h1><b>QR Code</b></h1>
<pre>
Bantu mimin buat decode QR Code ini dong. Cuman decode doang kok :)))

Challenge --> <a href='https://mega.nz/#!sgoUHIzb!mmQ5v0JKd1ZQRLyX73gi87z414UwgRISAWynAnjfcv4'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Decode QR pada URL <a href='https://webqr.com/'>QR_Reader</a>, atau dengan Script python dibawah</p>

```python3
from pyzbar import pyzbar
import cv2

image_qr = cv2.imread('qrcode (1).png')
qr = pyzbar.decode(image_qr)
for i in qr:
    barcodeData = i.data.decode("utf-8")
    print(barcodeData) #CTFR{qi3r_c0d3}
```
<h3><b>Flag</b></h3>
<pre>
CTFR{qi3r_c0d3}
</pre>
