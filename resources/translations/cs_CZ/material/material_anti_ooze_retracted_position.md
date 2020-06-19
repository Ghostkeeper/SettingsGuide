Pozice retrakce, zabraňující výtoku
====
U některých tiskáren, je-li materiál zatažen do spínače vláken, musí být materiál čistě odřezán tak, aby prošel podavačem bez zamotání. Toto nastavení konfiguruje část postupu tak, aby bylo čistě odlomeno.

Toto nastavení upravuje první pozici, do které je materiál zatažen, aby se zabránilo výtoku. Materiál v této fázi ještě není odlomen. Cílem je, tahem dovnitř, pouze rychle odstranit tlak na tryskovou komoru.

![Nejprve se materiál podle tohoto nastavení zatáhne, aby se zabránilo výtoku](../../../articles/images/filament_switch_anti_ooze.svg)
![Za druhé se vlákno pomalu stahuje, aby vytáhlo tenké vlákno, které lze snadno zlomit a toto vlákno nechá ztuhnout](../../../articles/images/filament_switch_break_preparation.svg)
![Za třetí se vlákno rychle zatáhne a odlomí](../../../articles/images/filament_switch_break.svg)

**Tento parametr není v rozhraní Cura v současné době viditelný. Může být definován pouze profily. Cura ho během slicování také nepoužívá. Tiskárny, které rozumí formátu souboru materiálu Cura, jej však mohou použít ke správné konfiguraci svého postupu změny vlákna.** Díky skriptu pro následné zpracování lze do tisku vložit příkaz `M600`, který vyvolá změnu vlákna.
