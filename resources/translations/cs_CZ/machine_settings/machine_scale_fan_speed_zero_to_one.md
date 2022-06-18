Stupnice otáček ventilátoru na 0-1
====
Aby bylo možné řídit rychlost otáčení ventilátorů tiskárny, vkládá Cura do g-kódu příkazy s parametrem, který řídí jejich otáčky. Obvykle je tímto parametrem číslo v rozmezí 0 až 255. Některé tiskárny však přijímají i číslo mezi 0 a 1 a interpretují ho pak jinak. Toto nastavení způsobí, že Cura zapíše rychlost ventilátoru jako číslo mezi 0 a 1, a nikoli mezi 0 a 255.

Na trhu existují 3 typy chování firmwaru v různých tiskárnách.
* Většina tiskáren akceptuje rychlost ventilátoru pouze jako číslo v rozsahu 0 až 255. Toto nastavení by pak mělo být vypnuto, jinak se ventilátor nikdy skutečně neroztočí.
* Některé tiskárny (zejména RepRapFirmware) akceptují čísla mezi 0 a 255, ale pokud je to 1 nebo méně, interpretují to jako číslo mezi 0 a 1. Toto nastavení by pak mělo být povoleno, jinak by mohlo dojít k vzácnému případu, kdy se Cura pokusí nastavit rychlost ventilátoru například na 0,4 % (1 z 255), ale tiskárna místo toho nastaví 100 %.
* Některé tiskárny přijímají pouze čísla od 0 do 1. Toto nastavení by pak mělo být také povoleno, jinak bude ventilátor vždy buď zcela vypnutý, nebo zcela zapnutý.