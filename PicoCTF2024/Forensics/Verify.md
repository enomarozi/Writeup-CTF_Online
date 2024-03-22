<h1>Verify</h1>
<h3>Description</h3>
<p>People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.
You can download the challenge files here:</p>
<a href='https://artifacts.picoctf.net/c_rhea/23/challenge.zip'>File</a>
<p>Additional details will be available after launching your challenge instance.</p>

<h3>Solution</h3>
<p>Check semua file di folder files/, disana ada banyak file ASCII Text dan ada 1 file yang sudah digenerate openssl</p>

```bash
#!/bin/bash

file_contents=$(cat checksum.txt)

for file in files/*; do
        checksum=$(sha256sum "$file" | awk '{print $1}')
        if [ "$checksum" == "$file_contents" ]; then
                data=$(openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -in "$file" -k picoCTF)
                echo $data;
        fi
done
```
<h3>Flag</h3>
<pre>picoCTF{trust_but_verify_451fd69b}</pre>
