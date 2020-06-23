Preference rohového švu
====
S tímto nastavením můžete ovládat polohu švů ve vztahu k rohům vašeho modelu.

Obecně existují dvě možnosti umístění švu: skryté ve vnitřním rohu nebo exponované ve vnějším rohu. Obvykle je nejlepší skrýt šev ve vnitřním rohu, protože šev tam bude stěží viditelný. Je však také možné jej umístit do vnějšího rohu, aby bylo možné oříznout šev nožem nebo jej brousit brusným papírem, pokud je možné dodatečné zpracování dílu provést.

Zde jsou možnosti dostupné pro toto nastavení a jejich účinky.
* **Žádné:** Rohy nejsou preferovány. Šev bude vybrán tak, aby co nejlépe vyhovoval požadavkům [Zarovnání švu v Z](z_seam_type.md).
* **Skrýt šev:** Nejlepší je schovat šev do vnitřního rohu. Pokud je zarovnání švu v Z nastaveno na "Nejostřejší roh", je vždy vybrán nejvnitřnější roh. Je-li nastaven na "Nejkratší", vybere se vnitřní roh, který je blízko k aktuální poloze trysky, když začíná obrys.
* **Vystavit šev:** Nejlepší je odhalit šev na vnějším rohu. Pokud je zarovnání švu v Z nastaveno na "Nejostřejší roh", vždy se vybere nejostřejší vnější roh. Pokud je nastavena na "Nejkratší", vybere se vnější roh, který je blízko k aktuální poloze trysky, když začíná obrys.
* **Skrýt nebo vystavit šev:** Tato funkce umožňuje umístit šev na ostrý roh, ať už uvnitř nebo vně, pokud není na ploché stěně.<!--if cura_version >= 4.2 -->
* **Inteligentní maskování:** To umožňuje, aby byl šev umístěn v rohu, jako v případě "Skrýt nebo vystavit šev", ale vnitřní rohy jsou vybírány častěji než vnější rohy, pokud jsou v obrysu vnitřní rohy k dispozici. Pokud neexistují žádné vnitřní rohy, zvolí se vnější roh.<!--endif-->
