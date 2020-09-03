Výška vrstvy
====
3D tiskárna ukládá plasty ve vrstvách. Výška vrstev je tloušťka těchto vrstev v milimetrech. Toto je nejdůležitější faktor jak pro vizuální kvalitu výsledného tisku, tak pro dobu tisku.

![Výška vrstvy 0,1 mm](../../../articles/images/layer_height_0.1.png)
![Výška vrstvy 0,2 mm](../../../articles/images/layer_height_0.3.png)

Výška vrstvy je nejdůležitějším parametrem ovlivňujícím celkovou kvalitu a naopak dobu tisku. To jsou jen některé z vlivů:
* Tenčí vrstvy zvyšují vizuální kvalitu tisku. Protože jsou vrstvy tenčí, bude se stupňový efekt na okrajích vrstvy snižovat. Kromě toho budou vrstvy blíže k sobě a záhyby mezi vrstvami budou proto menší, což celkově poskytne hladší povrch.
* Tenčí vrstvy umožňují tiskárně produkovat více detailů na horní a spodní straně tisku.
* Silnější vrstvy mají sklon k tomu, aby byl tisk, až do určitého bodu silnější. Mezi vrstvami bude méně hranic, což je slabou stránkou. Silnější vrstvy se nebudou tolik stříhat.
* Silnější vrstvy zkracují dobu tisku, protože tryska nemusí provádět tolik horizontálních pohybů.

Výška vrstev vzhledem k profilům
----
Mnoho parametrů závisí na výšce vrstvy. Protože výška vrstvy výrazně ovlivňuje tok materiálu tryskou, mění se mnoho parametrů tiskového procesu. To je velmi složité. Například, když zvětšíte výšku vrstvy, pravděpodobně budete muset mírně zvýšit teplotu tisku, abyste kompenzovali mimořádnou rychlost ztráty tepla. Teplota pak ovlivňuje likviditu materiálu, což ovlivní ostrost vašich rohů a potřebné chlazení atd. Je vždy dobré začít s předem stanoveným profilem kvality, který je k dispozici pro vaši tiskárnu a jeho výška se blíží tomu, co chcete.

Požadovanou výšku vrstvy si můžete vybrat v uživatelském režimu, ale prefabrikované profily jsou k dispozici také v různých výškách vrstvy. Profily pro různé výšky vrstev můžete vybrat v doporučeném režimu pomocí posuvníku nebo pomocí rozbalovacího widgetu v uživatelském režimu. Protože tyto profily také upravují určité parametry, které závisí na výšce vrstvy, pravděpodobně tímto způsobem dosáhnete lepší kvality.

Další poznámky
----
Při velmi nízké výšce vrstvy se můžete dostat do limitu rozlišení vaší osy Z. Zkontrolujte velikost kroku osy Z vaší tiskárny a ujistěte se, že výška vrstvy je jeho násobkem. Pokud se neshodují, některé vrstvy budou silnější než jiné, což způsobí pruhy.

**Mějte na paměti, že nastavení výšky vrstvy se nevztahuje na počáteční vrstvu tisku nebo na vrstvy voru, které mají svá vlastní samostatná nastavení pro úpravu výšky vrstev. Při použití adaptivních vrstev bude toto nastavení výšky vrstvy použito jako základní linie, ale skutečná výška vrstvy bude mít určité variace.**