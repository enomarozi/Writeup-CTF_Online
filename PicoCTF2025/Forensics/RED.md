```python3
import cv2
from base64 import b64decode

img = cv2.imread('red.png',cv2.IMREAD_UNCHANGED)
result = ''
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        b,g,r,a = img[i,j]
        for k in r,g,b,a:
            lsb = bin(k)[2:].rjust(8,'0')[-1]
            if len(result) == img.shape[0]*4:
                break
            result += str(lsb)

flag = ''.join([chr(int(result[:i][-8:],2)) for i in range(8,len(result)+8,8)])
print(b64decode(flag.encode()).decode())
```
