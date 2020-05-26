Použít věže
====
Malé převislé povrchy vytvářejí malé sloupky podpěry. Tyto sloupy mají sklon k převrácení. Místo těchto malých sloupů může Cura generovat specializované věže, větší a robustnější, aby se zabránilo převrácení podpěry.

![Věž podpírá meč, který by jinak měl velmi malou převislou plochu](../images/support_use_towers_cs.svg)

Převislé oblasti menší než [Minimální průměr nesený podpůrnou věží](support_minimal_diameter.md), budou podpírány takovou věží namísto běžné podpůrné struktury. Tyto věže jsou širší, aby se nerozpadly. V blízkosti vrcholu věže se věž zužuje směrem k šířce převislé plochy, která skutečně potřebuje podpěru.

Tyto věže mají větší průměr než oblast, kterou podpírají. Díky tomu jsou věže stabilnější než obvyklá podpěra, ale také vyžadují více materiálu, času tisku a místa na vaší podložce tisku.
