Automatická teplota
====
Pro rychlejší tisk je nejlepší tisknout při mírně vyšším tlaku. Díky tomu je termoplast tekutější, což mu umožňuje rychleji protékat otvorem trysky. Toto nastavení automaticky upravuje teplotu podle průměrného toku materiálu z trysky.

Chcete-li zjistit, do jaké míry by měla být teplota upravena, použijte [Graf teploty toku](material_flow_temp_graph.md). Rychlost průtoku se počítá v krychlových milimetrech za sekundu. Pokud to uvedeme ve vztahu k toku, dostaneme určitou teplotu. Toto hodnocení bude použito pro teplotu tisku. Je-li toto nastavení aktivováno, nebude již používáno běžné nastavení [teploty tisku](../material/material_print_temperature.md) ve prospěch teploty vypočtené z průtoku.

Účelem tohoto nastavení je dosáhnout lepší kvality tisku snížením nad-extruze a pod-extruze, pokud dojde k velkým změnám toku v tisku. Častým případem je případ hranice mezi pláštěm a výplní. Protože plášť je normálně tištěn mnohem pomaleji než výplňový materiál, měly by být vrstvy, kde je mnoho výplňového materiálu, tištěny při o něco vyšší teplotě, aby se materiál mohl během tisku této výplně, řádně vytlačit.

U mnoha tiskáren má PID regulátor, který reguluje teploty v trysce tiskárny, tendenci chovat se trochu přehnaně, když dojde k mnoha změnám v krátkém čase. Při použití tohoto nastavení proto může být tisk velmi nepřesný.

**Toto nastavení není aktuálně v rozhraní Cura vidět a nelze ho aktivovat.**
