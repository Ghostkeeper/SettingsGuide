Struktura podpěry
====
S tímto nastavením si můžete vybrat, který algoritmus použijete k vytvoření podpůrných struktur. Tyto konstrukce mají výrazně odlišné vlastnosti, takže výběr algoritmu bude mít velký vliv na to, jak dobře bude váš tisk podpírán. K dispozici jsou dvě možnosti.

Normální
----
![Normální podpůrná konstrukce](../../../articles/images/support_type_everywhere.png)

Jedná se o tradiční podpůrnou strukturu, na kterou je většina lidí zvyklá. Struktura je generována pod převislými oblastmi a obvykle je vyplněna vzorem, který přímo podpírá převislé oblasti. Odtud klesá přímo dolů, dokud nedosáhne tiskovou podložku nebo části modelu, kterou podpírá.

Normální konstrukce podpěry byla výchozí pro většinu historie 3D tisku a funguje podobně ve všech slicerech. Toto je zlatý standard, a ne bez důvodu:
* Díky své robustní struktuře, velkým kontaktním plochám na modelu a podložce tisku je velmi spolehlivá. Odpouští velmi špatné nastavení nebo špatně naladěné tiskárny.
* Protože je tvar jednoduchý, lze ji rychle slicovat.
* Přímou strukturu podpěry lze snadno přizpůsobit pro uživatele, protože je okamžitě jasné, které hranice budou podpírány a které nikoli.

Nejdůležitější nevýhody vyplývají ze stejných vlastností:
* Díky velkým kontaktním oblastem je podpěra často obtížně odstranitelná a může na povrchu, kde se dotýká, zanechat značné jizvy.
* Přestože je stabilní, může spotřebovat spoustu materiálu a tisk může zabrat spoustu času. To lze do určité míry potlačit pomocí [kónické podpěry](../experimental/conical_overhang_enabled.md).

Protože podpěra bude obvykle velká a široká, je pro správné podepření povrchu potřeba [výplňový vzor](support_pattern.md). Cik-cak vzor výplně může být použit k tisku podpěry z velké části z jedné linie a pro umožnění snadnějšího odstranění. Další vzory lze kombinovat s extra [obrysy](support_wall_count.md) aby byla podpěra místo toho robustní.

Strom
----
![Stromová podpěra](../../../articles/images/support_structure_tree.png)

Při stromové podpěře začne podpůrná struktura na desce sestavy malá a její větve rostou směrem k částem tisku, které potřebují podepřít.

Stromová podpěra se může vyhnout překážkám, když roste směrem k převislým oblastem, protože nemusí splývat přímo dolů. Pokud je to vůbec možné, bude podpěra spočívat pouze na tiskové podložce, aby se zabránilo zjizvení povrchu, na kterém podpěra spočívá. Pokud z podložky tisku k převisu neexistuje žádná cesta, bude podpěra spočívat na povrchu, který je co nejblíže převisu, aby se minimalizovalo použití materiálu. Větve stromové podpěry jsou omezeny hodnotou parametru [Úhel větve stromové podpěry](support_tree_angle.md) takže samotné nevytváří příliš strmý převis. To omezuje schopnost růst kolem překážek a také určuje výšku, ve které se kmeny začnou rozvětvovat.

Konstrukce stromové podpěry má oproti běžné podpěře řadu velkých výhod:
* Stromová podpěra často používá mnohem méně materiálu než běžná podpěra. Běžné je 25 až 50% využití materiálu. To šetří spoustu času a snižuje náklady na tisk.
* Vzhledem k jeho malé kontaktní ploše má převis při použití stromové podpěry tendenci vypadat lépe.
* Také díky malé kontaktní oblasti bude podpěru snadnější odstranit.
* Zanechává na povrchu méně jizev než běžná podpěra, protože je schopna se pohybovat kolem modelu od tiskové podložky směrem k převisu.

Hlavní nevýhody jsou:
* Slicování trvá podstatně déle než normální podpěra. Bude zapotřebí trpělivosti, zejména u vysokých modelů.
* Při tisku nejmenších větví dochází v toku k mnoha přerušením, což způsobuje, že stromová podpěra není vhodná pro tisk pomocí materiálů, které lze těžko vytlačovat, jako je PVA nebo pružné materiály.
* Stromová podpěra nefunguje dobře pro podpírání některých mechanických modelů. Zejména má tendenci umísťovat příliš málo větví na podporu plochých, šikmých převisů.

Ve výchozím nastavení je stromová podpěra dutá. Větve budou mít malý hrot, takže výplňový vzor neposkytuje zvláštní podporu pro převislý povrch tištěné položky. Díky svému zubatému tvaru je stromová podpěra obvykle poměrně robustní. Běžná nastavení podpěry však stále platí pro oblast ohraničenou větvemi stromu. Pro zvýšení pevnosti podpůrné struktury může být použit parametr [Hustota podpěry](support_infill_rate.md).