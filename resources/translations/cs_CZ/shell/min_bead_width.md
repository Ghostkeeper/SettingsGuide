Minimální šířka linie tenké stěny
====
Toto nastavení umožňuje tisknout velmi drobné detaily s šířkou linie, která je pro ně ve skutečnosti příliš velká. Místo tisku velmi tenkých linií se tiskne s přiměřenější šířkou linie.

Pokud je hodnota [Minimální velikost prvku](min_feature_size.md) velmi nízká, mohly by být vytištěny některé velmi tenké díly. To nefunguje dobře. Je možné vytisknout linie menší, než je velikost trysky, ale ne o mnoho. Tisk příliš tenkých linií vede k nekonzistentní extruzi.

Místo toho jsou tyto velmi tenké linie širší, aby se vytlačovaly konzistentněji. Jakákoli část modelu, která je tenčí než minimální šířka tenké linie, se vytiskne pomocí jediné linie o minimální šířce tenké linie. Linie se pak stanou širšími, než byla původní šířka modelu. Tím se sníží rozměrová přesnost, ale alespoň se bude tisknout spolehlivě.

Hodnota tohoto nastavení by měla odpovídat šířce nejtenčí linie, které tiskárna spolehlivě dosáhne, než začne vytvářet drsné povrchy a nekonzistentní extruzi. Tato hodnota se obvykle pohybuje někde mezi velikostí trysky a polovinou velikosti trysky. Jeho zvětšení vede k tomu, že tenké díly jsou tištěny příliš tlustě, ale snižuje možnost nedotisku v důsledku snahy vytisknout příliš tenké linie.