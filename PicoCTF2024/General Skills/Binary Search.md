<h1>Binary Search</h1>
<h3>Description</h3>
<p></p>Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.
Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!
You can download the challenge files here:</p>
<a href='https://artifacts.picoctf.net/c_atlas/20/challenge.zip'>challenge.zip</a>
<p>ssh -p 60545 ctf-player@atlas.picoctf.net
Using the password 6abf4a82. Accept the fingerprint with yes, and ls once connected to begin. Remember, in a shell, passwords are hidden!</p>
<h3>Solution</h3>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# ssh -p 60545 ctf-player@atlas.picoctf.net
ctf-player@atlas.picoctf.net's password: 
Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: 500
Lower! Try again.
Enter your guess: 250
Higher! Try again.
Enter your guess: 375
Higher! Try again.
Enter your guess: 450
Lower! Try again.
Enter your guess: 400
Higher! Try again.
Enter your guess: 425
Lower! Try again.
Enter your guess: 420
Higher! Try again.
Enter your guess: 422
Congratulations! You guessed the correct number: 422
Here's your flag: picoCTF{g00d_gu355_bee04a2a}
Connection to atlas.picoctf.net closed.
root@xisco-VirtualBox:/home/xisco/Downloads# 
```
<p>Cari dan Prediksi sesuai pesan error yang muncul</p>
<h3>Flag</h3>
<pre>picoCTF{g00d_gu355_bee04a2a}</pre>
