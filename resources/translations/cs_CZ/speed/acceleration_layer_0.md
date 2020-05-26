Zrychlení počáteční vrstvy
====
Toto nastavení řídí hodnotu, jakou tryska zrychluje v různých směrech během tisku první vrstvy. Zrychlení během tisku první vrstvy může být nastaveno na jinou hodnotu než pro zbytek tisku.

Zatímco stěny, přilnavost podložky tisku, dolní strana, podpěra a výplň mohou mít různé míry zrychlení, během první vrstvy budou stejné. Hodnota zrychlení počáteční vrstvy bude mít přednost před hodnotami zrychlení jednotlivých struktur. Pohyby přesunu mohou mít vždy jinou míru zrychlení než pohyby vytlačování díky parametrům [Zrychlení přesunu počáteční vrstvy](acceleration_travel_layer_0.md) a [Zrychlení tisku počáteční vrstvy](acceleration_print_layer_0.md). Parametr [Zrychlení sukénky/krempy](acceleration_skirt_brim.md) opět přepíše zrychlení tisku počáteční vrstvy.

Tisk při vysokých hodnotách zrychlení může způsobit vibrace, které ovlivňují tiskárnu. Tyto vibrace mohou zejména způsobit, že se podložka tisku otřásá shora dolů, což je škodlivé pro přilnutí tisku k tiskové podložce. Snížení zrychlení pro první vrstvu může snížit vibrace během této kritické části procesu tisku. Tisk však bude trvat déle a přílišné snížení hodnoty zrychlení může způsobit nerovnoměrné vytlačování v rozích, což také ovlivňuje přilnavost k tiskové podložce.
