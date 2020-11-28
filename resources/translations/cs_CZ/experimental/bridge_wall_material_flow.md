Tok při tisku stěny přemostění
====
Toto nastavení upravuje množství materiálu, který je extrudován pro tisk stěn přemostění.

Snížení množství materiálu účinně zmenší šířku linií stěn, které tvoří přemostění. Při snížených šířkách linií je poměr povrchu ke hmotnosti linií větší, což jim umožňuje se rychleji ochladit a zabránit jim v tom, aby se tolik prohýbaly.

Přílišné snížení průtoku však způsobí velkou změnu průtoku, zejména v kombinaci s [pomalejší rychlostí tisku](bridge_wall_speed.md). Ve skutečnosti nebude materiál schopen měnit svůj tok velmi rychle, což znamená, že linie budou o něco silnější, než se očekávalo, když se tok zpomalí, a o něco tenčí, než se očekávalo, když se tok zrychlí. První z těchto efektů může být vyrovnán určitým [dojezdem](bridge_wall_coast.md), ale to vyžaduje pečlivé nastavení.