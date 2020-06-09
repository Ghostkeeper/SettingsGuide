Minimální čas vrstvy
====
Minimální čas vrstvy nastavuje nejkratší čas povolený pro tisk vrstvy. Tiskárna nemá povoleno tisknout vrstvy rychleji.

To je nezbytné k tomu, aby předchozí vrstva mohla vychladnout před nasazením další vrstvy. Tím je zajištěno, že předchozí vrstva zcela ztuhla, aby se zabránilo jejímu ochabnutí.

![Jaká rychlost ventilátoru se používá, a kde](../images/cool_fan_speed_cs.svg)

Toto nastavení má tři efekty:
* Pokud se vrstva tiskne rychleji, než je uvedeno v parametru [Práh 
 normální/maximální rychlosti ventilátoru](cool_min_layer_time_fan_speed_max.md), zvýší se rychlost ventilátoru tak, aby dosáhl parametru [Maximální rychlost ventilátoru](cool_fan_speed_max.md). Pokud je vrstva tak malá, že její tisk trvá kratší dobu, použije se maximální rychlost ventilátoru. Rychlost ventilátoru je mezi nimi interpolována.
* Pokud vytisknutí vrstvy zabere méně času, než je minimální doba vrstvy, rychlost tisku se zpomalí, takže vždy zabere minimální čas vrstvy.
* Pokud je tisková hlava příliš pomalá (tisk pomalejší než nastavení parametru [Minimální rychlost](cool_min_speed.md), bude tisková hlava čekat na konci vrstvy a může ji trochu zvednout.
