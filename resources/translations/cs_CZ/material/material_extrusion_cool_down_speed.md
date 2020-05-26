Modifikátor rychlosti chlazení extrudéru
====
Pokud je funkce [Automatická teplota](../experimental/material_flow_dependent_temperature.md) aktivována, bude teplota tisku upravena podle množství vytlačovaného materiálu.

Když se materiál zahřívá uvnitř tryskové komory, odvádí se teplo z trysky . Rychlejší vytlačování materiálu má tendenci odebírat z trysky více tepla. Pokud teplotní sonda není přesně na konci trysky, má tryska při vytlačování materiálu mírně nižší teplotu než při zastavení, a to i při dobrém PID regulátoru.

Toto nastavení popisuje množství tepla ztraceného v trysce během tisku. Dodatečné teplo ztracené vytlačováním bude potom kompenzováno zvýšením požadované teploty tisku z g-kódu. Hodnota nastavení závisí na konstrukci trysky, tepelné kapacitě tištěného materiálu a rychlosti vytlačování.
