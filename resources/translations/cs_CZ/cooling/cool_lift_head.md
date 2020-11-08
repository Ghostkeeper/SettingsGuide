Zvednout hlavu
====
Po dosažení [minimálního času vrstvy](cool_min_layer_time.md) se tisková hlava zpomalí, aby se zabránilo tisku rychleji než je minimální čas vrstvy. Takto má předchozí vrstva čas na vychladnutí a ztuhnutí, než se na ni umístí další vrstva. Tisková hlava se může zpomalit, dokud není dosaženo [minimální rychlosti](cool_min_speed.md).

Pokud je toto nastavení povoleno a tisková hlava se musí pohybovat pomaleji než je minimální rychlost, aby se zachoval minimální čas vrstvy, pak se tisková hlava po tisku vrstvy bude pohybovat mírně nahoru. Potom bude chvíli počkat, dokud nebude dosaženo minimálního času vrstvy, než začne další vrstva. Nebude se pohybovat pomaleji než minimální rychlostí.

Pokud je tento parametr zakázán, bude tisková hlava čekat na konci vrstvy, přičemž se tryska dotkne tisku.

![Po dosažení minimálního času vrstvy se může hlava zvednout](../images/cool_fan_speed_cs.svg)

Tisková hlava se vždy pohybuje o 3 mm nahoru. V tuto chvíli není k dispozici žádné nastavení.

Kompromisy
----
Při zpomalení trysky dochází ke kompromisu, aby se vrstva lépe ochladila. Minimální doba vrstvy je zamýšlena tak, aby poskytla určitý čas na vychladnutí materiálu zpomalením pohybu tiskové hlavy. Během této doby budou ventilátory foukat na maximální výkon, aby ho rychleji ochladily, ale horká tryska je také stále na plastu. U velmi malých kousků může horká tryska přenášet do tisku více tepla, než kolik může ventilátor ochladit. To způsobí, že se plast roztaví ještě více, než kdybyste neměli žádnou minimální dobu vrstvy.

Se zvednutím hlavy je tento kompromis vyřešen. Stále můžete zpomalit do určité míry, ale u velmi malých vrstev vysune horkou trysku pryč, takže již nebude přenášet teplo do tisku. Hlava je držena dostatečně blízko, aby na ni ventilátory na tiskové hlavě stále foukaly.

Nevýhodou je, že bude účinně provádět [Z-skok](../travel/retraction_hop.md), což přináší nějaké [strunování](../troubleshooting/stringing.md). Zatímco zvedání hlavy může zlepšit prověšování a vytváření kapek, způsobí to jiný druh nepořádku. Trochou následného manuálního opracování nožem lze struny, které způsobí, vyčistit.