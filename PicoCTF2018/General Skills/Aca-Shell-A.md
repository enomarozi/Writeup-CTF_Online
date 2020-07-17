<h1><b>Aca-Shell-A</h1></b>
<pre>
It's never a bad idea to brush up on those linux skills or even learn some new ones before you set off on this adventure! 
Connect with nc 2018shell.picoctf.com 58422.
</pre>
</b><h3>Solution</h3></b>
<p>Connect nc dan ikuti seluruh intruksi terminal</p>

```console
root@Python:/home/venom/Downloads# nc 2018shell.picoctf.com 58422
Sweet! We have gotten access into the system but we aren't root.
It's some sort of restricted shell! I can't see what you are typing
but I can see your output. I'll be here to help you along.
If you need help, type "echo 'Help Me!'" and I'll see what I can do
There is not much time left!
~/$ ls
blackmail
executables
passwords
photos
secret
~/$ cd secret
Now we are cookin'! Take a look around there and tell me what you find!
~/secret$ ls
intel_1
intel_2
intel_3
intel_4
intel_5
profile_ahqueith5aekongieP4ahzugi
profile_ahShaighaxahMooshuP1johgo
profile_aik4hah9ilie9foru0Phoaph0
profile_AipieG5Ua9aewei5ieSoh7aph
profile_bah9Ech9oa4xaicohphahfaiG
profile_ie7sheiP7su2At2ahw6iRikoe
profile_of0Nee4laith8odaeLachoonu
profile_poh9eij4Choophaweiwev6eev
profile_poo3ipohGohThi9Cohverai7e
profile_Xei2uu5suwangohceedaifohs
Sabatoge them! Get rid of all their intel files!
~/secret$ rm intel_1
Nice! Once they are all gone, I think I can drop you a file of an exploit!
Just type "echo 'Drop it in!' " and we can give it a whirl!
~/secret$ echo 'Drop it in!'
Drop it in!
I placed a file in the executables folder as it looks like the only place we can execute from!
Run the script I wrote to have a little more impact on the system!
~/secret$ cd ..
~/$ ls
blackmail
executables
passwords
photos
secret
~/$ cd executables
~/executables$ ls
dontLookHere
~/executables$ ./dontLookHere
 3cbe 9716 f271 7067 c80a ceed 6660 b784 fa68 c1f1 16aa 7cb5 4861 dc3c e669 5d8e 3f2a 9311 da55 ebd6 39cf 9eff 0766 57f4 4904
 10bd 484a 849e 5f58 67b0 9809 ae95 40a2 2673 92c9 9bcc a172 3d7d 1b3c e23f 68ca aaf9 b669 cd85 94c2 5ada 1322 91c2 c0a7 30ef
 7750 77f2 4283 bf09 c25e 431f f972 6db4 9a32 fd2a 9307 5272 1767 d77c d54c c83f 7355 cce4 13e8 1430 e5c8 b8de afd5 0ada 29f9
 a67a 6735 c1eb 47a5 194e d9f7 0655 1dd5 01ae 2cb0 dfe0 9af2 22fb 00e7 5efb 4792 b0bc 35fe feb6 bcd2 bc24 1d22 fae0 2609 10e5
 c049 7123 d529 779a f4f7 7dac d208 0e18 8207 f963 d55d d1ba 5f69 657a 4109 48f4 ee27 2700 4358 9739 a840 b4a5 17f4 3d82 c688
 a69e 98fe eb98 58f4 462a ab3f 175e c0c1 0dd1 ae02 164d 3487 e019 30d9 6922 f111 8b14 1ab8 c6aa 6f72 4413 9259 5736 7597 7a2e
 49ee 24c0 7c35 0e36 eec8 3081 bc5d e409 1c81 62d8 3a76 4239 2d91 daa7 d154 83bd 0f71 8104 3cf3 0e01 5862 b8e6 4c6b d837 1c8d
 efad bc90 c2d9 e342 1e4c 0add a24b b14d 2c61 3095 9027 b1a9 bcd5 f71e ac7d e44c 82cf 48d4 88b1 8ccc 1e3b 8e70 1d35 4d92 663d
 574a 416f 668b 3428 bb46 e55f 44a2 553f 0673 d36c be65 fad2 2c8c 4909 f6f8 a4ed 95f0 c24c 0938 5b45 0b98 09ac ac36 2171 18b1
 6fed b2a0 2a81 5b30 7974 307f 1561 6b8d 2745 2588 199f cc04 4e77 4e22 7a97 0053 2b87 ab21 946d e0a0 6b3c a8c9 fafe 6759 08eb
 4af1 f0ac b957 3f7c ce80 20c1 c03d fa51 310f 077d 1327 f5e2 daa4 d492 e6ba 4ffd 8157 dd6a f9f4 1ce9 9034 4f04 6d09 5902 0dc5
 2820 c6e6 d250 5687 6f88 d764 11b7 86ca 55d2 46d5 7df4 3be8 f0aa 17e1 12e4 96e2 ee49 afe7 99ae caea 7ec8 2323 cfc3 e089 a683
 fb6b 0ffb b94f 43f8 7efb 7f9d c6b6 ed61 e69c 0b69 525d e0d6 1228 49e3 bd88 4d4c 26cf 0663 5634 d44f 934a 7e2f f388 2180 a30e
 5ef9 9db8 dbab dfa6 c676 ca7e 152d 5728 7632 e006 2409 9873 96ca 531b 2625 6fc9 0d1f 2732 ada7 5abb b0d3 8b71 5a0d b1fc 6ab7
 efec a942 c1fe b0f9 a607 ad28 112a f53b a17e a200 f13a 1fbb e6e3 68d4 0b37 10f0 37a3 b79f 9ac6 f7ad e736 3860 3f55 8163 46bc
 adb3 cd4a 309b a3c6 1db9 7c81 c2b2 f415 8d0f eb7f 7abb 76fc 1792 6b17 61ea 4f7b 3c3c 0f99 a2bd 0f17 8cb6 2655 039e b658 f4dc
 c08d fe08 f40d 8d58 bad1 784b ba4a c384 e4e1 2f9d c807 116a 11f2 28a6 6c7d d503 fb85 ff66 cbf2 f892 2134 5091 3594 b23c 4bc5
 f0c4 4348 26bf 6b2e 8456 a112 8ca1 a07e 8fd8 11e2 46e7 cd83 134b deb7 6143 6a2c 7a24 5658 a7a7 e3e9 2bbd 7ccc 2b2f 93db be06
 9168 e7d5 bc4f f044 d04b fbed 98a6 1f34 98ea 19fb b484 d662 8d8a 243d 6d71 17b5 0915 a726 7572 96e2 b567 4f11 8f99 8a1f 3894
 9dd1 f7ae 6422 20e6 9014 c4c3 ee2f 114e 039e 25d1 6c3f 440f 8c09 813c 8022 dac5 2d40 e2a6 bc24 e5dc 9334 8cc6 663f c193 ce05
 6dd6 930f 806a 5737 abf0 ffe6 34c6 5008 826f d357 2a90 0273 8222 5a6c 855d 0097 6298 ccea 5983 177c 64e2 ac0c 0e4f a0b5 f83c
 54c0 215a 7cde 9f95 1c46 3cb8 7d1f 21af 9060 81d8 1378 7d48 c747 c990 5ed8 7714 5097 68a6 0561 8aa3 a4e4 76b7 cd60 2698 b0c8
 4b80 0939 bef0 85e1 f325 c949 ec2f fc9e ab73 59fd 001f 2a54 66b2 f9c3 8c96 f776 29a9 81b6 c621 39e9 f7ab 5b1f e916 36e9 220a
 95ce 61a7 f7fc 1dd8 a382 217b 53b7 d195 4339 9b01 8924 a0b3 aea0 3581 85ff b92b 7d02 a003 91f4 68c8 ddb9 c667 23b2 c719 e3dc
 0c99 dcc0 4135 e7c2 d049 fdc2 3ebb ef7b f109 9388 ae1c f2c8 c652 8780 db61 17a4 26ff 9724 1877 cd88 f371 fa21 f0eb 54d1 2222
 d23e 2e5b 1b3b 64db 051f dbc3 2a5b 5264 6969 af4c fea2 1d11 c672 8ac4 3b8d 9f24 d25f 76f2 27a9 4f28 5559 510d a5d3 a02d 19ba
 3e58 98c7 8dd9 2396 4dcc 4ba7 cabf 658b 5018 f876 a69b af80 0ff3 9f82 e13e b1a7 be11 bba4 0846 c5e8 f7fd 793d 59de 671d 49f1
 f75e f382 761f fd51 b716 d456 689a 7242 7ff6 dbba bf71 8292 b68d 0dcb add1 0326 2de8 4fe6 1b40 480a d732 14d8 a1c7 5f4f 4c54
 d15a 33da b3b4 3d46 3081 462a dd21 90d1 a711 4836 98a2 098a a26a 0fe5 4f73 97ef c26d 9a14 d374 c057 2062 a8f5 5605 fbd2 2434
 670b a01b f886 9f46 ca43 2f74 635e ab2b 0631 c65d 90cc e53f 74a0 df6f fd63 e9d8 211d 8fea 605e 97c2 757d 9cfc 12d0 d288 e9f2
 5779 3777 e0d9 7dca de88 32eb 9dbd f3dc cb33 6084 ceb6 0912 688f 9913 432c 8d6a 858c c377 98a8 54ee c6ef 149f 6128 6393 344d
 3356 cb0a 05b6 dcdb 9410 898f 5dd5 394f b9d3 baa3 c8b0 7344 b73c e5d7 e849 1e74 f062 a65e 67a4 3cdd 9afb 63c1 fee0 829b 2737
 48fd 5a17 1003 5476 052d d249 71d1 b914 b664 b46f e736 dd93 5e57 a27a 07d3 4ec6 72d9 d5a6 0a60 e176 76d7 d05e 6d97 ba5f 215d
Looking through the text above, I think I have found the password. I am just having trouble with a username.
Oh drats! They are onto us! We could get kicked out soon!
Quick! Print the username to the screen so we can close are backdoor and log into the account directly!
You have to find another way other than echo!
~/executables$ cd ..
~/$ ls
blackmail
executables
passwords
photos
secret
~/$ cd passwords
~/passwords$ ls
~/passwords$ whoami
l33th4x0r
Perfect! One second!
Okay, I think I have got what we are looking for. I just need to to copy the file to a place we can read.
Try copying the file called TopSecret in tmp directory into the passwords folder.
~/passwords$ cp /tmp/TopSecret passwords
Server shutdown in 10 seconds...
Quick! go read the file before we lose our connection!
~/passwords$ ls
TopSecret
~/passwords$ cat TopSecret
Major General John M. Schofield's graduation address to the graduating class of 1879 at West Point is as follows: The discipline which makes the soldiers of a free country reliable in battle is not to be gained by harsh or tyrannical treatment.On the contrary, such treatment is far more likely to destroy than to make an army.It is possible to impart instruction and give commands in such a manner and such a tone of voice as to inspire in the soldier no feeling butan intense desire to obey, while the opposite manner and tone of voice cannot fail to excite strong resentment and a desire to disobey.The one mode or other of dealing with subordinates springs from a corresponding spirit in the breast of the commander.He who feels the respect which is due to others, cannot fail to inspire in them respect for himself, while he who feels,and hence manifests disrespect towards others, especially his subordinates, cannot fail to inspire hatred against himself.
picoCTF{CrUsHeD_It_4e355279}
```
</b><h3>Flag</h3></b>
<pre>
picoCTF{CrUsHeD_It_4e355279}
</pre>
