Monotónní uspořádání horního povrchu
====
Normálně Cura řadí linie tak, aby vzdálenost mezi nimi byla malá. Pokud je toto nastavení povoleno, uspořádá linie horního povrchu tak, aby se sousední linie tiskly vždy s překrytím ve stejném směru.

Při tisku linií horní plochy se linie obvykle trochu překrývají s liniemi vedle nich, protože tvar linie není dokonalý obdélník. Díky tomuto překrytí mají linie mírný sklon, což způsobuje, že odrážejí světlo různými směry. Pokud se sousední linie různě překrývají, tento odraz se mění. To je vidět na konečném výsledku. Různé oblasti povrchu se díky tomu různě lesknou. Tisk v monotónním pořadí zajišťuje, že překrytí je na celém povrchu stejné, takže se neliší v tom, jak odráží světlo. Díky tomu vypadá povrch konzistentněji a hladčeji.

![Nejedná se o monotónní pořadí](../../../articles/images/skin_monotonic_disabled.gif)
![Monotónní pořadí, vždy od pravého dolního rohu](../../../articles/images/skin_monotonic_enabled.gif)

Monotónní pořadí mírně prodlouží délku přesunů, ale tento vliv je velmi minimální. Má pouze vizuální efekt na tisk. Monotónní řazení nemá žádné mechanické výhody.

Chcete-li dosáhnout hladkého povrchu, zvažte kombinaci tohoto nastavení s nastavením [režimu objíždění](../travel/retraction_combing.md), abyste se vyhnuli tvorbě koženého povrchu, a případně zapněte [Z-skoky](../travel/retraction_hop.md). Případně můžete také povolit [žehlení](../top_bottom/ironing_enabled.md), ale to zcela přehluší užitečnost tohoto nastavení. Žehlení má vlastní volbu [monotónní uspořádání](../top_bottom/ironing_monotonic.md).