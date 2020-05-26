Zvednout hlavu
====
Po dosažení [minimálního času vrstvy](cool_min_layer_time.md) se tisková hlava zpomalí, aby se zabránilo tisku rychleji než je minimální čas vrstvy. Takto má předchozí vrstva čas na vychladnutí a ztuhnutí, než se na ni umístí další vrstva. Tisková hlava se může zpomalit, dokud není dosaženo [minimální rychlosti](cool_min_speed.md).

Pokud je toto nastavení povoleno a tisková hlava se musí pohybovat pomaleji než je minimální rychlost, aby se zachoval minimální čas vrstvy, pak se tisková hlava po tisku vrstvy bude pohybovat mírně nahoru. Potom bude chvíli počkat, dokud nebude dosaženo minimálního času vrstvy, než začne další vrstva.

Pokud je tento parametr zakázán, bude tisková hlava čekat na konci vrstvy, přičemž se tryska dotkne tisku.

![Po dosažení minimálního času vrstvy se může hlava zvednout](../images/cool_fan_speed_cs.svg)

Tisková hlava se vždy pohybuje o 3 mm nahoru. V tuto chvíli není k dispozici žádné nastavení.
