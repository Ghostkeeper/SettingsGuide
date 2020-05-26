Rychlost tisku počáteční vrstvy
====
Tento parametr umožňuje nastavit rychlost tisku spodní vrstvy modelu.

Nastavením tohoto parametru můžete upravit rychlost retrakčních pohybů v první vrstvě, ale ne pohyby přesunu. Chcete-li to provést, upravte parametr [Rychlost přesunu počáteční vrstvy](speed_travel_layer_0.md). I když stěny, plášť a podpěru lze normálně tisknout různými rychlostmi, nelze je vytisknout pro počáteční vrstvu. Vše bude vytištěno rychlostí uvedenou v tomto parametru. Ve výchozím nastavení tento parametr ovlivňuje [rychlost tisku sukénky/krempy](skirt_brim_speed.md), ale vždy je lze upravit samostatně. [Rychlost tisku základní vrstvy raftu](../platform_adhesion/raft_base_speed.md) není ovlivněna.

Snížení rychlosti tisku počáteční vrstvy zlepší přilnavost mezi modelem a podložkou tisku. Je to proto, že materiál zůstává déle teplejší a pak může déle protékat. To snižuje vnitřní napětí v materiálu a zvyšuje kontaktní povrch, dva faktory, které zvyšují přilnavost.
