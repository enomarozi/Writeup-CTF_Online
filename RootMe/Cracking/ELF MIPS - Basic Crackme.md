<h1>ELF MIPS - Basic Crackme</h1>
<h3>Description</h3>
<label>Find the validation password.</label><a href='https://static.root-me.org/cracking/ch27/ch27.bin'>File</a>
<h3>Solution</h3>
<label>Buka file dengan ghidra</label>

```c
undefined4 main(void)

{
  size_t sVar1;
  undefined4 local_58;
  char local_54 [4];
  char local_50;
  char local_4f;
  char local_4e;
  char local_4d;
  char local_4c [9];
  char local_43;
  char local_42;
  undefined4 local_c;
  
  puts("crack-me for Root-me by s4r");
  puts("Enter password please");
  fgets(local_54,0x40,_stdin);
  sVar1 = strlen(local_54);
  local_54[sVar1 - 1] = '\0';
  sVar1 = strlen(local_54);
  if (sVar1 == 0x13) {
    for (local_58 = 8; local_58 < 0x11; local_58 = local_58 + 1) {
      if (local_54[local_58] != 'i') {
        FUN_00400814();
        return 0;
      }
    }
    if (local_42 == 's') {
      if (local_43 == 'p') {
        if (local_4d == 'm') {
          if ((local_54[2] == 'n') && (local_4e == 'n')) {
            if (local_54[0] == 'c') {
              if (local_54[1] == 'a') {
                if (local_54[3] == 't') {
                  if (local_50 == 'r') {
                    if (local_4f == 'u') {
                      FUN_004007c0();
                      return local_c;
                    }
                    FUN_00400814();
                  }
                  else {
                    FUN_00400814();
                  }
                }
                else {
                  FUN_00400814();
                }
              }
              else {
                FUN_00400814();
              }
            }
            else {
              FUN_00400814();
            }
          }
          else {
            FUN_00400814();
          }
        }
        else {
          FUN_00400814();
        }
      }
      else {
        FUN_00400814();
      }
    }
    else {
      FUN_00400814();
    }
  }
  else {
    FUN_00400814();
  }
  return 0;
```
<label>Persamaan dengan python</label>

```python3
local_54 = 'cantrunmiiiiiiiiips'
for i in range(0x8,0x11):
    if local_54[i] != 'i':
        print("failed!")
if local_54[0] != 'c':
    if local_54[1] != 'a':
        if local_54[2] != 'n':
            if local_54[3] != 't':
                if local_54[4] != 'r':
                    if local_54[5] != 'u':
                        if local_54[6] != 'n':
                            if local_54[7] != 'm':
                                if local_54[17] != 'p':
                                    if local_54[18] != 's':
                                        print('failed!')
                                    print('failed!')
                                print('failed!')
                            print('failed!')
                        print('failed!')
                    print('failed!')
                print('failed!')
            print('failed!')
        print('failed!')
    print('failed!')

print("Success")
```

<h3>Flag</h3>
<pre>
cantrunmiiiiiiiiips
</pre>
