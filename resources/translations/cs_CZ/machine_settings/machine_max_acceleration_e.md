Maximální zrychlení vlákna
====
Toto nastavení označuje maximální zrychlení, které zvládnou motory podavače tiskárny, podle firmwaru tiskárny.

Toto nastavení se používá pouze k získání správných odhadů času. [Zrychlení](../speed/acceleration_print.md) nastavené aplikací Cura nemá žádný limit, ale Cura bude předpokládat, že váš firmware nastaví určitý limit na osu. Pokud zrychlení podavače překročí toto nastavení, odhad času těchto pohybů bude upraven tak, aby předpokládal, že váš firmware zrychlení omezuje. Celkové zrychlení může být stále větší, když se diagonálně zrychluje s více osami současně.

Je zcela běžné, že jsou dodrženy limity zrychlení podavače, protože (v závislosti na firmwaru) zrychlení nastavené aplikací Cura ovlivňuje také podavač. Proto je důležité, aby toto nastavení bylo správně nakonfigurováno, aby se získaly správné odhady času pro retrakce.

*Protože se jedná o nastavení stroje, není toto nastavení normálně v seznamu nastavení viditelné.*