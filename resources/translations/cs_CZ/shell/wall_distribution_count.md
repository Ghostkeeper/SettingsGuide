Počet rozdělení na stěnách
====
Cura dokáže upravit šířku linií stěn tak, aby lépe odpovídaly tisknutému tvaru, ale nemusí upravit každou stěnu o stejnou hodnotu. Raději mění šířku stěn více směrem dovnitř modelu. Toto nastavení určuje počet stěn, počítáno zevnitř ven, které se upraví tak, aby se vešly do dostupného prostoru.

![Koncentrované uprostřed, s velkými rozdíly v šířce linií](../../../articles/images/wall_distribution_count_1.png)
![Rozprostřené přes mnoho stěn](../../../articles/images/wall_distribution_count_5.png)

Stěny s proměnlivou šířkou se tisknou obtížněji než jednoduché stěny s konstantní šířkou. Trvá nějakou dobu, než se nastaví rychlost proudění z trysky, a při přechodu je také třeba udělat několik ostrých rohů, které mohou způsobit zvlnění. To vše je nejlepší provádět co nejdále od vnějšího povrchu, kde by to bylo na povrchu tisku vidět. Cura tedy soustředí úpravy šířky linie na nejvnitřnější stěny.

Na druhou stranu soustředění variací také znamená, že tyto linie uprostřed budou mít značně rozdílnou šířku. Rozložení na více linií znamená, že amplituda odchylek může být menší, čímž se vliv proměnlivé šířky linie zmenší, místo aby se skryl uvnitř.

Tímto nastavením se vybere několik stěn z vnitřní strany, mezi nimiž lze upravit šířku linie tak, aby vyplnila dostupný prostor. Počítá se v obou směrech od středu, takže pokud je nastavena hodnota 2, lze ve středu nastavit až 4 stěny. Ani v rámci těchto stěn není úprava rozložena rovnoměrně. Stěny uprostřed budou vždy upraveny o něco více než stěny blíže k vnějšímu okraji.

Vnější stěna se vždy udržuje na jmenovité šířce linie, pokud je to možné. Tato stěna má takový vliv na kvalitu tisku, že se udržuje na konstantní šířce linie, aby byl povrch co nejhladší. Pouze v případě, že je kus tak tenký, že se skládá pouze z vnějších stěn, budou tyto stěny upraveny.

V praxi je skrytí nedokonalostí uprostřed téměř vždy lepší strategií než rozprostření nedokonalostí na více stěn. V důsledku toho je nejlepší ponechat toto nastavení co nejnižší. Při práci s materiály, které se obtížně vytlačují nebo u nichž se obtížně mění tok, jako jsou pružné materiály, pomáhá toto nastavení zvýšit, aby se snížily změny toku. Nikdy však nemůže těmto změnám toku zcela zabránit.

**Toto nastavení se nevztahuje pouze na běžné stěny, ale také na dodatečné stěny, podpůrné stěny, výplňové stěny a soustředné vzory.**