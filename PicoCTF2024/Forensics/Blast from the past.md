<h1>Blast from the past</h1>
<h3>Description</h3>
<p>The judge for these pictures is a real fan of antiques. Can you age this photo to the specifications?
Set the timestamps on this picture to 1970:01:01 00:00:00.001+00:00 with as much precision as possible for each timestamp. In this example, +00:00 is a timezone adjustment. Any timezone is acceptable as long as the time is equivalent. As an example, this timestamp is acceptable as well: 1969:12:31 19:00:00.001-05:00. For timestamps without a timezone adjustment, put them in GMT time (+00:00). The checker program provides the timestamp needed for each.
Use this <a href="https://artifacts.picoctf.net/c_mimas/89/original.jpg">picture</a>.
Submit your modified picture here:</p>
<pre>
nc -w 2 mimas.picoctf.net 64033 < original_modified.jpg
Check your modified picture here:
nc -d mimas.picoctf.net 52280
</pre>
<h3>Solution</h3>
<p>Ganti Tag Metadata yang berhubungan dengan time ke 1970:01:01 00:00:00.001</p>
  
```console
root@xisco-VirtualBox:/home/xisco/Downloads# list_params=("-AllDates" "-CreateDate" "-DateTimeOriginal" "-ModifyDate" "-SubSecCreateDate" "-SubSecDateTimeOriginal" "-SubSecModifyDate")
root@xisco-VirtualBox:/home/xisco/Downloads# for ((i=0; i<${#list_params[@]};i++)); do exiftool ${list_params[$i]}="1970:01:01 00:00:00.001" original.jpg; done;
    1 image files updated
    1 image files updated
    1 image files updated
    1 image files updated
    1 image files updated
    1 image files updated
    1 image files updated
root@xisco-VirtualBox:/home/xisco/Downloads# 
```
<p>Dan untuk Image_UTC_Data ganti 1 miliseconds pada raw bytes</p>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# xxd original.jpg | tail -n 10
002b82a0: bfeb c5bf f433 5d50 dcc6 6ddc ffd9 0000  .....3]P..m.....
002b82b0: 010a 0e00 0000 496d 6167 655f 5554 435f  ......Image_UTC_
002b82c0: 4461 7461 3130 3030 3100 3030 3030 3030  Data00001.000000
002b82d0: 3000 00a1 0a08 0000 004d 4343 5f44 6174  0........MCC_Dat
002b82e0: 6133 3130 0000 610c 1800 0000 4361 6d65  a310..a.....Came
002b82f0: 7261 5f43 6170 7475 7265 5f4d 6f64 655f  ra_Capture_Mode_
002b8300: 496e 666f 3153 4546 486b 0000 0003 0000  Info1SEFHk......
002b8310: 0000 0001 0a57 0000 0023 0000 0000 00a1  .....W...#......
002b8320: 0a34 0000 0013 0000 0000 0061 0c21 0000  .4.........a.!..
002b8330: 0021 0000 0030 0000 0053 4546 54         .!...0...SEFT
```

<pre>
  31 37 30 30 35 31 33 31 38 31 34 32 30 menjadi 30 30 30 30 31 00 30 30 30 30 30 30
</pre>

```console
Checking tag 7/7
Timezones do not have to match, as long as it's the equivalent time.
Looking at Samsung: TimeStamp
Looking for '1970:01:01 00:00:00.001+00:00'
Found: 1970:01:01 00:00:00.001+00:00
Great job, you got that one!

root@xisco-VirtualBox:/home/xisco/Downloads# nc -w 2 mimas.picoctf.net 64033 < original.jpg
root@xisco-VirtualBox:/home/xisco/Downloads# nc -d mimas.picoctf.net 52280
```

<h3>Flag</h3>
<pre>picoCTF{71m3_7r4v311ng_p1c7ur3_a25174ab}</pre>
