Minimální rychlost
====
Firmware Marlin pro 3D tiskárny, ze kterého je odvozena většina firmwaru tiskáren, má minimální rychlost pro všechny své pohyby. Toto nastavení označuje, jaká je minimální rychlost pro firmware vaší tiskárny.

Minimální rychlost je nastavení, které zabrání chybám ve firmwaru v důsledku dělení nulou. Firmware musí vypočítat časové intervaly mezi kroky, aby mohl motorům poslat signál se správným načasováním. Pokud se motor potřebuje pohybovat rychlostí 0 (tj. stát v klidu), jedná se o nekonečný časový interval, který firmware neumí dobře zvládnout. To platí pouze v případě, že se žádný z motorů tiskárny skutečně neotáčí. Například při pohybu ve směru X se motor ovládající osu Y stále neotáčí, ale kvůli složitosti krokových motorů zde neplatí minimální rychlost.

Cura používá tuto minimální rychlost k vytvoření správných odhadů času. Používá se při zrychlování na začátku tisku nebo po pauze a při zpomalení do klidového stavu na konci tisku nebo před pauzou.

*Protože se jedná o nastavení stroje, není toto nastavení normálně v seznamu nastavení viditelné.*