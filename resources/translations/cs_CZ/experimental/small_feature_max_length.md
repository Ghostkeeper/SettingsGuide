Maximální délka malého prvku
====
Malé detaily tisku jsou často velmi důležité z hlediska rozměrů. Toto nastavení způsobí, že malé otvory v tisku budou vytištěny pomaleji, aby se dosáhlo větší přesnosti.

Pokud má otvor menší obvod, než který je uveden v tomto parametru, bude rychlost, při které je obvod tohoto otvoru vytištěn, vynásobena faktorem [Rychlost tisku malého prvku](small_feature_speed_factor.md) (obvykle se sníží). Tento parametr je jiným způsobem přiblížení se k parametru [Maximální velikost malých otvorů](small_hole_max_size.md), který je obecnější, než pro kruhové otvory.

Běžným případem použití této funkce je tisk otvorů pro šrouby ve velmi přesných rozměrech. Při tisku malých otvorů má kapka tendenci být tažena tryskou do rohu. Pokud jsem roh je velmi ostrý, jako je tomu u malých otvorů, má to za následek zmenšení otvoru. Pokud je tisk pomalejší, je tato trakce snížena, protože materiál má více času na usazení a protože mechanická trakce je prostě nižší.

Zvýšením tohoto nastavení se více obrysů označí jako "malý prvek". Pomaleji bude vytištěno více otvorů v tisku. Tyto otvory budou proto vytištěny přesněji, ale doba tisku bude delší.