<h1><b>Victor you're hidding me something</b></h1>
<pre>
Fort heureux l'homme qui trouvera
La vérité au travère des noires
Abysses d'une âme tourmenter par la
Galère d'un amour improbable.

Ces âmes que tu rappelles,
Mon coeur, ne reviennent pas.
Pourquoi donc s'obstinent-elles,
Hélas ! à rester là-bas ?

Dans les sphères éclatantes,
Dans l'azur et les rayons,
Sont-elles donc plus contentes
Qu'avec nous qui les aimions ?

Nous avions sous les tonnelles
Une maison près Saint-Leu.
Comme les fleurs étaient belles !
Comme le ciel était bleu !

Parmi les feuilles tombées,
Nous courions au bois vermeil ;
Nous cherchions des scarabées
Sur les vieux murs au soleil ;

On riait de ce bon rire
Qu'Éden jadis entendit,
Ayant toujours à se dire
Ce qu'on s'était déjà dit ;

Je contais la Mère l'Oie ;
On était heureux, Dieu sait !
On poussait des cris de joie
Pour un oiseau qui passait.
</pre>

<h3><b>Solution</h3></b>
<p>flag cuts are found in 1 bytes for all lines, save message in text.txt</p>

```python3
file = open("text.txt")
for i in file:
    print(i.strip("\n")[:1],end="")
```

<h3><b>Flag</h3></b>
<pre>
FLAGCMPHDDSQNUCCPNNSOQACJOOP
</pre>
