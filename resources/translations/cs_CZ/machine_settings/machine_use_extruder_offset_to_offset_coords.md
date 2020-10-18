Odsazení s extrudérem
====
Toto nastavení rozhoduje, zda má Cura psát souřadnice pro přesun na pozici pro tiskovou hlavu nebo pro trysku.

Pokud má vaše tiskárna pouze jednu trysku, je souřadný systém vaší tiskárny s největší pravděpodobností zarovnán s vaší tryskou. To znamená, že pohyb do pozice [50,50] ve skutečnosti posune do této pozice  špičku trysky. Pokud však vaše tiskárna obsahuje více trysek a tyto trysky jsou v tiskové hlavě vedle sebe, pak na tom záleží.

Některé tiskárny by přesunuly tiskovou hlavu na stejné místo bez ohledu na to, která tryska je aktuálně aktivována. Zatímco g-kód by mohl tiskárně přikázat, aby se přesunula na pozici [50,50], špička aktuálně aktivní trysky by se mohla místo toho přesunout do pozice [68,50], protože je například 18 mm napravo od první trysky. V tomto případě by toto nastavení mělo být povoleno.

Ostatní tiskárny automaticky upraví polohu tiskové hlavy tak, aby se aktivní tryska posunula do polohy uvedené v g-kódu. To znamená, že pokud g-kód přikáže tiskárně, aby se přesunula do pozice [50,50], přesunul by se do této pozice aktuálně aktivní extrudér. Samotná tisková hlava by se trochu posunula na stranu, aby tam umístila aktivní extrudér. Pokud se vaše tiskárna chová tímto způsobem, mělo by být toto nastavení deaktivováno.

**Protože se jedná o nastavení stroje, není toto nastavení normálně v seznamu nastavení viditelné.**