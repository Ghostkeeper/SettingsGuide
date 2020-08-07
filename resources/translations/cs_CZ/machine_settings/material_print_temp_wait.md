Čekat na vyhřátí trysky
====
Počáteční vrstva může mít jinou [teplotu trysky](../material/material_print_temperature_layer_0.md) než je [teplota trysky pro zbytek tisku](../material/material_print_temperature.md). Pokud je toto nastavení povoleno, bude tiskárna před pokračováním v tisku čekat, dokud se nedosáhne této teploty.

Počká, až se tryska zahřeje nebo ochladí na vhodnou teplotu. Zatímco popis tohoto nastavení říká, že bude čekat na zahřátí, ochladí se stejně dobře. Tryska nebude čekat na jiné změny teploty, například na [teplotu při zahájení tisku](../material/material_initial_print_temperature.md), [konečnou teplotu tisku](../material/material_final_print_temperature.md) nebo na [pohotovostní teplotu](../material/material_standby_temperature.md). Pokud tisknete v [režimu jeden po druhém](../blackmagic/print_sequence.md), bude také tryska čekat na dosažení teploty tisku počáteční vrstvy, když se znovu začíná s počáteční vrstvou pro další model. V těchto případech bude tiskárna před pokračováním v tisku čekat, až se dosáhne nové teploty

**Protože se jedná o nastavení stroje, není toto nastavení normálně v seznamu nastavení viditelné.**