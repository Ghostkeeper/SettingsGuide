Graf teploty toku
====
Pro rychlejší tisk je nejlepší tisknout při mírně vyšším tlaku. Díky tomu je termoplast tekutější, což mu umožňuje rychleji protékat otvorem trysky. Když je aktivována [Automatická teplota](material_flow_dependent_temperature.md), určuje toto nastavení pro každou rychlost průtoku teplotu, při kterém má být materiál vytištěn. Průtok je pak zprůměrován pro každou vrstvu pro stanovení teploty pro tuto vrstvu

Průtok je počítán v krychlových milimetrech za sekundu, průměrován pro celou vrstvu. Hodnota je vyjádřena ve stupních Celsia. Hodnota tohoto parametru musí být seznam souřadnic oddělených čárkami. Každá souřadnice má tvar `[<průtok>, <teplota>]`.

Účelem tohoto nastavení je dosáhnout lepší kvality tisku snížením nad-extruze a po-extruze, pokud se v tisku vyskytnou velké změny toku. Častým případem je případ hranice mezi pláštěm a výplní. Protože plášť je normálně tištěn mnohem pomaleji než materiál výplně, měly by být vrstvy, kde je mnoho výplňového materiálu, tištěny při o něco vyšší teplotě, aby se materiál mohl během tisku tohoto materiálu řádně tuto výplň vytlačit.

U mnoha tiskáren má PID regulátor, který reguluje teploty v trysce tiskárny, tendenci chovat se trochu přehnaně, když dojde k mnoha změnám v krátkém čase. Při použití tohoto nastavení proto může být tisk velmi nepřesný.

**Toto nastavení není aktuálně v rozhraní Cura vidět a nelze ho aktivovat.**
