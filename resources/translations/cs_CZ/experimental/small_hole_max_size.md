Maximální velikost malých otvorů
====
Malé detaily tisku jsou často velmi důležité z hlediska rozměrů. Toto nastavení způsobí, že malé otvory v tisku budou vytištěny pomaleji, aby se dosáhlo větší přesnosti.

Pokud má kruhový otvor průměr menší, než je hodnota tohoto parametru, rychlost, při které je vytištěn obvod tohoto otvoru, bude vynásobena faktorem [Rychlost tisku malého prvku](small_feature_speed_factor.md) (obvykle se sníží). Otvory, které nejsou kruhové, budou vytištěny odlišnou rychlostí, pokud je obvod menší než kružnice se zde specifikovaným průměrem. Viz také [Maximální délka malé struktury](small_feature_max_length.md); toto je nastavení, které bude skutečně použito pro slicování.

Běžným případem použití této funkce je tisk otvorů pro šrouby ve velmi přesných rozměrech. Při tisku malých otvorů má kapka tendenci být tažena tryskou do rohu. Pokud jsem roh je velmi ostrý, jako je tomu u malých otvorů, má to za následek zmenšení otvoru. Pokud je tisk pomalejší, je tato trakce snížena, protože materiál má více času na usazení a protože mechanická trakce je prostě nižší.

Zvýšením tohoto nastavení se více obrysů označí jako „malý prvek“. Pomaleji bude vytištěno více otvorů v tisku. Tyto otvory budou proto vytištěny přesněji, ale doba tisku bude delší.
