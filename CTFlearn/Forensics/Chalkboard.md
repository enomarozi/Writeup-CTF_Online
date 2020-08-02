<h1><b>Chalkboard</h1></b>
<pre>
Solve the equations embedded in the jpeg to find the flag. 
Solve this problem before solving my Scope challenge which is worth 100 points.

<a href='https://ctflearn.com/challenge/download/972'>math.jpg</a> 
</pre>
</b><h3>Solution</h3></b>
<p>Eksekusi perintah exiftool dan grep pada file JPG</p>

```console
root@Python:/home/venom/Downloads# exiftool math.jpg -a | grep -i comment
Comment                         : The flag for this challenge is of the form:..CTFlearn{I_Like_Math_x_y}..where x and y are the solution to these equations:..3x + 5y = 31..7x + 9y = 59...
root@Python:/home/venom/Downloads# 
```
<p>Disana terdapat comment yang menyatakan flag yaitu CTFlearn{I_Like_Math_x_y}, dimana x dan y merupakan persamaan 3x + 5y = 31 dan 7x + 9y = 59</p>
<pre>
3x + 5y = 31  --> 21x + 35y = 217 <-- dikali 7
7x + 9y = 59  --> 21x + 27y = 177 <-- dikali 3
----------------------------------  dikurang
              -->        8y = 40
              -->         y = 5

untuk x --> 3x + 5(5) = 31
            3x + 25 = 31
                 3x = 25 - 31
                 3x = -6
                  x = 2
</pre>
<p>Dari persamaan diatas didapatkan x = 2, dan y = 5, dan dibawah cara bruteforce hehe</p>

```python
for x in range(10):
    for y in range(10):
        c1 = 3*x + 5*y
        c2 = 7*x + 9*y
        if c1==31 and c2==59:
            print(x,y)
```
</b><h3>Flag</h3></b>
<pre>
CTFlearn{I_Like_Math_2_5}
</pre>
