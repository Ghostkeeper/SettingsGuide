Povolit aktivační věž
====
Tento systém vytiskne na vaši tiskové ploše věž se směsí materiálů. Věž je určena k likvidaci, ale používá se k aktivaci materiálu po každé výměně extrudéru.

![Jak vypadá aktivační věž a její rozměry](../images/prime_tower_cs.svg)

Zatímco jiné extrudéry tisknou, někdy z trysky vytéká materiál, přičemž tryska zůstává nenaplněna materiálem. Následně je nezbytné materiál napenetrovat, jinak materiál zpočátku správně neprotéká.

Aktivační věž se skládá z vnější skořepiny, která je plně vytištěna každou vrstvou jedním extrudérem. To je nezbytné pro zajištění stability věže, ale někdy bude vyžadováno, pro určitý tisk, přepnutí  extrudéru. Všechny ostatní extrudéry budou tisknout smyčky uvnitř této skořepiny nalitím jejich materiálu do věže, nejlépe podél vnitřních stěn. Tyto extrudéry nepotřebují aktivaci, pokud začnou na vrstvě, protože nebudou v tomto okamžiku nebudou uvedeny do pohotovostního stavu.

Materiál, který se vybere pro vnější plášť, je materiál s největší [Tendencí přilnavosti](../material/material_adhesion_tendency.md). Toto je skryté nastavení, které nelze změnit z rozhraní, naznačuje, jak dobře se vrstvy drží pohromadě. Výběrem materiálu s největší adhezí mezi vrstvami je minimalizováno riziko rozbití aktivační věže. Pokud má více materiálů stejnou tendenci přilnavosti (např. u dvoubarevných tisků se stejným typem materiálu), je vybrán extruder s nejnižším číslem.

Kromě plnění se tryska bude pohybovat také uvnitř věže, aby otřela veškerý materiál trysky, který se nahromadil během pohotovostního režimu. Tím se zabrání tomu, aby se výtok přilepil na tisk. Proto se aktivační věž někdy také nazývá *čistící věž*.

Nevýhody aktivační věže jsou v tom, že tisk trvá trochu déle a zabírá místo na podložce tisku.