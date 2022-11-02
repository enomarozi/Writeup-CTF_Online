<h1>reverse_cipher</h1>
<p>We have recovered a <a href='https://jupiter.challenges.picoctf.org/static/7aa5f383ec616fe9d72c2ffe1fabd0d9/rev'>binary</a> and a <a href='https://jupiter.challenges.picoctf.org/static/7aa5f383ec616fe9d72c2ffe1fabd0d9/rev_this'>text file</a>. Can you reverse the flag.</p>
<h3>Solution</h3>
<p>Source code dari ghidra tool</p>

```c
void main(void)

{
  size_t sVar1;
  char local_58 [23];
  char local_41;
  int local_2c;
  FILE *local_28;
  FILE *local_20;
  uint local_14;
  int local_10;
  char local_9;
  
  local_20 = fopen("flag.txt","r");
  local_28 = fopen("rev_this","a");
  if (local_20 == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (local_28 == (FILE *)0x0) {
    puts("please run this on the server");
  }
  sVar1 = fread(local_58,0x18,1,local_20);
  local_2c = (int)sVar1;
  if ((int)sVar1 < 1) {
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  local_10 = 0;
  while (local_10 < 8) {
    local_9 = local_58[local_10];
    fputc((int)local_9,local_28);
    local_10 = local_10 + 1;
  }
  local_14 = 8;
  while ((int)local_14 < 0x17) {
    if ((local_14 & 1) == 0) {
      local_9 = local_58[(int)local_14] + '\x05';
    }
    else {
      local_9 = local_58[(int)local_14] + -2;
    }
    fputc((int)local_9,local_28);
    local_14 = local_14 + 1;
  }
  local_9 = local_41;
  fputc((int)local_41,local_28);
  fclose(local_28);
  fclose(local_20);
  return;
}

```
<p>Pada program, 8 Char pertama flag tanpa ada proceses encrypt, kemudian char 8 s/d 24 terdapat encrypt yaitu jika index char &(logical operation) 1 == 0
maka char ditambah +(0x5), dan jika tidak char ditambah +(-2)</p>
<p>Jadi, untuk decrypt <b>picoCTF{w1{1wq84fb<1>49}</b> bisa membalikan operasi (penjumlahan) ke (pengurangan) atau + jadi -, dan begitu sebaliknya</p>
  
 ```python3
local_20 = open('rev_this','r').read()
local_28 = open('result.txt','a')
local_10 = 0
while (local_10<8):
    print(local_20[local_10],end='')
    local_10 += 1
local_14 = 8
while (local_14<0x17):
    if ((local_14 & 1) == 0):
        print(chr(ord(local_20[local_14])-0x5),end='')
    else:
        print(chr(ord(local_20[local_14])-(-2)),end='')
    local_14+=1
  ```
  
 <h3>Flag</h3>
 <p>
  picoCTF{r3v3rs36ad73964}
  <p>
