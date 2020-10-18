Preferovat retrakci
====
Kompenzace překrývajících se linií stěn sníží tok některých stěn. Pokud se tento tok sníží pod hodnotu parametru [Minimální tok pro stěny](wall_min_flow.md), provede se místo linie stěny, přesun.

Pokud je tento parametr aktivován, bude vlákno během tohoto pohybu přesunu zasunuto.

Cílem této úpravy je snížit výtok na stěnách. Účelem této úpravy je omezit výtok na extrémně tenkých stěnách, což není příliš hezké. Tento výsledek je možné dále vylepšit aktivací tohoto nastavení.

Retrakce na vnějších stěnách však způsobuje dočasné zastavení trysky, zatímco je vlákno zasunuto. To zanechává skvrnu na povrchu, kde bylo provedeno stažení. Zvyšuje také čas tisku a rychleji se opotřebuje vlákno.