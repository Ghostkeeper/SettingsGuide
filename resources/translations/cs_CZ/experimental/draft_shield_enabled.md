Aktivovat ochranný štít
====
Pokud je toto nastavení povoleno, tiskárna vytvoří kolem vašeho obalu skořepinu, která chrání tisk před vzdušnými proudy z okolního prostředí.

![Okolo modelu se vytiskne ochranný štít](../../../articles/images/draft_shield_enabled.png)

Některé tiskárny a tiskové materiály jsou velmi citlivé na prostředí, ve kterém jsou tištěny. Tisk na různých místech na podložce tisku může vést k různým výsledkům, protože jsou citlivější na průvan zvenčí. Pokud je tisk ponechán přes noc a místnost se ochladí, může to mít významný dopad na tisk. Cílem tohoto nastavení je snížit tento efekt vytvořením malého izolovaného objemu kolem tisku. Slouží jako provizorní "vytápěný prostor", který udržuje tisk v teple a chrání ho před studeným průvanem přicházejícím z vnějšku.

Štít se vytiskne současně při tisku modelu. Pokud je do tisku zapojeno několik extrudérů, bude štít vytištěn pomocí extrudéru, který začíná vrstvu. To se bude střídat z vrstvy na vrstvu.

Štít má na tisk několik hlavních vlivů:
* Udržuje teplotu tisku více konstantní. Toto je požadovaný efekt ochranného štítu. V důsledku toho by se mělo snížit pruhování vlivem teplotních posunů v místnosti.
* Obecně bude teplota uvnitř ochranného štítu vyšší než v případě, že ochranný kryt neexistuje. Ve skutečnosti má teplo větší potíže s únikem a nemohou vznikat konvekční proudy, které vzrůstají horkým vzduchem tisku. To má vliv na všechny aspekty tisku. Zejména bude více strun a prověšování.
* Ventilátory tiskové hlavy budou méně účinné. Štít také narušuje proud vzduchu. Pro zvýšení účinnosti ventilátorů na tiskové hlavě lze zvětšit [vzdálenost](draft_shield_dist.md) ochranného štítu.
* Ochranný štít se může zdvojnásobit jako [štít proti výtoku](../dual/ooze_shield_enabled.md). Pokud jsou pohyby provedeny směrem k předmětu chráněnému štítem, veškerá prosakující část, která zůstane na trysce, bude na otřena na štítu.
* Ochranný štít lze použít jako [aktivační věž](../dual/prime_tower_enable.md). Protože je tištěn před objektem, je tisk ochranného štítu způsob, jak materiál očistit a řádně zavést. To je účinné pouze u 2 extrudérů, protože ne všechny extrudéry se očistí, pokud jich bude více než 2.