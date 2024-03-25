<h1>binhexa</h1>
<h3>Description</h3>
<p>How well can you perfom basic binary operations?
Start searching for the flag here nc titan.picoctf.net 64026</p>

<h3>Solution</h3>

```python3
import sys

def calc(nil1,nil2,ops,sys):
    nilai_1 = int(str(nil1),2)
    nilai_2 = int(str(nil2),2)
    if ops == "x":
        if sys == "1to2":
            print(bin(nilai_1 * nilai_2)[2:])
    elif ops == "or":
        if sys == "1to2":
            print(bin(nilai_1 | nilai_2)[2:])
    elif ops == "and":
        if sys == "1to2":
            print(bin(nilai_1 & nilai_2)[2:])
    elif ops == "plus":
        if sys == "1to2":
            print(bin(nilai_1 + nilai_2)[2:])
    elif ops == "rshift":
        if sys == "1to1":
            print(bin(nilai_1 >> 1)[2:])
        elif sys == "2to1":
            print(bin(nilai_2 >> 1)[2:])
    elif ops == "lshift":
        if sys == "1to1":
            print(bin(nilai_1 << 1)[2:])
        elif sys == "2to1":
            print(bin(nilai_2 << 1)[2:])
            
if __name__ == "__main__":
    if len(sys.argv) == 5:
        arg = sys.argv
        nil1 = arg[1]
        nil2 = arg[2]
        ops = arg[3]
        sys = arg[4]
        calc(nil1,nil2,ops,sys)
    else:
        print("Error")

```

```console
Enter the results of the last operation in hexadecimal: 18

Correct answer!
The flag is: picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_1367e2c6}
```

<h3>Flag</h3>
<pre>picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_1367e2c6}</pre>
