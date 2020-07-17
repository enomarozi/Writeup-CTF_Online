<h1><b>LOGO</h1></b>
<pre>
It is often said that Death leaves out his messages in famous pictures and logos. 
We are certain that our logo is also one of the victims. 
Find and Submit SHA-256 of the flag obtained from <a href="http://static.beast.sdslabs.co/static/LOGO/sdslabs.png">this</a> image
</pre>
<h3><b>Solution</h3></b>
<p>Didapatkan sebuah image png</p>
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/sdslabs.png">
</p>
<p>gunakan tool zsteg pada terminal dan reverse text</p>

```console
root@Python:/home/venom/Downloads# zsteg sdslabs.png -a | head -n 1
b1,a,msb,XY         .. text: "3r3h7_3b_ll1w_r00dkc4b_l43r_n0053r3h7_3b_ll1w_r00dkc4b_l43r_n0053r3h7_3b_ll1w_r00dkc4b_l43r_n0053r3h7_3b_ll1w_r00dkc4b_l43r_n0053r3h7_3b_ll1w_r00dkc4b_l43r_n0053r3h7_3b_ll1w_r00dkc4b_l43r_n005"
root@Python:/home/venom/Downloads# echo "3r3h7_3b_ll1w_r00dkc4b_l43r_n0053r3h7_3b_ll1w_r00dkc4b_l43r_n0053r3h7_3b_ll1w_r00dkc4b_l43r_n0053r3h7_3b_ll1w_r00dkc4b_l43r_n0053r3h7_3b_ll1w_r00dkc4b_l43r_n0053r3h7_3b_ll1w_r00dkc4b_l43r_n005" | rev
500n_r34l_b4ckd00r_w1ll_b3_7h3r3500n_r34l_b4ckd00r_w1ll_b3_7h3r3500n_r34l_b4ckd00r_w1ll_b3_7h3r3500n_r34l_b4ckd00r_w1ll_b3_7h3r3500n_r34l_b4ckd00r_w1ll_b3_7h3r3500n_r34l_b4ckd00r_w1ll_b3_7h3r3
root@Python:/home/venom/Downloads# 
```
<h3><b>Flag</h3></b>
<pre>
500n_r34l_b4ckd00r_w1ll_b3_7h3r3
</pre>
