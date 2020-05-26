Teplota retrakce pro zlomení
====
U některých tiskáren, je-li materiál zatažen do spínače vláken, musí být materiál čistě odřezán tak, aby prošel podavačem bez zamotání. Toto nastavení konfiguruje část postupu tak, aby bylo čistě odlomeno.

Toto nastavení upravuje teplotu trysky, když je materiál zatažen do druhé pozice, aby se materiál vytáhl na tenké vlákno. Toto jemné vlákno se vytáhne mimo vyhřívanou oblast trysky, což mu umožňuje se ochladit a ztuhnout. Tenké tvrdé vlákno materiálu může být během další fáze retrakce zlomeno.

![Nejprve se materiál zatáhne, aby se zabránilo výtoku](../../../articles/images/filament_switch_anti_ooze.svg)
![Za druhé se vlákno pomalu stahuje, aby vytáhlo tenké vlákno, které lze snadno zlomit a toto vlákno nechá ztuhnout](../../../articles/images/filament_switch_break_preparation.svg)
![Za třetí se vlákno rychle zatáhne a odlomí](../../../articles/images/filament_switch_break.svg)

**Tento parametr není v rozhraní Cura v současné době viditelný. Může být definován pouze profily. Cura ho během slicování také nepoužívá. Tiskárny, které rozumí formátu souboru materiálu Cura, jej však mohou použít ke správné konfiguraci svého postupu změny vlákna.** Díky skriptu pro následné zpracování lze do tisku vložit příkaz "M600", který vyvolá změnu vlákna.
