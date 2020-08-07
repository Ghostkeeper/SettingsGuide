Pozice Z zavádění extrudéru
====
Pokud je aktivována [zaváděcí kapka](../platform_adhesion/prime_blob_enable.md), označuje toto nastavení souřadnici Z, na které začíná pohyb čistící kapky. Cura se přesune do této pozice dříve, než bude zaváděcí kapka provedena.

Na rozdíl od souřadnic X a Y je toto nastavení stroje. Je tomu tak proto, že se předpokládá, že akt aktivace má pevnou souřadnici Z. Chcete-li vytvořit zaváděcí kapku, bude se tryska muset přesunout na podložku tisku a možná se posunout trochu nahoru a dolů. Souřadnice [X](../platform_adhesion/extruder_prime_pos_x.md) a [Y](../platform_adhesion/extruder_prime_pos_y.md) lze zvolit pomocí normálního nastavení, aby se posunula poloha zaváděcí kapky v případě, že prostor na podložce tisku je omezující, ale souřadnice Z ne.

Jedinou věcí, kterou se to změní, je souřadnice Z, na kterou Cura nařídí, přesunutí trysky před provedením příkazu zaváděcí kapky.

**Protože se jedná o nastavení stroje, není toto nastavení normálně v seznamu nastavení viditelné.**